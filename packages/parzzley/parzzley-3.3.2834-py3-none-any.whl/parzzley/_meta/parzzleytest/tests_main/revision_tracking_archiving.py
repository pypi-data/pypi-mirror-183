#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys
sys.path.append(os.path.abspath(__file__+"/../../.."))
from parzzleytest.test import *

import tarfile


class Test(unittest.TestCase):

    def test_main(self):

        setconfig("""<?xml version="1.0" ?>
<parzzleyconfig>
    <sync name="test" interval="0s">
        <fs type="LocalFilesystem" path="${MYDIR}m" name="master">
            <aspect type="DefaultRemove"/>
            <aspect type="RevisionTracking" number_unarchived_revisions="3" number_revisions_per_archive="4"/>
        </fs>
        <fs type="LocalFilesystem" path="${MYDIR}s" name="slave">
            <aspect type="TrashRemove"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        write2file("s/_dummys", "")  # otherwise the other dir gets empty which is a bad thing for the watchdog
        write2file("m/_dummym", "")  # otherwise the other dir gets empty which is a bad thing for the watchdog
        SYNC()
        for i in range(20):
            write2file("m/a", str(i))
            SYNC()

        revdir = "/m/.parzzley.control/content_revisions/a/"
        revfiles = sorted(os.listdir(getmydir() + revdir))
        directrevfiles = revfiles[-3:]
        lastarchive = revfiles[-4]
        archives = revfiles[:-3]
        i = 0
        for archive in archives:
            with tarfile.open(getmydir() + revdir + archive, "r:bz2") as tf:
                lsm = sorted(tf.getnames())
                if archive != lastarchive:
                    self.assertEqual(len(lsm), 4)
                for sm in lsm:
                    with tf.extractfile(sm) as f:
                        c = f.read()
                    self.assertEqual(i, int(c))
                    i += 1
        for directrevfile in directrevfiles:
            c = readfile(revdir+directrevfile)
            self.assertEqual(i, int(c))
            i += 1
        self.assertEqual(i, 20)


if __name__ == '__main__':
    unittest.main()
