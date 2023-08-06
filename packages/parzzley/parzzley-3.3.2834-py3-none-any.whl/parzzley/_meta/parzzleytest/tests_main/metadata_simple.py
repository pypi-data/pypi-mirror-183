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
            <aspect type="TrashRemove"/>
            <aspect type="MetadataSynchronizationWithShadow"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="TrashRemove"/>
            <aspect type="MetadataSynchronization"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("m/d/dummy", "dummy")
        write2file("m/d2/dummy", "dummy")
        write2file("m/f1", "f1")
        write2file("m/f2", "f2")
        write2file("s/f3", "f3")
        write2file("s/f4", "f4")
        metadata.setfilemetadata("m/f1", "foo", "1")
        metadata.setfilemetadata("m/f2", "foo", "2")
        metadata.setfilemetadata("s/f3", "foo", "3")
        metadata.setfilemetadata("s/f4", "foo", "4")
        metadata.setfilemetadata("m/d", "foo", "d")
        metadata.setfilemetadata("m/d/dummy", "foo", "dummy")

        SYNC()

        self.assertTrue(metadata.getfilemetadata("m/f1", "foo") == "1")
        self.assertTrue(metadata.getfilemetadata("s/f1", "foo") == "1")
        self.assertTrue(metadata.getfilemetadata("m/f2", "foo") == "2")
        self.assertTrue(metadata.getfilemetadata("s/f2", "foo") == "2")
        self.assertTrue(metadata.getfilemetadata("m/f3", "foo") == "3")
        self.assertTrue(metadata.getfilemetadata("s/f3", "foo") == "3")
        self.assertTrue(metadata.getfilemetadata("m/f4", "foo") == "4")
        self.assertTrue(metadata.getfilemetadata("s/f4", "foo") == "4")
        self.assertTrue(metadata.getfilemetadata("m/d", "foo") == "d")
        self.assertTrue(metadata.getfilemetadata("s/d", "foo") == "d")
        self.assertTrue(metadata.getshadowmetadata("m/f1", "foo") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/f2", "foo") == "2")
        self.assertTrue(metadata.getshadowmetadata("m/f3", "foo") == "3")
        self.assertTrue(metadata.getshadowmetadata("m/f4", "foo") == "4")
        self.assertTrue(metadata.getshadowmetadata("m/d", "foo") == "d")
        self.assertTrue(metadata.getfilemetadata("m/f1", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/f1", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/f2", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/f2", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/f3", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/f3", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/f4", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/f4", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/d", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/d", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/f1", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/f2", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/f3", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/f4", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/d", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/d2", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d2", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("m/d2/dummy", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d2/dummy", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d2", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d2/dummy", "_version") is None)

        SYNC()

        self.assertTrue(metadata.getfilemetadata("m/d", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/d", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/d", "foo") == "d")
        self.assertTrue(metadata.getfilemetadata("s/d", "foo") == "d")
        self.assertTrue(metadata.getshadowmetadata("m/d", "foo") == "d")

        metadata.setfilemetadata("s/f1", "foo", "1A")
        metadata.setfilemetadata("s/f3", "foo", "3A")
        metadata.setfilemetadata("s/d", "foo", "dA")
        metadata.setshadowmetadata("m/f2", "foo", "2A")
        metadata.killshadowmetadata("m/f4")

        SYNC()

        self.assertTrue(metadata.getfilemetadata("m/f1", "foo") == "1A")
        self.assertTrue(metadata.getfilemetadata("s/f1", "foo") == "1A")
        self.assertTrue(metadata.getfilemetadata("m/f2", "foo") == "2A")
        self.assertTrue(metadata.getfilemetadata("s/f2", "foo") == "2A")
        self.assertTrue(metadata.getfilemetadata("m/f3", "foo") == "3A")
        self.assertTrue(metadata.getfilemetadata("s/f3", "foo") == "3A")
        self.assertTrue(metadata.getfilemetadata("m/f4", "foo") == "4")
        self.assertTrue(metadata.getfilemetadata("s/f4", "foo") == "4")
        self.assertTrue(metadata.getfilemetadata("m/d", "foo") == "dA")
        self.assertTrue(metadata.getfilemetadata("s/d", "foo") == "dA")
        self.assertTrue(metadata.getshadowmetadata("m/f1", "foo") == "1A")
        self.assertTrue(metadata.getshadowmetadata("m/f2", "foo") == "2A")
        self.assertTrue(metadata.getshadowmetadata("m/f3", "foo") == "3A")
        self.assertTrue(metadata.getshadowmetadata("m/f4", "foo") == "4")
        self.assertTrue(metadata.getshadowmetadata("m/d", "foo") == "dA")
        self.assertTrue(metadata.getfilemetadata("m/f1", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("s/f1", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("m/f2", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("s/f2", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("m/f3", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("s/f3", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("m/f4", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("s/f4", "_version") == "0")
        self.assertTrue(metadata.getfilemetadata("m/d", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("s/d", "_version") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/f1", "_version") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/f2", "_version") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/f3", "_version") == "1")
        self.assertTrue(metadata.getshadowmetadata("m/f4", "_version") == "0")
        self.assertTrue(metadata.getshadowmetadata("m/d", "_version") == "1")
        self.assertTrue(metadata.getfilemetadata("m/d2", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d2", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("m/d2/dummy", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d2/dummy", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d2", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d2/dummy", "_version") is None)

        deletedir("s/d")

        SYNC()

        self.assertTrue(metadata.getfilemetadata("m/d/dummy", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d/dummy", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d/dummy", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("m/d", "_version") is None)
        self.assertTrue(metadata.getfilemetadata("s/d", "_version") is None)
        self.assertTrue(metadata.getshadowmetadata("m/d", "_version", hint_isdir=True) is None)


if __name__ == '__main__':
    unittest.main()
