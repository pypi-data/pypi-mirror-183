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
        <preparation type="MountPreparation" src="${MYDIR}part" tgt="${MYDIR}m" options_0="-o" options_1="loop"/>
    </sync>
</parzzleyconfig>
        """)

        os.makedirs(mydir+"s")
        os.makedirs(mydir+"m")
        subprocess.call(["dd", "if=/dev/zero", "of="+mydir+"part", "bs=4096", "count=1000"])
        subprocess.call(["dd", "if=/dev/zero", "of="+mydir+"s/file", "bs=4096", "count=1250"])
        subprocess.call(["mkfs.ext3", "-F", mydir+"part"])
        subprocess.call(["sudo", "-A", "mount", "-o", "loop", mydir+"part", mydir+"m"])
        time.sleep(1)
        subprocess.call(["sudo", "-A", "chmod", "-R", "777", mydir+"m"])
        time.sleep(1)
        subprocess.call(["sudo", "-A", "umount", mydir+"m"])
        time.sleep(2)
        try:
            SYNC()
        except Exception:
            pass
        subprocess.call(["sudo", "-A", "mount", "-o", "loop", mydir+"part", mydir+"m"])
        try:
            self.assertTrue(fileexists("m/.parzzley.control/temp/_parzzley_currenttransfer.1"))
            self.assertTrue(readfile("m/file") == "")
            time.sleep(2)
            subprocess.call(["sudo", "-A", "umount", mydir+"m"])
            time.sleep(2)
            deletefile("s/file")
            try:
                SYNC()
            except Exception:
                pass
            subprocess.call(["sudo", "-A", "mount", "-o", "loop", mydir+"part", mydir+"m"])
            self.assertFalse(fileexists("m/.parzzley.control/temp/_parzzley_currenttransfer.1"))
            self.assertTrue(readfile("m/file") == "")
            write2file("s/file", "file")
            time.sleep(2)
            subprocess.call(["sudo", "-A", "umount", mydir+"m"])
            time.sleep(2)
            try:
                SYNC()
            except Exception:
                pass
            subprocess.call(["sudo", "-A", "mount", "-o", "loop", mydir+"part", mydir+"m"])
            self.assertTrue(readfile("m/file") == "file")
            time.sleep(2)
        finally:
            subprocess.call(["sudo", "-A", "umount", mydir+"m"])


if __name__ == '__main__':
    unittest.main()
