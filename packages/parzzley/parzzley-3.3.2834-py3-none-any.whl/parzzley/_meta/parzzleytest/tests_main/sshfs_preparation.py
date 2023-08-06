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
            <aspect type="TrashRemove" />
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}_s" name="slave">
            <aspect type="TrashRemove" />
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
        <preparation type="SshfsMountPreparation" src="pino@localhost:${MYDIR}s" tgt="${MYDIR}_s"
            idfile="${MYDIR}loginkey" port="42921"
            options_0="-o" options_1="StrictHostKeyChecking=no" options_2="-o" 
            options_3="UserKnownHostsFile=/dev/null"/>
    </sync>
</parzzleyconfig>
        """)

        with TemporarySshFs(mydir):
            os.mkdir(mydir + "_s")

            write2file("m/d1/d2/f1", "f1")
            write2file("m/d1/d2/f2", "f2")
            write2file("m/d1/f3", "f3")
            write2file("s/d5/d7/f4", "f4")
            write2file("s/d5/d6/f5", "f5")
            write2file("s/d1/d2/f6", "f6")

            SYNC()

            self.assertTrue(readfile("m/d1/d2/f2") == "f2")
            self.assertTrue(readfile("m/d1/d2/f2") == "f2")
            self.assertTrue(readfile("m/d1/f3") == "f3")
            self.assertTrue(readfile("s/d1/d2/f1") == "f1")
            self.assertTrue(readfile("s/d1/d2/f2") == "f2")
            self.assertTrue(readfile("s/d1/f3") == "f3")
            self.assertTrue(readfile("m/d5/d7/f4") == "f4")
            self.assertTrue(readfile("m/d5/d6/f5") == "f5")
            self.assertTrue(readfile("m/d1/d2/f6") == "f6")
            self.assertTrue(readfile("s/d5/d7/f4") == "f4")
            self.assertTrue(readfile("s/d5/d6/f5") == "f5")
            self.assertTrue(readfile("s/d1/d2/f6") == "f6")


if __name__ == '__main__':
    unittest.main()
