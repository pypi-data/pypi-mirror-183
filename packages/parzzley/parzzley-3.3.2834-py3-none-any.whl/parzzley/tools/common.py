# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Tools for very common jobs.
"""

import json
import os
import subprocess
import sys
import time
import typing as t


def call(*cmdline: t.Union[t.List[str], str], shell: bool = False, decode: bool = True,
         errorstring: t.Optional[t.AnyStr] = None) -> t.Union[t.AnyStr, t.Tuple[int, t.AnyStr]]:
    """
    Executes an external process and returns a tuple of returnvalue and program output.
    """
    ret = 0
    try:
        if len(cmdline) == 1:
            cmdline = cmdline[0]
        r = subprocess.check_output(cmdline, stderr=subprocess.STDOUT, shell=shell)
    except subprocess.CalledProcessError as err:
        ret = err.returncode
        r = err.output
    if ret != 0 and errorstring:
        raise Exception(errorstring + ": " + r.decode())
    rd = r.decode() if decode else r
    return rd if errorstring else (ret, rd)


def abspath(path: str) -> str:
    """
    A variant of os.path.abspath that does what it is used for in all operating systems.
    """
    if (sys.platform == "win32") and (len(path) > 1) and (path[1] != ":"):
        return os.path.abspath(path)[2:].replace("\\", "/")
    else:
        return os.path.abspath(path)


def lock(fle: str, *, pidless: bool = False, lockpid: t.Optional[int] = None) -> bool:
    """
    Locks a lockfile for synchronization.
    @parm pidless: If to return a lock not bound to a process. If yes, it must be unlocked and refreshed every 10 
                   minutes.
    @parm lockpid: The process id to lock with, if not the own one. This process should live over the entire timespan.
    """
    if os.path.isfile(fle):
        # check for old orphaned lock (but return if not orphaned)
        with open(fle, "r") as f:
            slockcrit = f.read()
        try:
            lockcrit = json.loads(slockcrit)
        except json.JSONDecodeError:
            lockcrit = {}  # just old garbage -> orphaned
        if "deadline" in lockcrit:
            if time.time() < lockcrit["deadline"]:
                return False
        elif "cmdline" in lockcrit:
            try:
                with open(f"/proc/{lockcrit['pid']}/cmdline", "rb") as f:
                    if f.read().decode(errors='ignore') == lockcrit["cmdline"]:
                        return False
            except OSError:
                pass
        try:
            os.unlink(fle)  # this is not perfect, since in theory this could be a new one meanwhile :-/
        except OSError:
            pass
    # make the new lock
    lockcrit = {}
    if sys.platform != "win32":
        if pidless:
            lockcrit["deadline"] = time.time() + 60 * 20
        else:
            if lockpid is None:
                lockpid = os.getpid()
            try:
                with open("/proc/" + str(lockpid) + "/cmdline", "rb") as f:
                    lockcrit["cmdline"] = f.read().decode(errors='ignore')
                lockcrit["pid"] = lockpid
            except OSError:
                pass
    if not lockcrit:
        lockcrit["deadline"] = time.time() + 60 * 60 * 24
    try:
        fd = os.open(fle, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
        os.write(fd, json.dumps(lockcrit).encode())
        os.close(fd)
        return True
    except OSError:
        return False


def unlock(fle: str) -> None:
    """
    Unlocks a lockfile.
    """
    os.remove(fle)
