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
        <aspect type="HighLevelCustomization"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("m/d1/d2/d3/INNER/y", "y")
        write2file("s/d1/d2/d3/INNER/x", "x")
        SYNC()
        write2file("m/d1/.parzzley.custom.py", """
def beforeupdate(filesystem, path, event):
    inner = filesystem.rootpath + event.scriptsource + "/d2/d3/INNER/"
    if path == "/d1/f2" and event.isnew:
        if event.ischanged or event.isdeleted:
            raise Exception("A")
        if filesystem.name != "master":
            raise Exception("B")
        with open(inner+"f2c", "w") as f: f.write("")
        event.runtime.mark_dirty()
    elif path == "/f1" and event.isnew:
        raise Exception("B")
    elif path == "/d1/d2/d3/f9" and event.ischanged:
        if event.isnew or event.isdeleted:
            raise Exception("A")
        if filesystem.name != "master":
            raise Exception("B")
        with open(inner+"f9c", "w") as f: f.write("")
        event.runtime.mark_dirty()
    elif path == "/d1/fcrash" and event.isnew:
        raise Exception("FCRASH")
    elif path == "/d1/ftouch" and event.ischanged:
        with open(filesystem.rootpath + path, "r") as f:
            cnt = f.read()
        with open(filesystem.rootpath + path, "w") as f:
            f.write(cnt.upper())
        event.continue_touched()
        return
    event.continue_untouched()
        """)

        write2file("m/d1/d2/.parzzley.custom.py", """
skiponerror = True
def beforeupdate(filesystem, path, event):
    inner = filesystem.rootpath + event.scriptsource + "/d3/INNER/"
    if path == "/d1/d2/f3" and event.ischanged:
        with open(inner+"f3c", "w") as f: f.write("")
        event.runtime.mark_dirty()
    if path == "/d1/d2/fcrash" and event.isnew:
        raise Exception("FCRASH")
    event.continue_untouched()
        """)

        write2file("m/d1/d2/d3/.parzzley.custom.py", """
def beforeupdate(filesystem, path, event):
    inner = filesystem.rootpath + event.scriptsource + "/INNER/"
    if path == "/d1/d2/d3/f4" and event.isdeleted:
        if event.ischanged or event.isnew:
            raise Exception("A")
        if filesystem.name != "slave":
            raise Exception("B")
        with open(inner+"f4c", "w") as f: f.write("")
        event.runtime.mark_dirty()
    event.continue_untouched()
        """)
        SYNC()

        write2file("m/f1", "f1")
        write2file("m/d1/f2", "f2")
        write2file("m/d1/d2/f3", "f3")
        write2file("m/d1/d2/d3/f4", "f4")
        SYNC(repeat_when_dirty=True)
        self.assertTrue(fileexists("m/d1/d2/d3/INNER/f2c"))
        self.assertTrue(fileexists("s/d1/d2/d3/INNER/f2c"))
        self.assertTrue(not fileexists("m/d1/d2/d3/INNER/f3c"))
        self.assertTrue(not fileexists("s/d1/d2/d3/INNER/f3c"))
        self.assertTrue(not fileexists("m/d1/d2/d3/INNER/f4c"))
        self.assertTrue(not fileexists("s/d1/d2/d3/INNER/f4c"))
        write2file("m/d1/d2/f3", "f3")
        SYNC(repeat_when_dirty=True)
        self.assertTrue(fileexists("m/d1/d2/d3/INNER/f3c"))
        self.assertTrue(fileexists("s/d1/d2/d3/INNER/f3c"))
        self.assertTrue(not fileexists("m/d1/d2/d3/INNER/f4c"))
        self.assertTrue(not fileexists("s/d1/d2/d3/INNER/f4c"))
        deletefile("s/d1/d2/d3/f4")
        write2file("m/d1/d2/d3/f9", "f9")
        SYNC(repeat_when_dirty=True)
        self.assertTrue(fileexists("m/d1/d2/d3/INNER/f4c"))
        self.assertTrue(fileexists("s/d1/d2/d3/INNER/f4c"))
        self.assertTrue(not fileexists("m/d1/d2/d3/INNER/f9c"))
        self.assertTrue(not fileexists("s/d1/d2/d3/INNER/f9c"))
        write2file("m/d1/d2/d3/f9", "f9")
        write2file("m/f1", "f1")
        write2file("m/c1", "c1")
        SYNC(repeat_when_dirty=True)
        self.assertTrue(fileexists("m/d1/d2/d3/INNER/f9c"))
        self.assertTrue(fileexists("s/d1/d2/d3/INNER/f9c"))
        write2file("m/d1/fcrash", "")
        iscrashed = False
        try:
            SYNC(repeat_when_dirty=True)
        except:
            iscrashed = True
        self.assertTrue(iscrashed)
        deletefile("m/d1/fcrash")
        write2file("m/d1/ftouch", "")
        SYNC(repeat_when_dirty=True)
        write2file("m/d1/d2/fcrash", "")
        SYNC(repeat_when_dirty=True)
        deletefile("m/d1/d2/fcrash")
        write2file("m/d1/ftouch", "foo")
        time.sleep(1.1)
        SYNC(repeat_when_dirty=True)
        self.assertTrue(readfile("m/d1/ftouch") == "FOO")
        self.assertTrue(readfile("s/d1/ftouch") == "FOO")
        write2file("m/d1/ftouch", "bar")
        time.sleep(1.1)
        SYNC(repeat_when_dirty=True)
        self.assertTrue(readfile("m/d1/ftouch") == "BAR")
        self.assertTrue(readfile("s/d1/ftouch") == "BAR")


if __name__ == '__main__':
    unittest.main()
