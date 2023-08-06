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
            <aspect type="MetadataSynchronizationWithShadow"/>
        </fs>
        <fs type="SshfsFilesystem" path="${MYDIR}s" sshtarget="pino@localhost" idfile="${MYDIR}loginkey" name="slave"
            port="42921"
            options_0="-o" options_1="StrictHostKeyChecking=no" options_2="-o" options_3="UserKnownHostsFile=/dev/null">
            <aspect type="PullAndPurgeSyncSource"/>
            <aspect type="MetadataSynchronization"/>
        </fs>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        with TemporarySshFs(mydir):
            os.makedirs(mydir + "s/.parzzley.control")

            write2file("s/d1/d2/f1", "f1")
            write2file("s/d1/f2", "f2")
            write2file("m/_dummy", "")
            metadata.setfilemetadata("s/d1/d2/f1", "foo", "1")
            SYNC()

            metadata.setfilemetadata("m/d1/f2", "foo", "2")
            SYNC()

            self.assertTrue(metadata.getfilemetadata("m/d1/d2/f1", "foo") == "1")
            self.assertTrue(metadata.getfilemetadata("m/d1/f2", "foo") == "2")
            self.assertTrue(metadata.getshadowmetadata("m/d1/d2/f1", "foo") == "1")
            self.assertTrue(metadata.getshadowmetadata("m/d1/f2", "foo") == "2")

            metadata.setshadowmetadata("m/d1/f2", "foo", "22")
            metadata.killshadowmetadata("m/d1/d2/f1")

            SYNC()

            self.assertTrue(metadata.getfilemetadata("m/d1/f2", "foo") == "22")
            self.assertTrue(metadata.getshadowmetadata("m/d1/f2", "foo") == "22")
            self.assertTrue(metadata.getfilemetadata("m/d1/d2/f1", "foo") == "1")
            self.assertTrue(metadata.getshadowmetadata("m/d1/d2/f1", "foo") == "1")


if __name__ == '__main__':
    unittest.main()
