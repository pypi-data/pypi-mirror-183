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
            <aspect type="PullAndPurgeSyncSink"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="PullAndPurgeSyncSource"/>
        </fs>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("s/d1/d2/f1", "f1")
        write2file("s/d1/d2/f2", "f2")
        write2file("m/d1/f3", "f3")
        SYNC()
        self.assertTrue(readfile("m/d1/d2/f1") == "f1")
        self.assertTrue(readfile("m/d1/d2/f2") == "f2")
        self.assertTrue(readfile("m/d1/f3") == "f3")
        self.assertTrue(len(filesindir("s/")) == 0)
        write2file("s/d1/d2/f2", "f2b")
        write2file("s/d1/f4", "f4")
        write2file("m/d1/f5", "f5")
        SYNC()
        self.assertTrue(readfile("m/d1/d2/f1") == "f1")
        self.assertTrue(readfile("m/d1/d2/f2.1") == "f2")
        self.assertTrue(readfile("m/d1/f3") == "f3")
        self.assertTrue(readfile("m/d1/f4") == "f4")
        self.assertTrue(readfile("m/d1/f5") == "f5")
        self.assertTrue(readfile("m/d1/d2/f2") == "f2b")
        self.assertTrue(len(filesindir("s/")) == 0)


if __name__ == '__main__':
    unittest.main()
