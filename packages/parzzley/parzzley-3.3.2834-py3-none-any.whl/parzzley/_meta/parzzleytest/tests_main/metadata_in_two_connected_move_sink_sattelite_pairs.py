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
    <sync name="test1" interval="0s">
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master">
            <aspect type="PullAndPurgeSyncSink"/>
            <aspect type="MetadataSynchronizationWithShadow"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s1" name="slave1">
            <aspect type="PullAndPurgeSyncSource"/>
            <aspect type="MetadataSynchronization"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
    <sync name="test2" interval="0s">
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master">
            <aspect type="PullAndPurgeSyncSink"/>
            <aspect type="MetadataSynchronizationWithShadow"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s2" name="slave2">
            <aspect type="PullAndPurgeSyncSource"/>
            <aspect type="MetadataSynchronization"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("s1/d1/f1", "f1")
        write2file("s2/d1/f2", "f2")
        write2file("m/_dummy", "")
        metadata.setfilemetadata("s1/d1/f1", "foo", "1")
        SYNC()
        self.assertTrue(metadata.getfilemetadata("m/d1/f1", "foo") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/d1/f1", "foo") == "1")


if __name__ == '__main__':
    unittest.main()
