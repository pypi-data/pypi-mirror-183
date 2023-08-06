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
        </fs>
        <aspect type="DefaultSync"/>
        <aspect type="Logging" logupdate="1" logcreate="1" logremove="1" />
    </sync>
</parzzleyconfig>
        """)

        runs = 2

        class State:

            def __init__(self):
                self.files = {}
                self.dump = "|DUMP:"

            def populatemachine(self, _lm, length):
                flat = random.choice([True, False])
                for fi in range(20):
                    b = "" if flat else random.choice([
                        "", "w/", "w/x/", "w/x/y/", "w/x/y/z/"
                    ])
                    # noinspection PyUnusedLocal
                    content = "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for x in range(10)])
                    number = int(length * 4)
                    fnm = b + "f" + _lm + str(fi)
                    self.files[fnm] = (content, )
                    self.dump += "create '" + content + " in " + fnm + ";"
                    write2file(_lm + "/" + fnm, "x" * number)
                    metadata.setfilemetadata(_lm + "/" + fnm, "foo", content)

            def updatemachine(self, length):
                upd = []
                for fi in range(20):
                    remove = random.choice([True, False]) if (len(self.files.keys()) > 20) else False
                    mach = random.choice(["m", "s"])
                    tok = None
                    fulltok = None
                    while tok is None:
                        tok = random.choice(list(self.files.keys()))
                        fulltok = mydir + mach + "/" + tok
                        if tok in upd:
                            tok = None
                        elif not os.path.exists(fulltok):
                            tok = None
                            break
                    if tok is None:
                        continue
                    if remove:
                        os.remove(fulltok)
                        self.files[tok] = (None, )
                        self.dump += "deleted " + tok + ";"
                    else:
                        rewrite = random.choice([True, False])
                        if rewrite:
                            number = int(length * 4)
                            write2file(mach + "/" + tok, "x" * number)
                            self.dump += "rewrite " + tok + ";"
                        else:
                            content = "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)])
                            self.files[tok] = (content, )
                            self.dump += "update '" + content + "' in " + tok + ";"
                            metadata.setfilemetadata(mach + "/" + tok, "foo", content)
                    upd += [tok]

            def checkmachine(self, _lm):
                for f in self.files:
                    (c,) = self.files[f]
                    dfn = _lm + "/" + f
                    if c is None:
                        if os.path.exists(mydir + dfn):
                            self.dump += "was not deleted: " + dfn + ";"
                            return False
                    else:
                        fc = metadata.getfilemetadata(dfn, "foo")
                        if fc != c:
                            self.dump += "got " + dfn + ":" + (fc or "None") + ";"
                            return False
                return True

        with TemporarySshFs(mydir) as tempssh:
            os.makedirs(mydir + "s/.parzzley.control")
            with RateLimiter():
                (for10secs, conn_oh) = measure_network()
                with Disturbator(conn_oh, tempssh, mydir):
                    for ir in range(runs):
                        state = State()
                        for lm in ["m", "s"]:
                            state.populatemachine(lm, for10secs)
                        for iir in range(3):
                            print("begin pass "+str(iir))
                            succ = False
                            if iir > 0:
                                state.updatemachine(for10secs)
                            while not succ:
                                try:
                                    SYNC(inprocess=False)
                                    succ = True
                                except Exception as e:
                                    print(e)
                            good = state.checkmachine("m") and state.checkmachine("s")
                            if not good:
                                self.assertTrue(False, msg=str(ir + 1) + " failed; " + state.dump)
                        RESET()
                        os.makedirs(mydir + "s/.parzzley.control")


if __name__ == '__main__':
    unittest.main()
