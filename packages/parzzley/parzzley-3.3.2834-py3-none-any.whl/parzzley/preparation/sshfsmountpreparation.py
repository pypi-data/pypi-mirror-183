# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import os
import signal
import subprocess
import threading
import time
import typing as t

import parzzley.config.configpiece
import parzzley.preparation.mountpreparation
import parzzley.tools.common
import parzzley.tools.networking

if t.TYPE_CHECKING:
    import parzzley.runtime.runtime


class SshfsMountPreparation(parzzley.preparation.mountpreparation.MountPreparation):
    """
    Mounts remote filesystems with sshfs.
    """

    def __init__(self, *, src: str, tgt: str, idfile: t.Optional[str] = None, password: t.Optional[str] = None,
                 port: int = 22, timeout: t.Union[datetime.timedelta, str] = "10s", **kwargs):
        super().__init__(src=src, tgt=tgt, **kwargs)
        self.idfile = idfile
        self.password = password
        self.port = int(port)
        self.timeout = parzzley.config.configpiece.gettimedelta(timeout)

    def __str__(self):
        return f"[{type(self).__name__},{self.src}]"

    @staticmethod
    def translate_to_alternative_endpoint(src: str, port: int,
                                          runtime: 'parzzley.runtime.runtime.RuntimeData') -> t.Tuple[str, int]:
        u = ""
        pa = ""
        i = src.find("@")
        if i > -1:
            u = src[:i + 1]
            src = src[i + 1:]
        i = src.rfind(":")
        if i > -1:
            pa = src[i:]
            src = src[:i]
        m, p = parzzley.tools.networking.translate_parzzley_portforwarding(src, port, runtime)
        return u + m + pa, p

    def enable(self, runtime):
        ret = None
        def timeoutthread(_p, secs):
            nonlocal ret
            for i in range(int(secs * 10)):
                time.sleep(0.1)
                if ret is not None:
                    break
            try:
                _p.send_signal(signal.SIGINT)
            except Exception:
                pass
        try:
            if not os.path.exists(self.tgt):
                os.makedirs(self.tgt)
            opts = []
            port = 22
            if self.port:
                port = self.port
            (real_src, real_port) = SshfsMountPreparation.translate_to_alternative_endpoint(self.src, port, runtime)
            opts += ["-p", str(real_port)]
            opts += [real_src, self.tgt]
            if self.idfile:
                opts += ["-o", "IdentityFile=" + self.idfile]
            for option in self.options:
                opts.append(option)
            if self.password:
                opts += ["-o", "password_stdin"]
            sacm = str(max(int(self.timeout.total_seconds() / 2), 2))
            opts += ["-o", "ServerAliveCountMax=" + sacm, "-o", "ServerAliveInterval=2"]
            pwd = (self.password + "\n").encode("utf-8") if self.password else ""
            parzzley.preparation.mountpreparation.MountPreparation._checkmountpointempty(self.tgt)
            p = subprocess.Popen(["sshfs", *opts], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            threading.Thread(target=timeoutthread, args=(p, self.timeout.total_seconds() * 3)).start()
            if self.password:
                time.sleep(2)
            rr = p.communicate(pwd)
            r = rr[0].decode("utf-8") + "; " + rr[1].decode("utf-8")
            p.stdin.close()
            ret = p.wait()
            if ret != 0:
                raise Exception(f"{self.src} not mounted: {r}")
        finally:
            if ret is None:
                ret = -1  # stop the thread under all circumstances

    def disable(self, runtime):
        try:
            # noinspection PySimplifyBooleanCheck
            if self.getstate(runtime) is False:
                return
        except Exception:
            pass
        parzzley.tools.common.call("sync")
        parzzley.tools.common.call("sync")
        (ret, r) = parzzley.tools.common.call("fusermount", "-u", self.tgt)
        if ret != 0:
            raise Exception(f"{self.src} not unmounted: {r}")
