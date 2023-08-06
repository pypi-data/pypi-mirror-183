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
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master" external_control_directory="${MYDIR}ctrl">
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="DefaultRemove"/>
        </fs>
        <aspect type="MySetMtimeGranularity"/>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
    <customaspect name="MySetMtimeGranularity">
import parzzley.syncengine.sync
class MySetMtimeGranularity(parzzley.aspect.abstractaspect.Aspect):
    def __init__(self):
        parzzley.aspect.abstractaspect.Aspect.__init__(self)
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def mysetmtimegranularity(self, ctx, filesystem):
        filesystem._is_mtime_precision_fine = True
    </customaspect>
</parzzleyconfig>
        """)

        createdir("m")
        createdir("_m")
        subprocess.call(["sudo", "-A", "mount", "--bind", "-o", "ro", mydir+"_m", mydir+"m"])
        try:
            isreadonly = False
            try:
                write2file("m/foo", "foo")
            except:
                isreadonly = True
            self.assertTrue(isreadonly)
            write2file("_m/f1", "x")
            write2file("_m/f2", "x")
            createdir("s")
            SYNC()
            self.assertTrue(readfile("s/f1") == "x")
            self.assertTrue(readfile("s/f2") == "x")
            deletefile("_m/f1")
            write2file("_m/f2", "y")
            write2file("_m/f3", "y")
            SYNC()
            self.assertTrue(not fileexists("s/f1"))
            self.assertTrue(readfile("s/f2") == "y")
            self.assertTrue(readfile("s/f3") == "y")
            self.assertTrue(fileexists("ctrl/README"))
        finally:
            subprocess.call(["sudo", "-A", "umount", mydir+"m"])


if __name__ == '__main__':
    unittest.main()
