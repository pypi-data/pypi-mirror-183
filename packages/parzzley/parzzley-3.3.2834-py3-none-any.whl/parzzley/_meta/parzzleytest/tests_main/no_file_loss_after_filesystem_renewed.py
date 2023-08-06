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
            <aspect type="TrashRemove" trashdelay="20s"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="TrashRemove" trashdelay="20s"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("m/d1/d2/f1", "f1")
        write2file("s/f2", "f2")
        SYNC()
        self.assertTrue(readfile("m/d1/d2/f1") == "f1")
        self.assertTrue(readfile("m/f2") == "f2")
        self.assertTrue(readfile("s/d1/d2/f1") == "f1")
        self.assertTrue(readfile("s/f2") == "f2")
        deletedir("s")
        write2file("s/_dummy", "")
        try:
            SYNC()
        except Exception:
            pass
        SYNC()
        self.assertTrue(readfile("m/d1/d2/f1") == "f1")
        self.assertTrue(readfile("m/f2") == "f2")
        self.assertTrue(readfile("s/d1/d2/f1") == "f1")
        self.assertTrue(readfile("s/f2") == "f2")

        self.assertTrue(isdir("s/.parzzley.control"))
        deletedir("s/.parzzley.control")
        try:
            SYNC()
        except Exception:
            pass
        SYNC()
        self.assertTrue(readfile("m/d1/d2/f1") == "f1")
        self.assertTrue(readfile("m/f2") == "f2")
        self.assertTrue(readfile("s/d1/d2/f1") == "f1")
        self.assertTrue(readfile("s/f2") == "f2")

if __name__ == '__main__':
    unittest.main()
