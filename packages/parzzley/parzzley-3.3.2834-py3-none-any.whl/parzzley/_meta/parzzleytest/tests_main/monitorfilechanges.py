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
    <sync name="test" interval="9999s">
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master">
            <aspect type="TrashRemove"/>
        </fs>
        <fs type="SshfsFilesystem" path="${MYDIR}s" sshtarget="pino@localhost" idfile="${MYDIR}loginkey" name="slave"
            port="42921"
            options_0="-o" options_1="StrictHostKeyChecking=no" options_2="-o" options_3="UserKnownHostsFile=/dev/null">
            <aspect type="TrashRemove"/>
            <aspect type="MonitorFileChanges"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        with TemporarySshFs(mydir):
            os.makedirs(mydir + "s/.parzzley.control")
            write2file("m/f1", "f1")
            SYNC()
            time.sleep(10)
            self.assertTrue(readfile("m/f1") == "f1")
            self.assertTrue(readfile("s/f1") == "f1")
            for s in ["f2", "f3", "f4"]:
                time.sleep(3)
                write2file("s/f1", s)
                updated = False
                for xxx in range(3):
                    updated = readfile("m/f1") == s and readfile("s/f1") == s
                    if updated:
                        break
                    time.sleep(3)
                    SYNC()
                self.assertTrue(updated, s)


if __name__ == '__main__':
    unittest.main()
