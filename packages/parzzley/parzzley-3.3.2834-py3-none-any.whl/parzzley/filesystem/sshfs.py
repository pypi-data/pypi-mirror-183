# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import base64
import datetime
import os
import shutil
import subprocess
import threading
import time

import parzzley.config.configpiece
import parzzley.exceptions
import parzzley.filesystem.abstractfilesystem
import parzzley.filesystem.local
import parzzley.logger
import parzzley.preparation.sshfsmountpreparation

try:
    import fcntl
except ImportError:
    fcntl = None


class SyncSshFilesystemError(parzzley.filesystem.abstractfilesystem.SyncFilesystemError):
    pass


class SyncSshFilesystemRemoteProxyError(SyncSshFilesystemError):
    pass


class SshfsFilesystem(parzzley.filesystem.local.LocalFilesystem):
    """
    A location in a (remote) ssh filesystem.
    Please note that remote ssh filesystems have to be manually prepared before using with Parzzley. This is
    needed for some detection features. Please create the directory `.parzzley.control` in the root directory of
    a directory structure, before you try to sync it via ssh with Parzzley!
    """

    def __str__(self):
        return f"[ssh port:{self.port} {self.rootpath}]"

    def __init__(self, *aspects, name, sshtarget, path, idfile=None, password=None, port="22",
                 timeout="10s", **kwa):
        self.options = parzzley.config.configpiece.getlist(kwa, "options")
        super().__init__(*aspects, name=name, path=None, **kwa)
        # (we set the path later on)
        self.sshtarget = sshtarget
        self.targetpath = path
        self.idfile = idfile
        self.password = password
        self.port = int(port)
        self.timeout = parzzley.config.configpiece.gettimedelta(timeout)
        self.sshxattrproxy = None
        self._sshpreparationadded = False
        self._initialize_populate_automatically = False
        self.sshpath = None

    def initialize(self, sync, runtime):
        r_target, r_port = parzzley.preparation.sshfsmountpreparation.SshfsMountPreparation.\
            translate_to_alternative_endpoint(self.sshtarget, self.port, runtime)
        self.sshtarget = r_target
        self.port = r_port
        self.sshpath = f"{self.sshtarget}:{self.targetpath}"
        mountdir = f"{runtime.datadir}/mounts/{sync.name}"
        if not os.path.isdir(mountdir):
            os.makedirs(mountdir)
        self.rootpath = mountdir
        self.sshxattrproxy = None
        if not self._sshpreparationadded:
            sshmountpreparation = parzzley.preparation.sshfsmountpreparation.SshfsMountPreparation(
                src=self.sshpath, timeout=self.timeout, tgt=mountdir, idfile=self.idfile, port=self.port,
                password=self.password, options=self.options)
            sync.preparations.append(sshmountpreparation)
            self._sshpreparationadded = True
        super().initialize(sync, runtime)

    def shutdown(self, sync, runtime):
        super().shutdown(sync, runtime)
        if self.sshxattrproxy:
            self.sshxattrproxy.shutdown()
            runtime.log(subject=f"Spent {self.sshxattrproxy.benchmark.total_seconds()} seconds in ssh remote proxy.",
                        severity=parzzley.logger.Severity.DEBUG)

    class _SshXattrProxy:

        def _waitanswer(self, endstring, additionaltimeout=0):
            self._ready = False
            self._quark = ""
            self._stopreadywaitthread = False

            def readywaitthread():
                self._quark = ""
                self._finished = False
                while not self._finished and not self._stopreadywaitthread:
                    t = self.sout.read()
                    if t:
                        self._quark += t.decode()
                    self._finished = self._quark.endswith(f"{endstring}\n")
                    if not self._finished:
                        time.sleep(0.002)
                with self.readywaitlock:
                    self._ready = True
                    self.readywaitcondition.notify_all()

            threading.Thread(target=readywaitthread).start()
            timeout = additionaltimeout * 2 + 20  # some extra seconds :)
            with self.readywaitlock:
                while (not self._ready) and (timeout > 0) and (self.sshproc.poll() is None):
                    self.readywaitcondition.wait(0.5)
                    timeout -= 1
            if self.sshproc.poll() is not None:
                raise SyncSshFilesystemRemoteProxyError("ssh xattr remote proxy terminated unexpectedly. received: " +
                                                        self._quark)
            if not self._ready:
                raise SyncSshFilesystemRemoteProxyError("timeout in communication with the remote ssh xattr proxy. "
                                                        "received so far: " + self._quark)
            return self._quark

        def __init__(self, sshfs):
            self.sshfs = sshfs
            self.benchmark = datetime.timedelta()
            sshfscontrolfs = self.sshfs.get_control_filesystem()
            if not sshfscontrolfs.is_really_onvolume:
                raise parzzley.exceptions.ConfigurationError("The Parzzley ssh proxy does not support filesystems"
                                                             " without an embodied control directory"
                                                             " (e.g. read-only ones).")
            proxyfilename = __file__
            _relproxyfilename = "/tools/sshxattrproxy.py"
            while not os.path.isfile(proxyfilename + _relproxyfilename) \
                    and proxyfilename != os.path.dirname(proxyfilename):
                proxyfilename = os.path.dirname(proxyfilename)
            proxyfilename += _relproxyfilename
            fullproxypath = sshfscontrolfs.getfulllocalpath("/sshxattrproxy.py")
            shutil.copyfile(proxyfilename, fullproxypath)
            os.chmod(fullproxypath, 0o755)
            self.sshproc = subprocess.Popen(["ssh", self.sshfs.sshtarget, "-p", str(self.sshfs.port), "-i",
                                            self.sshfs.idfile] + self.sshfs.options +
                                            [f"{self.sshfs.targetpath}/" +
                                             sshfscontrolfs.translate_path("/sshxattrproxy.py", self.sshfs)],
                                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.sin = self.sshproc.stdin
            self.sout = self.sshproc.stdout
            fcntl.fcntl(self.sout, fcntl.F_SETFL, fcntl.fcntl(self.sout, fcntl.F_GETFL) | os.O_NONBLOCK)
            self.readywaitlock = threading.Lock()
            self.readywaitcondition = threading.Condition(self.readywaitlock)
            self._waitanswer(endstring="SSHXATTRPROXY_READY", additionaltimeout=self.sshfs.timeout.total_seconds())
            if self.request(("init", self.sshfs.targetpath)) != "ACK":
                raise SyncSshFilesystemRemoteProxyError("internal error while initializing the remote ssh xattr proxy.")

        def request(self, command):
            _bench1 = datetime.datetime.now()
            rawcmd = base64.b64encode(repr(command).encode(errors="backslashreplace"))
            self.sin.write((rawcmd+b"\n"))
            self.sin.flush()
            rawans = self._waitanswer(endstring=" DONE")[:-5].strip()
            doraise = False
            if rawans.endswith(" RAISE"):
                doraise = True
                rawans = rawans[:-6]
            ans = base64.b64decode(rawans.encode()).decode()
            self.benchmark += (datetime.datetime.now() - _bench1)
            if doraise:
                try:
                    ex = eval(ans)
                except Exception:
                    ex = SyncSshFilesystemRemoteProxyError(f"Unserializable exception from remote ssh xattr"
                                                           f" proxy: {ans}")
                raise ex
            return eval(ans)

        def shutdown(self):
            try:
                self.request(("shutdown",))
            except Exception:
                pass

    def getsshxattrproxy(self):
        if self.sshxattrproxy is None:
            # noinspection PyProtectedMember
            self.sshxattrproxy = SshfsFilesystem._SshXattrProxy(self)
        return self.sshxattrproxy

    def listxattrkeys(self, path):
        return self.getsshxattrproxy().request(("listxa", path))

    def getxattrvalue(self, path, key):
        return self.getsshxattrproxy().request(("getxa", path, key))

    def setxattrvalue(self, path, key, value):
        return self.getsshxattrproxy().request(("setxa", path, key, value))

    def unsetxattrvalue(self, path, key):
        return self.getsshxattrproxy().request(("unsetxa", path, key))
