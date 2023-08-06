# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Some common helper functions for implementing tests.
"""


import os
import subprocess
import shutil
import sys
import time
sys.path.append(os.path.abspath(__file__+"/../../.."))
import parzzley.syncengine.core
import parzzley.runtime.returnvalue


_testfile = os.path.abspath(__file__)


def gettestfile():
    return _testfile


def gettestrootdir():
    return os.path.dirname(gettestfile())


def getmydir():  # must be within the homedir, otherwise sshd fails
    return gettestrootdir() + "/testing/"


def createdir(p):
    _p = mydir + p
    if not os.path.exists(_p):
        os.makedirs(_p)


def write2file(p, m):
    _p = mydir + p
    createdir(os.path.dirname(p))
    with open(_p, "wt") as ff:
        ff.write(m + "\n")


def readfile(p, readall=False):
    r = ""
    try:
        with open(mydir + p, "rt") as ff:
            if readall:
                r = "".join(ff.readlines())
            else:
                r = ff.readline()
    except Exception:
        pass
    return r.strip()


def readtrashedfile(p):
    si = p.index("/")
    return readfile(p[:si] + "/.parzzley.control/deleted_items" + p[si:])


def fileexiststrashed(p):
    si = p.index("/")
    return fileexists(p[:si] + "/.parzzley.control/deleted_items" + p[si:])


def link(s, d):
    try:
        if os.path.islink(mydir + d):
            os.remove(mydir + d)
    except OSError:
        pass
    os.symlink(s, mydir + d)


def islink(s):
    try:
        return os.readlink(mydir + s)
    except Exception:
        return None


def trashed(p, onlybool=False):
    r = ""
    try:
        ip = p.find("/")
        p1 = p[0:ip]
        p2 = p[ip + 1:]
        x = os.path.abspath(mydir + p1 + "/.parzzley.control/deleted_items/" + p2)
        if os.path.exists(x):
            if onlybool:
                return True
            with open(x, "rt") as ff:
                r += ff.readline()
    except Exception:
        pass
    if onlybool:
        return False
    return r.strip() if r != "" else None


def deletefile(p):
    try:
        os.remove(mydir + p)
    except OSError:
        pass


def deletedir(p):
    try:
        shutil.rmtree(mydir + p)
    except OSError as e:
        print(e)


def filesindir(p, _res=None):
    res = [] if _res is None else _res
    for x in os.listdir(mydir + p):
        if not x.startswith("."):
            if os.path.isfile(mydir + p + "/" + x):
                res.append(x)
            elif os.path.isdir(mydir + p + "/" + x):
                filesindir(p + "/" + x, res)
    return res


def listdir(p):
    try:
        return os.listdir(mydir + p)
    except OSError:
        return []


def isdir(p):
    return os.path.isdir(mydir + p)


def fileexists(p):
    return os.path.isfile(mydir + p)


def fileexistspattern(p):
    dr = os.path.dirname(mydir + p)
    fn = os.path.basename(p)
    for x in os.listdir(dr):
        if x.find(fn) != -1:
            return True
    return False


def exists(p):
    return os.path.exists(mydir + p)


def haslogentry(p, verb=None):
    with open(mydir + "log.txt", "rt") as ff:
        cont = ff.readlines()
    for ll in cont:
        if ll.find(p) > -1 and (verb is None or ll.find(verb) > -1):
            return True
    return False


def setconfig(cnt):
    with open(mydir + "cfg.xml", "w") as f:
        f.write(cnt)


do_sleep_in_SYNC = False


# noinspection PyPep8Naming
def SYNC(inprocess=True, repeat_when_dirty=False):
    global _comm_i
    if os.path.exists(mydir + "log.txt"):
        os.remove(mydir + "log.txt")
    if not os.path.exists(mydir + "datadir"):
        os.makedirs(mydir + "datadir")
    with open(mydir + "datadir/parzzley.xml", "w") as f:
        f.write("""<?xml version="1.0" ?>
<parzzleyconfig>
    <logger minseverity="debug" maxseverity="error">
        <out type="FilestreamLoggerout" filename="${MYDIR}log.txt" />
        <formatter type="PlaintextLogformat" />
    </logger>
    <logger minseverity="debug" maxseverity="debug">
        <out type="FilestreamLoggerout" />
        <formatter type="PlaintextLogformat" color="4"/>
    </logger>
    <logger minseverity="info" maxseverity="error">
        <out type="FilestreamLoggerout" />
        <formatter type="PlaintextLogformat" color="3"/>
    </logger>
    <include path="${MYDIR}/cfg.xml" />
</parzzleyconfig>
        """)
    cwd = os.getcwd()
    os.chdir(mydir)
    os.environ["MYDIR"] = mydir
    if do_sleep_in_SYNC:
        time.sleep(2.1)
    try:
        runsyncing = True
        while runsyncing:
            runsyncing = False
            cmdline = [f"{gettestrootdir()}/../../parzzley.py", "--sync", "ALL", "--datadir", f"{mydir}datadir",
                       "--configfile", f"{mydir}datadir/parzzley.xml"]
            if inprocess:
                retval = parzzley.syncengine.core.main(cmdline, callexit=False)
            else:
                current_sync_process = subprocess.Popen(cmdline)
                retval = current_sync_process.wait()
            if repeat_when_dirty:
                wasdirty = (retval & parzzley.runtime.returnvalue.ReturnValue.DIRTY) > 0
                if wasdirty:
                    retval -= parzzley.runtime.returnvalue.ReturnValue.DIRTY
                    runsyncing = True
            if retval != 0:
                raise Exception("error in Parzzley call (possibly wanted by the test)")
    finally:
        os.chdir(cwd)
        if os.path.isfile(mydir + "log.txt"):
            shutil.copy(mydir + "log.txt", mydir + "test.log.{0}.txt".format(_comm_i))
        _comm_i += 1


# noinspection PyPep8Naming
def RESET(removebefore=False):
    if removebefore and os.path.exists(mydir):
        shutil.rmtree(mydir)
    if not os.path.exists(mydir):
        os.mkdir(mydir)
    for x in os.listdir(mydir):
        fx = mydir + "/" + x
        if os.path.isdir(fx):
            shutil.rmtree(fx)

try:
    cols = int(subprocess.check_output(["tput", "cols"]))
except Exception:
    cols = 80

mydir = getmydir()
_comm_i = 1

