# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys


def run() -> None:

    if len(sys.argv) < 2:
        print("""
Usage: {cmd} [command] [args]

The following commands are allowed:

- list: Lists all conflicts.

- gettasks [relpath]:

        Returns the task names that have flagged conflicts on this entry.

- getfsnames [task] [relpath]:

        Returns filesystem names that are potential solutions for a conflict.

- resolve [relpath] [task] [fsname]:

        Resolves the conflict for a given file (exactly as returned from
        'list') in a given task by flagging the given filesystem as the master.

The current working directory specifies on top of which Parzzley volume this
commands are applied.

Append '--controldir=/some/control/dir/path' if the synchronization is
configured to use a different control directory (more an exotic case).
        """.format(cmd=os.path.basename(sys.argv[0])))
        sys.exit(1)
    argcontroldir = "./.parzzley.control"
    for x in sys.argv:
        if x.startswith("--controldir="):
            argcontroldir = x[13:]
    if argcontroldir.startswith("./"):
        rootdir = os.getcwd()
        _l = None
        while not os.path.exists(rootdir + argcontroldir[1:]) and _l != rootdir:
            _l = rootdir
            rootdir = os.path.dirname(rootdir)
        controldir = rootdir + argcontroldir[1:]
        if not os.path.isdir(controldir):
            print("Please call this command somewhere from within a Parzzley volume.")
            sys.exit(2)
    else:
        controldir = argcontroldir
        if not os.path.isdir(controldir):
            print("Please specify an existing control directory.")
            sys.exit(2)
    if sys.argv[1] == "list":
        def helper(fr, fa):
            if os.path.exists(fa):
                for xfa in os.listdir(fa):
                    sr = f"{fr}/{xfa}"
                    sa = f"{fa}/{xfa}"
                    if os.path.isfile(sa):
                        with open(sa, "r") as fisa:
                            safsnames = [lnn for lnn in [ln.strip() for ln in fisa.readlines()] if lnn]
                        if len(safsnames) > 1:
                            print(sr[1:])
                    elif os.path.isdir(sa):
                        helper(sr, sa)
        if os.path.exists(f"{controldir}/conflicts"):
            for task in os.listdir(f"{controldir}/conflicts"):
                helper("", f"{controldir}/conflicts/{task}")
    elif sys.argv[1] == "gettasks":
        if os.path.exists(f"{controldir}/conflicts"):
            for task in os.listdir(f"{controldir}/conflicts"):
                if os.path.isfile(f"{controldir}/conflicts/{task}/{sys.argv[2]}"):
                    print(task)
    elif sys.argv[1] == "getfsnames":
        if os.path.exists(f"{controldir}/conflicts"):
            f = f"{controldir}/conflicts/{sys.argv[2]}/{sys.argv[3]}"
            if os.path.isfile(f):
                with open(f, "r") as fi:
                    fsnames = [lnn for lnn in [ln.strip() for ln in fi.readlines()] if lnn]
                print("\n".join(fsnames))
    elif sys.argv[1] == "resolve":
        with open(f"{controldir}/conflicts/{sys.argv[3]}/{sys.argv[2]}", "w") as fi:
            fi.write(sys.argv[4])
    else:
        print(f"Unknown command: {sys.argv[1]}")
        sys.exit(3)
