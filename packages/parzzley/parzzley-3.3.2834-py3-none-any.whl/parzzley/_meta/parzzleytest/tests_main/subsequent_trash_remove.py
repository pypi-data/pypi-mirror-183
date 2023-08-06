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

        write2file("m/_dummy1", "")
        write2file("s/_dummy2", "")
        write2file("m/file", "X")
        SYNC()
        self.assertTrue(readfile("m/file") == "X")
        self.assertTrue(readfile("s/file") == "X")
        deletefile("m/file")
        SYNC()
        self.assertTrue(readtrashedfile("s/file") == "X")
        time.sleep(11)
        SYNC()
        self.assertTrue((not fileexiststrashed("m/file")) and (not fileexiststrashed("m/file..0"))
                        and (not fileexists("m/file")))
        self.assertTrue((not fileexiststrashed("s/file")) and (not fileexiststrashed("s/file..0"))
                        and (not fileexists("s/file")))
        write2file("m/file", "Y")
        SYNC()
        self.assertTrue(readfile("m/file") == "Y")
        self.assertTrue(readfile("s/file") == "Y")
        deletefile("m/file")
        SYNC()
        self.assertTrue(readtrashedfile("s/file") == "Y")
        time.sleep(11)
        SYNC()
        self.assertTrue((not fileexiststrashed("m/file")) and (not fileexiststrashed("m/file..0"))
                        and (not fileexists("m/file")))
        self.assertTrue((not fileexiststrashed("s/file")) and (not fileexiststrashed("s/file..0"))
                        and (not fileexists("s/file")))
        write2file("m/file", "Z")
        SYNC()
        self.assertTrue(readfile("m/file") == "Z")
        self.assertTrue(readfile("s/file") == "Z")
        deletefile("m/file")
        SYNC()
        write2file("m/file", "ZZ")
        SYNC()
        deletefile("m/file")
        SYNC()
        self.assertTrue(readtrashedfile("s/file") + readtrashedfile("s/file..0") == "ZZZ")
        time.sleep(11)
        SYNC()
        self.assertTrue((not fileexiststrashed("m/file")) and (not fileexiststrashed("m/file..0"))
                        and (not fileexists("m/file")))
        self.assertTrue((not fileexiststrashed("s/file")) and (not fileexiststrashed("s/file..0"))
                        and (not fileexists("s/file")))


if __name__ == '__main__':
    unittest.main()
