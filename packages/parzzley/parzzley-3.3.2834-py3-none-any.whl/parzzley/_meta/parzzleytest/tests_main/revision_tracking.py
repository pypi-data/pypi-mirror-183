#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys
sys.path.append(os.path.abspath(__file__+"/../../.."))
from parzzleytest.test import *


class Test(unittest.TestCase):

    def test_main(self):

        setconfig("""<?xml version="1.0" ?>
<parzzleyconfig>
    <sync name="test" interval="0s">
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master">
            <aspect type="DefaultRemove"/>
            <aspect type="RevisionTracking"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="TrashRemove"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("m/a/b/c/x", "x")
        write2file("s/a/b/c/y", "y")
        write2file("m/f1", "1")
        write2file("m/f2", "1")
        write2file("s/f3", "1")
        write2file("s/_dummy", "")  # otherwise the other dir gets empty which is a bad thing for the watchdog
        SYNC()
        write2file("m/a/b/c/x", "X")
        deletefile("s/f1")
        SYNC()
        time.sleep(1)
        write2file("s/a/b/c/y", "Y")
        write2file("s/f1", "2")
        write2file("m/f2", "2")
        SYNC()
        time.sleep(1)
        deletedir("m/a")
        write2file("m/f1", "3")
        deletefile("m/f2")
        deletefile("s/f3")
        SYNC()
        deletefile("m/f1")
        SYNC()
        self.assertTrue(len(listdir("s")) == 2)
        self.assertTrue(len(listdir("m")) == 2)
        for f in [1, 2, 3]:
            p = "m/.parzzley.control/content_revisions/f{f}/".format(f=f)
            l = listdir(p)
            t = 4 - f
            self.assertTrue(len(l) == t)
            found = {}
            for kk in [1, 2, 3][:t]:
                found[kk] = False
            l.sort()
            for li, ll in enumerate(l):
                cont = readfile(p + ll)
                try:
                    if int(cont) == li + 1:
                        found[li + 1] = True
                except ValueError:
                    pass
            for kk in [1, 2, 3][:t]:
                self.assertTrue(found[kk])
        for f in ["x", "y"]:
            p = "m/.parzzley.control/content_revisions/a/b/c/" + f
            l = listdir(p)
            lo = False
            up = False
            for ll in l:
                t = readfile(p + "/" + ll)
                if t == f:
                    lo = True
                if t == f.upper():
                    up = True
            self.assertTrue(lo)
            self.assertTrue(up)
            self.assertTrue(len(l) == 2)


if __name__ == '__main__':
    unittest.main()
