#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
SSH remote proxy for exchange of file metadata.
"""

import base64
import datetime
import os
import sys
import threading
import time
import xattr


class Mainloop:
    """
    This program is not directly used in the process of the Parzzley engine but is copied to a remote system and
    controlled via an ssh session as a proxy for doing some tasks on this remote system that cannot be done via an
    sshfs mount.
    """

    def __init__(self):
        self.rootdir = None
        self.lastalive = datetime.datetime.now()
        self.lastalivelock = threading.Lock()
        self.running = True

    def _watchdog(self):
        while True:
            time.sleep(60)
            with self.lastalivelock:
                if (datetime.datetime.now() - self.lastalive).total_seconds() >= 60 * 60 * 2:
                    # noinspection PyProtectedMember,PyUnresolvedReferences
                    os._exit(1)

    def run(self):
        sys.stdout.write("SSHXATTRPROXY_READY\n")
        sys.stdout.flush()
        threading.Thread(target=self._watchdog).start()
        while True:
            rawreq = sys.stdin.readline()
            req = eval(base64.b64decode(rawreq).decode())
            doraise = False
            try:
                res = repr(self.processrequest(req))
            except Exception as e:
                res = repr(e)
                doraise = True
            rawres = base64.b64encode(res.encode(errors='backslashreplace')).decode()
            if doraise:
                rawres += " RAISE"
            sys.stdout.write(f"{rawres} DONE\n")
            sys.stdout.flush()
            with self.lastalivelock:
                self.lastalive = datetime.datetime.now()
            if not self.running:
                # noinspection PyProtectedMember
                os._exit(0)

    def processrequest(self, req):
        cmd = req[0]
        if cmd == "init":
            self.rootdir = req[1]
            return "ACK"
        elif cmd == "listxa":
            fpath = f"{self.rootdir}/{req[1]}"
            res = xattr.list(fpath)
            return [x.decode("utf-8") for x in res]
        elif cmd == "getxa":
            fpath = f"{self.rootdir}/{req[1]}"
            key = req[2]
            # noinspection PyUnresolvedReferences
            return xattr.get(fpath, key).decode("utf-8")
        elif cmd == "setxa":
            fpath = f"{self.rootdir}/{req[1]}"
            key = req[2]
            value = req[3]
            xattr.set(fpath, key, value)
            return None
        elif cmd == "unsetxa":
            fpath = f"{self.rootdir}/{req[1]}"
            key = req[2]
            xattr.remove(fpath, key)
            return None
        elif cmd == "shutdown":
            self.running = False
        else:
            raise Exception(f"command not understood: {cmd}")


if __name__ == '__main__':
    Mainloop().run()
