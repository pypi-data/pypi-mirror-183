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
        write2file("m/x", "x")
        SYNC()
        time.sleep(1.1)
        write2file("m/x", "x1")
        time.sleep(1.1)
        write2file("s/x", "x2")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))

        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        self.assertTrue(ll[0] in ["master", "slave"])
        self.assertTrue(ll[1] in ["master", "slave"])
        write2file("m/.parzzley.control/conflicts/test/x", "master")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x") == "x1")
        self.assertTrue(readfile("s/x") == "x1")
        SYNC()

        time.sleep(1.1)
        write2file("m/x", "x1")
        time.sleep(1.1)
        write2file("s/x", "x2")
        SYNC()
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "slave")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x") == "x2")
        self.assertTrue(readfile("s/x") == "x2")


if __name__ == '__main__':
    unittest.main()
