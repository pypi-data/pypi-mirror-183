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
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="DefaultRemove"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("m/d1/d2/d3/d4/d5/f1", "f1")
        write2file("s/e1/e2/e3/e4/e5/f2", "f2")
        SYNC()
        time.sleep(1)
        self.assertTrue(readfile("s/d1/d2/d3/d4/d5/f1") == "f1")
        self.assertTrue(readfile("m/e1/e2/e3/e4/e5/f2") == "f2")
        write2file("s/d1/d2/f3", "f3")
        write2file("m/e1/e2/f4", "f4")
        deletefile("s/d1/d2/d3/d4/d5/f1")
        deletefile("s/e1/e2/e3/e4/e5/f2")
        deletedir("s/d1/d2/d3/d4/d5/")
        deletedir("s/d1/d2/d3/d4")
        deletedir("s/d1/d2/d3")
        deletedir("s/e1/e2/e3/e4/e5/")
        deletedir("s/e1/e2/e3/e4/")
        deletedir("s/e1/e2/e3/")
        deletedir("s/e1/e2/")
        deletedir("s/e1/")
        SYNC()
        self.assertTrue(not isdir("m/d1/d2/d3/"))
        self.assertTrue(not isdir("m/e1/e2/e3/"))
        self.assertTrue(readfile("m/e1/e2/f4") == "f4")
        self.assertTrue(readfile("m/d1/d2/f3") == "f3")
        self.assertTrue(readfile("s/e1/e2/f4") == "f4")
        self.assertTrue(readfile("s/d1/d2/f3") == "f3")


if __name__ == '__main__':
    unittest.main()
