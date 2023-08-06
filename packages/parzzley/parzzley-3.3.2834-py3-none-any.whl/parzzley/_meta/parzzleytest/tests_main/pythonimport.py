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
        <fs type="MyFilesystem" path="${MYDIR}m" name="master">
            <aspect type="DefaultRemove"/>
        </fs>
        <fs type="MyFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="DefaultRemove"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="ApplyPathAcceptor" function="mypathacceptor"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
    <pythonimport importfrom="mymod.MyFilesystemImpl" to="MyFilesystem" />
    <pythonimport importfrom="mymod.mypathacceptorimpl" to="mypathacceptor" />
</parzzleyconfig>
        """)

        write2file("m/y", "y")
        write2file("s/x", "x")
        write2file("mymod.py", """
import parzzley.filesystem.local
class MyFilesystemImpl(parzzley.filesystem.local.LocalFilesystem):
    pass
def mypathacceptorimpl(path,fs):
    return True
        """)

        sys.path.append(mydir)
        SYNC()


if __name__ == '__main__':
    unittest.main()
