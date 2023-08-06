#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
SSH remote proxy for monitoring and notifying file changes.
"""

import base64
import os
import sys
import traceback


if __name__ == '__main__':
    try:

        import pyinotify

        class Mainloop:
            """
            This program is not directly used in the process of the Parzzley engine but is copied to a remote system and
            controlled via an ssh session as a proxy for doing some tasks on this remote system.
            """

            def __init__(self):
                self.rootdir = os.path.abspath(sys.argv[1])
                self.rootcdir = f"{self.rootdir}/.parzzley.control/"

            def run(self):
                rlen = len(self.rootdir)

                def _proc_fun(event):
                    if f"{event.pathname}/".startswith(self.rootcdir):
                        return
                    sys.stdout.write(f":PARZZLEY:{base64.b64encode(event.pathname[rlen:].encode()).decode()}\n")
                    sys.stdout.flush()

                wm = pyinotify.WatchManager()
                notifier = pyinotify.Notifier(wm)
                flags = pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_CLOSE_WRITE'] | \
                    pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_MOVED_FROM'] | \
                    pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_MOVED_TO'] | \
                    pyinotify.EventsCodes.FLAG_COLLECTIONS['OP_FLAGS']['IN_DELETE']
                wm.add_watch(self.rootdir, flags, rec=True, auto_add=True, proc_fun=_proc_fun)
                notifier.loop()

        Mainloop().run()

    except Exception:
        sys.stdout.write(f":PARZZLEY:ERROR:{base64.b64encode(traceback.format_exc().encode()).decode()}\n")
        sys.stdout.flush()
