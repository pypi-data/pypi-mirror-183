# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import base64
import datetime
import fcntl
import os
import subprocess
import sys
import threading
import time
import traceback

if __name__ == "__main__":
    sys.path.append(os.path.abspath(f"{__file__}/../../.."))

import parzzley.aspect.abstractaspect
import parzzley.filesystem.sshfs
import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.common
import parzzley.exceptions


class MonitorFileChanges(parzzley.aspect.abstractaspect.Aspect):
    """
    Tries to establish a proxy on the other end of an ssh filesystem connection
    that monitors file changes. If changes appear, a sync is triggered for the
    next possible moment. It only works on parzzley.filesystem.sshfs.SshfsFilesystem's.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def _beginsync(self, ctx, filesystem):
        """
        Establishes the proxy.
        """
        import psutil
        if not isinstance(filesystem, parzzley.filesystem.sshfs.SshfsFilesystem):
            raise parzzley.exceptions.ConfigurationError("MonitorFileChanges is only allowed in SshfsFilesystem "
                                                        "filesystems.")
        if not hasattr(ctx.syncglobaldata, "monitorfilechanges_notifyonly_storage"):
            ctx.syncglobaldata.monitorfilechanges_notifyonly_storage = \
                parzzley.runtime.datastorage.get_storage_department(
                    ctx, "monitorfilechanges_notifyonly", location=parzzley.runtime.datastorage.StorageLocation.SYSTEM,
                    scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
            ctx.syncglobaldata._monitorfilechanges_asynclog_storage = \
                parzzley.runtime.datastorage.get_storage_department(
                    ctx, "monitorfilechanges_asynclog", location=parzzley.runtime.datastorage.StorageLocation.SYSTEM,
                    scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
            ctx.syncglobaldata.monitorfilechanges_filesseen = {}
            ctx.syncglobaldata.monitorfilechanges_filesseen_inbetween = {}
            ctx.syncglobaldata.monitorfilechanges_filesseen_lock = threading.Lock()
        ctx.syncglobaldata.monitorfilechanges_filesseen[filesystem] = []
        threading.Thread(target=self.filesseenwriterthread,
                         args=(ctx.sync, filesystem, ctx.syncglobaldata.monitorfilechanges_notifyonly_storage,
                               ctx.syncglobaldata.monitorfilechanges_filesseen,
                               ctx.syncglobaldata.monitorfilechanges_filesseen_lock)).start()
        asynclogpath = ctx.syncglobaldata._monitorfilechanges_asynclog_storage.get_filesystem(
            sync=ctx.sync).getfulllocalpath(filesystem.name)
        os.makedirs(asynclogpath, exist_ok=True)
        for lent in sorted(os.listdir(asynclogpath)):
            flent = asynclogpath + "/" + lent
            with open(flent, "r") as f:
                cnt = f.read()
            os.unlink(flent)
            ctx.logproblem(filesystem, "file change monitoring", comment=f"{lent}\n{cnt}")
        ptoken = "parzzleychangemonitor:" + base64.b64encode(ctx.sync.name.encode()).decode() + "." \
                 + base64.b64encode(filesystem.name.encode()).decode() + "."
        for pid in psutil.pids():
            try:
                if ptoken in psutil.Process(pid).cmdline():
                    return
            except psutil.NoSuchProcess:
                pass  # gone meanwhile
        proxyfilename = __file__
        _relproxyfilename = "/tools/sshchangenotifyproxy.py"
        while not os.path.isfile(proxyfilename + _relproxyfilename) \
                and proxyfilename != os.path.dirname(proxyfilename):
            proxyfilename = os.path.dirname(proxyfilename)
        proxyfilename += _relproxyfilename
        controlfs = filesystem.get_control_filesystem()
        controlfs.copyfile(proxyfilename, "/sshchangenotifyproxy.py")
        pxpath = filesystem.targetpath + "/" + controlfs.translate_path("/sshchangenotifyproxy.py", filesystem)
        lastsuccfile = ctx.sync_success_storage.get_value_path(ctx.sync)
        notifyonlylist = ctx.syncglobaldata.monitorfilechanges_notifyonly_storage.get_filesystem(
            sync=ctx.sync).getfulllocalpath("list")
        subprocess.Popen(["nohup", "/usr/bin/python3", __file__, filesystem.sshtarget, str(filesystem.port),
                          filesystem.idfile, pxpath, filesystem.targetpath, ptoken, lastsuccfile,
                          notifyonlylist, asynclogpath] + filesystem.options,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_BeforeElectMaster)
    def _beforeelectmaster(self, ctx, filesystem):
        """
        Remembers which files have been seen, so we can catch just notifications for them (the other ones are not
        interesting).
        """
        pathx = ctx.syncglobaldata.monitorfilechanges_filesseen_inbetween.get(filesystem, None)
        ctx.syncglobaldata.monitorfilechanges_filesseen_inbetween[filesystem] = ctx.path
        if pathx:
            with ctx.syncglobaldata.monitorfilechanges_filesseen_lock:
                ctx.syncglobaldata.monitorfilechanges_filesseen[filesystem].append(pathx)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.CloseSync)
    def _closesync(self, ctx, filesystem):
        """
        Stops the filesseenwriter thread (and  more).
        """
        try:  # be very careful in CloseSync!
            with ctx.syncglobaldata.monitorfilechanges_filesseen_lock:
                ctx.syncglobaldata.monitorfilechanges_filesseen[filesystem] = None
        except Exception:
            ctx.logproblem(filesystem, "CloseSync", comment=traceback.format_exc())
        try:
            ffs = ctx.syncglobaldata.monitorfilechanges_notifyonly_storage.get_filesystem()
            ffs.removefile("list")
        except Exception:
            ctx.logproblem(filesystem, "CloseSync", comment=traceback.format_exc())

    def filesseenwriterthread(self, sync, filesystem, notifyonly_storage, filesseen, filesseen_lock):
        ffs = notifyonly_storage.get_filesystem(sync=sync)
        ffile = ffs.getfulllocalpath("list")
        with open(ffile, "w") as f:
            while True:
                with filesseen_lock:
                    if filesseen[filesystem] is None:
                        break
                    else:
                        _filesseen = filesseen[filesystem]
                        filesseen[filesystem] = []
                x = ""
                for fs in _filesseen:
                    x += fs + "\n"
                f.write(x)
                f.flush()
                time.sleep(0.5)

    @staticmethod
    def monitorproxy(sshtarget, port, idfile, proxypath, rvolpath, lastsuccfile, notifyonlylist, asynclogpath,
                     options):
        class RemoteException(Exception):
            pass
        try:
            sshproc = subprocess.Popen(["ssh", sshtarget, "-p", str(port), "-i", idfile] + options +
                                       ["/usr/bin/python3", proxypath, rvolpath],
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            sout = sshproc.stdout
            fcntl.fcntl(sout, fcntl.F_SETFL, fcntl.fcntl(sout, fcntl.F_GETFL) | os.O_NONBLOCK)
            _notifyonly = None
            _notifyonly_lock = threading.Lock()

            def readnotifyonlythread():
                nonlocal _notifyonly
                nonlocal _notifyonly_lock
                try:
                    while True:
                        try:
                            try:
                                with open(notifyonlylist, "r") as fnot:
                                    fcntl.fcntl(fnot, fcntl.F_SETFL, fcntl.fcntl(fnot, fcntl.F_GETFL) | os.O_NONBLOCK)
                                    with _notifyonly_lock:
                                        _notifyonly = set()
                                    while True:
                                        xx = [ln[:-1] for ln in fnot.readlines()]
                                        time.sleep(1.5)
                                        with _notifyonly_lock:
                                            _notifyonly.update(xx)
                                            if not os.path.exists(notifyonlylist):
                                                _notifyonly = None
                                                break
                            finally:
                                with _notifyonly_lock:
                                    _notifyonly = None
                        except IOError:
                            time.sleep(1)
                except Exception as e1:
                    with _notifyonly_lock:
                        _notifyonly = (e1, traceback.format_exc())

            threading.Thread(target=readnotifyonlythread, daemon=True).start()
            _lineprefix = b""  # this is required since readlines() can return an unfinished line at the end
            while True:
                lines = list(sout.readlines())
                if lines:
                    _lines = []
                    for line in lines:
                        _lineprefix = line = _lineprefix + line
                        if line.endswith(b"\n"):
                            _lineprefix = b""
                            line = line[:-1]
                            if line.startswith(b":PARZZLEY:ERROR:"):
                                raise RemoteException(base64.b64decode(line[15:]).decode())
                            elif line.startswith(b":PARZZLEY:"):
                                _lines.append(line[9:])
                            else:
                                with open(f"{asynclogpath}/{datetime.datetime.now().isoformat()}", "a") as f:
                                    f.write(f"Local part received corrupted line: {repr(line)}\n")
                    dostick = False  # if we actually flag the sync for immediate run
                    dostick_retrylater = False  # special situation (see below)
                    while True:
                        if dostick_retrylater:
                            time.sleep(2)
                        with _notifyonly_lock:
                            if _notifyonly is None:  # currently no sync is running
                                if dostick_retrylater:
                                    dostick = True
                                else:
                                    # if no sync is running, we wait a short time and check again, otherwise early sync
                                    # operations could trigger the file change detection
                                    dostick_retrylater = True
                                    continue
                            else:  # sync is running (handled later; here we just forward exceptions from the thread)
                                if isinstance(_notifyonly, tuple) and isinstance(_notifyonly[0], BaseException):
                                    raise Exception(f"filesseenwriter thread: {_notifyonly[1]}")
                            if (not dostick) and (not dostick_retrylater):  # sync is running (since first check!)
                                for line in _lines:
                                    lline = base64.b64decode(line).decode()
                                    if lline in _notifyonly:
                                        dostick = True
                                        break
                        break
                    if dostick:
                        with open(lastsuccfile, "r") as f:
                            cnt = f.read()
                        with open(lastsuccfile, "w") as f:
                            f.write(" " + cnt.lstrip())
                if sshproc.poll() is not None:
                    break
                time.sleep(1)
        except Exception as e:
            if isinstance(e, RemoteException):
                txt = "The remote part crashed."
                stack = e.args[0]
            else:
                txt = "The local part crashed."
                stack = traceback.format_exc()
            with open(f"{asynclogpath}/{datetime.datetime.now().isoformat()}", "a") as f:
                f.write(f"{txt}\n{stack}\n")


if __name__ == "__main__":
    sshtarget_ = sys.argv[1]
    port_ = sys.argv[2]
    idfile_ = sys.argv[3]
    proxypath_ = sys.argv[4]
    rvolpath_ = sys.argv[5]
    ptoken_ = sys.argv[6]
    lastsuccfile_ = sys.argv[7]
    notifyonlylist_ = sys.argv[8]
    asynclogpath_ = sys.argv[9]
    options_ = sys.argv[10:]
    MonitorFileChanges.monitorproxy(sshtarget_, port_, idfile_, proxypath_, rvolpath_, lastsuccfile_, notifyonlylist_,
                                    asynclogpath_, options_)
