# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Some helper functions over ssh filesystems.
"""


import random
import signal
import shutil
import subprocess
import threading
import time
import datetime
import os
import psutil
import parzzleytest.testhelper_common


def _iptables(cmd):
    try:
        subprocess.call(["sudo", "-A", "iptables"] + cmd.split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass
    try:
        subprocess.call(["sudo", "-A", "ip6tables"] + cmd.split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass


class RateLimiter:

    def __init__(self):
        pass

    def __enter__(self):
        self.__exit__(None, None, None)
        _iptables("-N PARZZLEYTEST11")
        _iptables("-I INPUT -i lo -p tcp --dport 42921 -j PARZZLEYTEST11")
        _iptables("-A PARZZLEYTEST11 -m limit --limit 5000/min -j ACCEPT")
        _iptables("-A PARZZLEYTEST11 -j DROP")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _iptables("-D INPUT -i lo -p tcp --dport 42921 -j PARZZLEYTEST11")
        _iptables("-F PARZZLEYTEST11")
        _iptables("-X PARZZLEYTEST11")


class TemporarySshFs:

    def __init__(self, mydir):
        self.mydir = mydir
        self.sshdpath = "/usr/sbin/sshd"
        self.sftpserverpath = "/usr/lib/sftp-server"
        self.exited = False
        parzzleytest.testhelper_common.do_sleep_in_SYNC = True

    def __enter__(self):
        if self.exited:
            return
        print("starting sshd")
        self.__exit__(-1, None, None)
        sshdconfig = """
            Port 42921
            AddressFamily any
            ListenAddress 0.0.0.0
            ListenAddress ::
            HostKey {MYDIR}/hostkey
            UsePrivilegeSeparation no
            AuthorizedKeysFile {MYDIR}/parzzley.authorizedkeys
            PermitEmptyPasswords yes
            UsePAM yes
            Compression no
            Subsystem	sftp	{SFTPSERVERPATH}
        """.format(MYDIR=self.mydir, SFTPSERVERPATH=self.sftpserverpath)
        if not os.path.exists(self.mydir + "/sshdconfig"):
            with open(self.mydir + "/sshdconfig", "w") as f:
                f.write(sshdconfig)
            subprocess.call(["ssh-keygen", "-t", "rsa", "-f", self.mydir + "/hostkey", "-N", ""])
            subprocess.call(["ssh-keygen", "-t", "rsa", "-N", "", "-f", self.mydir + "/loginkey"])
            shutil.copy(self.mydir + "/loginkey.pub", self.mydir + "/parzzley.authorizedkeys")
        subprocess.call([self.sshdpath, "-f", self.mydir + "/sshdconfig"])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != -1:
            print("killing sshd")
        if exc_type != -1 and exc_type != -2:
            self.exited = True
        for pid in psutil.pids():
            try:
                for conn in psutil.Process(pid).connections():
                    try:
                        laddr = conn.laddr
                    except AttributeError:
                        laddr = None
                    if laddr:
                        if laddr[1] == 42921:
                            try:
                                subprocess.check_output(["sudo", "-A", "kill", "-9", str(pid)])
                            except subprocess.CalledProcessError:
                                pass
            except psutil.AccessDenied:
                pass
            except Exception as e:
                print(str(e))


class Disturbator:
    def __init__(self, conn_oh, tempssh, mydir, disturbinterval=16):
        self.conn_oh = conn_oh
        self.mydir = mydir
        self.starttime = None
        self.terminated = False
        self.on = False
        self.tempssh = tempssh
        self.t = None
        self.disturbinterval = disturbinterval

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.terminate()

    def d_iptables(self):
        m = random.choice(["REJECT", "DROP"])
        _iptables("-I PARZZLEYTEST11 -p tcp --dport 42921 -j " + m)
        time.sleep(random.randrange(self.disturbinterval) + 3)
        _iptables("-D PARZZLEYTEST11 -p tcp --dport 42921 -j " + m)

    def d_killmounter(self):
        pidnames = {}
        for pid in psutil.pids():
            try:
                with open("/proc/" + str(pid) + "/cmdline", "r") as f:
                    pidname = f.readline()
                pidnames[pid] = pidname
            except OSError:
                pass
        for pid in pidnames:
            n = pidnames[pid]
            if n.find("42921") > -1 and n.find("ftp") > -1:
                os.kill(pid, signal.SIGTERM)
                print("Terminate pid " + str(pid))

    def d_killserver(self):
        self.tempssh.__exit__(-2, None, None)
        time.sleep(random.randrange(self.disturbinterval) + 3)
        self.tempssh.__enter__()

    def disturb(self):
        try:
            random.choice([self.d_iptables, self.d_killmounter, self.d_killserver])()
        except Exception as e:
            print(e)

    def thread(self):
        while not self.terminated:
            while (not self.terminated) and (not self.on):
                time.sleep(0.1)
            dur = (1 + random.randrange(2)) * self.conn_oh * 0.8 + random.randrange(self.disturbinterval)
            for w in range(int(dur)):
                time.sleep(1)
                if self.terminated:
                    return
            print("begin disturbing process")
            self.disturb()
            print("stop disturbing process")

    def start(self):
        self.on = True
        self.t = threading.Thread(target=self.thread, args=())
        self.t.start()

    def terminate(self):
        self.terminated = True


def measure_network():
    os.mkdir(parzzleytest.testhelper_common.getmydir() + "_s")
    curr = 13000.0
    dur = None
    print("determining a good filesize for 10 seconds transfer time")
    print("determining connection overhead")
    mins = 1000000
    maxs = 0
    parzzleytest.testhelper_common.write2file("s/_dummym", "")
    parzzleytest.testhelper_common.write2file("m/_dummys", "")
    parzzleytest.testhelper_common.SYNC()
    for i in range(3):
        t1 = datetime.datetime.now()
        parzzleytest.testhelper_common.SYNC()
        t2 = datetime.datetime.now()
        _dur = (t2 - t1).total_seconds()
        if _dur < mins:
            mins = _dur
        if _dur > maxs:
            maxs = _dur
    parzzleytest.testhelper_common.RESET()
    os.makedirs(parzzleytest.testhelper_common.mydir + "s/.parzzley.control")
    if maxs - mins > 2:
        print("WARNING: sloppy system!")
    ohdur = (maxs + mins) * 0.5
    for10secs = None
    print("overhead duration: " + str(ohdur) + "s (deviation: " + str(maxs - mins) + ")")
    while (dur is None) or not (9.0 < dur < 13.0):
        if not os.path.exists(parzzleytest.testhelper_common.getmydir() + "m"):
            os.mkdir(parzzleytest.testhelper_common.getmydir() + "m")
        with open(parzzleytest.testhelper_common.getmydir() + "m/b", "w") as f:
            l = "1" * 1024
            for i in range(int(curr)):
                f.write(l)
        parzzleytest.testhelper_common.write2file("s/_dummy", "")
        if curr >= 0.6 * 1024 * 1024 * 1024:
            scurr = str(curr / (1024.0 * 1024 * 1024)) + "TB"
        elif curr >= 0.6 * 1024 * 1024:
            scurr = str(curr / (1024.0 * 1024)) + "GB"
        elif curr >= 0.6 * 1024:
            scurr = str(curr / 1024.0) + "MB"
        else:
            scurr = str(curr) + "KB"
        print("testing with " + scurr)
        t1 = datetime.datetime.now()
        parzzleytest.testhelper_common.SYNC()
        t2 = datetime.datetime.now()
        dur = max((t2 - t1).total_seconds() - ohdur, 0.2)
        print("we took " + str(dur) + " seconds")
        for10secs = int(curr)
        curr *= (11.0 / dur)
        parzzleytest.testhelper_common.RESET()
        os.makedirs(parzzleytest.testhelper_common.mydir + "s/.parzzley.control")
    print("use the last value")
    if curr > 1024 * 25:
        print("WARNING: the rate limiter does not seem to work; huge data amounts can occur!")
    return for10secs, ohdur
