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

        write2file("s/d1/f1", "f1")
        write2file("m/d1/f2", "f2")
        write2file("s/d1/f3", "f3")
        link("d1/f1", "s/l1")
        link("d1/f2", "s/l2")
        link("d1/f3", "m/l3")
        link("d1/f4", "s/l4")
        link("l3", "s/l5")
        link("d1", "m/ll1")
        link("d1", "m/ll2")
        link("d1/f2", "m/ll3")
        link("d1/f1", "s/ll3")
        link("d1", "m/ll4")
        SYNC()
        self.assertTrue(readfile("m/d1/f1") == "f1")
        self.assertTrue(readfile("m/l1") == "f1")
        self.assertTrue(islink("m/l1") == "d1/f1")
        self.assertTrue(readfile("m/d1/f2") == "f2")
        self.assertTrue(readfile("m/l2") == "f2")
        self.assertTrue(islink("m/l2") == "d1/f2")
        self.assertTrue(readfile("m/d1/f3") == "f3")
        self.assertTrue(readfile("m/l3") == "f3")
        self.assertTrue(islink("m/l3") == "d1/f3")
        self.assertTrue(readfile("s/d1/f1") == "f1")
        self.assertTrue(readfile("s/l1") == "f1")
        self.assertTrue(islink("s/l1") == "d1/f1")
        self.assertTrue(readfile("s/d1/f2") == "f2")
        self.assertTrue(readfile("s/l2") == "f2")
        self.assertTrue(islink("s/l2") == "d1/f2")
        self.assertTrue(readfile("s/d1/f3") == "f3")
        self.assertTrue(readfile("s/l3") == "f3")
        self.assertTrue(islink("s/l3") == "d1/f3")
        self.assertTrue(islink("m/l5") == "l3")
        self.assertTrue(islink("s/l5") == "l3")
        self.assertTrue(haslogentry("ll3", verb="conflict"))
        self.assertTrue(islink("m/ll3") == "d1/f2")
        self.assertTrue(islink("s/ll3") == "d1/f1")
        self.assertTrue(islink("s/ll1") == "d1")
        self.assertTrue(islink("m/ll1") == "d1")
        deletefile("s/l1")
        deletefile("s/l2")
        deletefile("s/ll1")
        link("d1/f1", "m/ll1")
        link("d1/f1", "m/ll2")
        link("d1/f2", "m/ll4")
        link("d1/f1", "s/ll4")
        write2file("s/l2", "l2")
        SYNC()
        self.assertTrue(readfile("m/d1/f3") == "f3")
        self.assertTrue(readfile("m/l3") == "f3")
        self.assertTrue(islink("m/l3") == "d1/f3")
        self.assertTrue(readfile("s/d1/f3") == "f3")
        self.assertTrue(readfile("s/l3") == "f3")
        self.assertTrue(islink("s/l3") == "d1/f3")
        self.assertTrue(not exists("m/l1"))
        self.assertTrue(not exists("s/l1"))
        self.assertTrue(haslogentry("l2", verb="conflict"))
        self.assertTrue(readfile("s/l2") == "l2")
        self.assertTrue(islink("m/l2") == "d1/f2")
        self.assertTrue(islink("s/ll1") == "d1/f1")
        self.assertTrue(islink("m/ll1") == "d1/f1")
        self.assertTrue(islink("m/ll1") == "d1/f1")
        self.assertTrue(islink("m/ll2") == "d1/f1")
        self.assertTrue(islink("s/ll2") == "d1/f1")
        self.assertTrue(haslogentry("ll4", verb="conflict"))
        self.assertTrue(islink("m/ll4") == "d1/f2")
        self.assertTrue(islink("s/ll4") == "d1/f1")


if __name__ == '__main__':
    unittest.main()
