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
            <aspect type="TrashRemove" trashdelay="10s"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="TrashRemove" trashdelay="10s"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("s/_dummy", "")

        write2file("m/x", "x1")
        write2file("m/y", "y")
        write2file("m/z", "z")
        time.sleep(1)
        write2file("s/x", "x2")
        write2file("s/y", "y")
        write2file("s/z", "z")

        tt = time.time()
        os.utime(mydir + "m/z", (tt, tt))
        os.utime(mydir + "s/z", (tt, tt))

        try:
            SYNC()
        except:
            pass
        self.assertTrue(readfile("m/x") == "x1")
        self.assertTrue(readfile("s/x") == "x2")
        self.assertTrue(readfile("m/y") == "y")
        self.assertTrue(readfile("s/y") == "y")
        self.assertTrue(readfile("m/z") == "z")
        self.assertTrue(readfile("s/z") == "z")
        self.assertFalse(haslogentry("y", verb="updated"))
        self.assertFalse(haslogentry("z", verb="updated"))

        write2file("s/y", "y2")
        write2file("m/z", "z2")
        SYNC()
        self.assertTrue(readfile("m/x") == "x1")
        self.assertTrue(readfile("s/x") == "x2")
        self.assertTrue(readfile("m/y") == "y2")
        self.assertTrue(readfile("s/y") == "y2")
        self.assertTrue(readfile("m/z") == "z2")
        self.assertTrue(readfile("s/z") == "z2")


if __name__ == '__main__':
    unittest.main()
