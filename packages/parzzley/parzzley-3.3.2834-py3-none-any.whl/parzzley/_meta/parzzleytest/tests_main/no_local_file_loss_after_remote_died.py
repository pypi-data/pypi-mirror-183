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
            <aspect type="MetadataSynchronizationWithShadow"/>
        </fs>
        <fs type="SshfsFilesystem" path="${MYDIR}s" sshtarget="pino@localhost" idfile="${MYDIR}loginkey" name="slave"
            port="42921" timeout="4s"
            options_0="-o" options_1="StrictHostKeyChecking=no" options_2="-o" options_3="UserKnownHostsFile=/dev/null">
            <aspect type="TrashRemove"/>
            <aspect type="MetadataSynchronization"/>
            <aspect type="SleepWhileBeginning"/>
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
    <customaspect name="SleepWhileBeginning">
import random, subprocess, shutil, signal, random, threading, datetime
import parzzley.syncengine.sync
class SleepWhileBeginning(parzzley.aspect.abstractaspect.Aspect):
    def __init__(self):
        parzzley.aspect.abstractaspect.Aspect.__init__(self)
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_Prepare)
    def sleepwhilebeginupdatedir(self, ctx, filesystem):
        if ctx.path == "":
            if os.path.exists("/var/tmp/_parzzley_ctrl_die_in_beginning"):
                os.unlink("/var/tmp/_parzzley_ctrl_die_in_beginning")
                time.sleep(3)
    </customaspect>
</parzzleyconfig>
        """)

        with TemporarySshFs(mydir) as tempssh:
            os.makedirs(mydir + "s/.parzzley.control")

            try:
                os.unlink("/var/tmp/_parzzley_ctrl_die_in_beginning")
            except OSError:
                pass

            def wait_and_kill_connection():
                with open("/var/tmp/_parzzley_ctrl_die_in_beginning", "w"):
                    pass
                while os.path.exists("/var/tmp/_parzzley_ctrl_die_in_beginning"):
                    pass
                dis = Disturbator(0, tempssh, mydir)
                dis.d_killmounter()

            write2file("s/_dummy", "")
            write2file("m/a", "a")

            SYNC()

            write2file("m/b", "b")

            threading.Thread(target=wait_and_kill_connection).start()

            try:
                SYNC()
            except Exception:
                pass

            self.assertTrue(readfile("m/a") == "a")
            self.assertTrue(readfile("s/a") == "a")
            self.assertTrue(readfile("m/b") == "b")
            self.assertTrue(not fileexists("s/b"))

            SYNC()

            self.assertTrue(readfile("m/a") == "a")
            self.assertTrue(readfile("s/a") == "a")
            self.assertTrue(readfile("m/b") == "b")
            self.assertTrue(readfile("s/b") == "b")


if __name__ == '__main__':
    unittest.main()
