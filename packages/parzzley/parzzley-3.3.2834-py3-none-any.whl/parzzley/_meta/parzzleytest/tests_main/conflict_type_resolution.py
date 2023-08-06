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
        deletefile("s/x")
        link("x", "s/x")
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
        self.assertTrue(readfile("m/x") == "x")
        self.assertTrue(readfile("s/x") == "x")
        SYNC()

        # file > link
        deletefile("s/x")
        link("x", "s/x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "slave")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(islink("m/x") == "x")
        self.assertTrue(islink("s/x") == "x")
        SYNC()

        # link > dir
        deletefile("s/x")
        write2file("s/x/foo", "x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "slave")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x/foo") == "x")
        self.assertTrue(readfile("s/x/foo") == "x")

        # dir > link
        deletedir("m/x")
        link("x", "m/x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "master")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(islink("m/x") == "x")
        self.assertTrue(islink("s/x") == "x")
        SYNC()

        # link > file
        deletefile("m/x")
        write2file("m/x", "x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "master")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x") == "x")
        self.assertTrue(readfile("s/x") == "x")
        SYNC()

        # file > dir
        deletefile("s/x")
        write2file("s/x/foo", "x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "slave")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x/foo") == "x")
        self.assertTrue(readfile("s/x/foo") == "x")

        # dir > file
        deletedir("m/x")
        write2file("m/x", "x")
        SYNC()
        self.assertTrue(haslogentry("x", verb="conflict"))
        ll = readfile("m/.parzzley.control/conflicts/test/x", readall=True).split("\n")
        self.assertTrue(len(ll) == 2)
        write2file("m/.parzzley.control/conflicts/test/x", "master")
        SYNC()
        self.assertTrue(not fileexists("m/.parzzley.control/conflicts/test/x"))
        self.assertTrue(not fileexists("s/.parzzley.control/conflicts/test/x"))
        self.assertTrue(readfile("m/x") == "x")
        self.assertTrue(readfile("s/x") == "x")
        SYNC()


if __name__ == '__main__':
    unittest.main()
