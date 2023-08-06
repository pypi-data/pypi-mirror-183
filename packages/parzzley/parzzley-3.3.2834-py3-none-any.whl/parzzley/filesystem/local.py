# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import os
import shutil
import sys
import time

import parzzley.exceptions
import parzzley.filesystem.abstractfilesystem
import parzzley.syncengine.common

try:
    import xattr
except ImportError:
    xattr = None


class SyncLocalFilesystemError(parzzley.filesystem.abstractfilesystem.SyncFilesystemError):
    pass


class LocalFilesystem(parzzley.filesystem.abstractfilesystem.Filesystem):
    """
    A location in the local filesystem.
    """

    def __str__(self):
        return f"[local {self.rootpath}]"

    def __init__(self, *aspects, path, external_control_directory=None, **kwa):
        """
        :param external_control_directory: Absolute path to an external volume storage directory. Use it for read-only
                                           filesystems.
        """
        super().__init__(*aspects, **kwa)
        self.rootpath = path
        if isinstance(external_control_directory, str) and len(external_control_directory) > 0:
            self.control_directory = external_control_directory
        else:
            self.control_directory = "./.parzzley.control"
        self._initialize_populate_automatically = True
        self._is_mtime_precision_fine = None

    def listdir(self, path):
        fpath = self.getfulllocalpath(path)
        return os.listdir(fpath)

    def _gettemp(self):
        tempfs = self.get_control_filesystem("/temp")
        tpath = None
        i = 1
        while tpath is None or tempfs.exists(tpath):
            tpath = f"/_parzzley_currenttransfer.{i}"
            i += 1
        return tpath, tempfs

    def _translate_remote_time_to_local(self, rtime: datetime.datetime) -> datetime.datetime:
        if not hasattr(self, "_translate_remote_time_to_local__gap"):
            temprpath, tempfs = self._gettemp()
            tempfs.writetofile(temprpath, b"")
            nowlocal = datetime.datetime.now()
            nowremote = tempfs.getmtime(temprpath)
            self._translate_remote_time_to_local__gap = nowlocal - nowremote
        return rtime + self._translate_remote_time_to_local__gap

    def copyfile(self, srcpath, dstpath, verifier=lambda path, tempfile, mtime, size: True):
        parentfs = self.get_parent_filesystem()
        temprpath, tempfs = self._gettemp()
        pdstpath = self.translate_path(dstpath, parentfs)
        fdstpath = tempfs.getfulllocalpath(temprpath)
        ptemprpath = tempfs.translate_path(temprpath, parentfs)
        if (sys.platform == "win32") and os.path.exists(fdstpath):
            os.unlink(fdstpath)
        msize = os.stat(srcpath).st_size
        mt = os.stat(srcpath).st_mtime
        shutil.copyfile(srcpath, fdstpath)
        shutil.copystat(srcpath, fdstpath)
        newmsize = os.stat(srcpath).st_size
        newmt = os.stat(srcpath).st_mtime
        if mt == newmt and msize == newmsize:
            _mt = datetime.datetime.fromtimestamp(newmt)
            age = (datetime.datetime.now() - self._translate_remote_time_to_local(_mt)).total_seconds()
            if age > 2 or self.is_mtime_precision_fine():
                _msize = newmsize
                verified = verifier(srcpath, ptemprpath, _mt, _msize)
                if verified:
                    parentfs.move(ptemprpath, pdstpath)
                    return _mt, _msize
        return None, None

    def removefile(self, path):
        fpath = self.getfulllocalpath(path)
        os.unlink(fpath)

    def createdirs(self, path, recursive=True):
        parentfs = self.get_parent_filesystem()
        if parentfs != self:
            ppath = self.translate_path(path, parentfs)
            if ppath:
                return [parentfs.translate_path(x, self) for x in parentfs.createdirs(ppath, recursive=recursive)]
        spath = ""
        if sys.platform == "win32":
            path = path.replace("\\", "/")
        temprpath, tempfs = self._gettemp()
        ptemprpath = tempfs.translate_path(temprpath, parentfs)
        fdstpath = tempfs.getfulllocalpath(temprpath)
        parrpath = self.translate_path("", parentfs)
        createdpaths = []
        for segm in (path.split("/") if recursive else [path]):
            if segm != "":
                spath += f"/{segm}"
                if not self.exists(spath):
                    os.mkdir(fdstpath)
                    parentfs.move(ptemprpath, f"{parrpath}/{spath}")
                    createdpaths.append(spath)
        return createdpaths

    def removedir(self, path, recursive=False):
        fpath = self.getfulllocalpath(path)
        if recursive:
            shutil.rmtree(fpath)
        else:
            os.rmdir(fpath)

    def createlink(self, srcpath, dstpath):
        parentfs = self.get_parent_filesystem()
        temprpath, tempfs = self._gettemp()
        ptemprpath = tempfs.translate_path(temprpath, parentfs)
        pdstpath = self.translate_path(dstpath, parentfs)
        fdstpath = tempfs.getfulllocalpath(temprpath)
        os.symlink(srcpath, fdstpath)
        parentfs.move(ptemprpath, pdstpath)

    def removelink(self, path):
        fpath = self.getfulllocalpath(path)
        os.unlink(fpath)

    def move(self, path, dst):
        fpath = self.getfulllocalpath(path)
        fdst = self.getfulllocalpath(dst)
        if sys.platform == "win32" and os.path.exists(fdst):
            os.unlink(fdst)
        os.rename(fpath, fdst)

    def getftype(self, path):
        fpath = self.getfulllocalpath(path)
        if os.path.islink(fpath):
            return parzzley.syncengine.common.EntryType.Link
        elif os.path.isdir(fpath):
            return parzzley.syncengine.common.EntryType.Directory
        elif os.path.isfile(fpath):
            return parzzley.syncengine.common.EntryType.File
        else:
            return None

    def exists(self, path):
        fpath = self.getfulllocalpath(path)
        return os.path.exists(fpath) or os.path.islink(fpath)  # sic! -> for unresolved links

    def getsize(self, path):
        fpath = self.getfulllocalpath(path)
        return os.stat(fpath).st_size

    def getmtime(self, path):
        fpath = self.getfulllocalpath(path)
        mt = os.stat(fpath, follow_symlinks=False).st_mtime
        return datetime.datetime.fromtimestamp(mt)

    def getlinktarget(self, path):
        fpath = self.getfulllocalpath(path)
        return os.readlink(fpath)

    def getfulllocalpath(self, path):
        return os.path.abspath(f"{self.rootpath}/{path}")

    def _create_control_filesystem(self, path):
        if self.control_directory.startswith("./"):
            is_really_onvolume = True
            ipath = self.getfulllocalpath(self.control_directory[2:])
        else:
            is_really_onvolume = False
            ipath = self.control_directory
        return LocalFilesystem(path=f"{ipath}/{path}", name=None), is_really_onvolume

    def writetofile(self, path, content):
        with self.getoutputstream(path) as f:
            f.write(content)

    def readfromfile(self, path):
        with self.getinputstream(path) as f:
            return f.read()

    def getoutputstream(self, path):
        fpath = self.getfulllocalpath(path)
        return open(fpath, "wb")

    def getinputstream(self, path):
        fpath = self.getfulllocalpath(path)
        return open(fpath, "rb")

    def listxattrkeys(self, path):
        fpath = self.getfulllocalpath(path)
        res = xattr.list(fpath)
        return [x.decode("utf-8") for x in res]

    def getxattrvalue(self, path, key):
        fpath = self.getfulllocalpath(path)
        # noinspection PyUnresolvedReferences
        return xattr.get(fpath, key).decode("utf-8")

    def setxattrvalue(self, path, key, value):
        fpath = self.getfulllocalpath(path)
        xattr.set(fpath, key, value)

    def unsetxattrvalue(self, path, key):
        fpath = self.getfulllocalpath(path)
        xattr.remove(fpath, key)

    def initialize(self, sync, runtime):
        if not os.path.isdir(self.rootpath):
            raise SyncLocalFilesystemError(f"the path '{self.rootpath}' for '{self.name}' does not exist")
        super().initialize(sync, runtime)

    def initialize_late(self, sync, runtime):
        controlfs = self._create_control_filesystem("/")[0]
        fctrlpath = controlfs.getfulllocalpath("/")
        if not os.path.exists(fctrlpath):
            if self._initialize_populate_automatically:
                os.mkdir(fctrlpath)
            else:
                raise parzzley.filesystem.abstractfilesystem.SyncFilesystemError(
                    f"The filesystem {self.name} is not correctly mounted or is not prepared for synchronization. The"
                    f" directory '{controlfs.translate_path('', self) or controlfs.getfulllocalpath('')}' must exist.")
        tmpdir = f"{fctrlpath}/temp"
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)
        os.mkdir(tmpdir)
        for mtimesensori in range(1, 4):
            with open(f"{tmpdir}/mtime.sensor.{mtimesensori}", "w"):
                pass
            time.sleep(0.02 * mtimesensori)
        super().initialize_late(sync, runtime)

    def is_mtime_precision_fine(self):
        """
        Checks if the filesystem has fine (typically milliseconds) time granularity.
        |dooverride_optional|
        """
        result = self._is_mtime_precision_fine
        if result is None:
            controlfs = self.get_control_filesystem()
            if controlfs.is_really_onvolume:
                if self.getmtime("").microsecond != 0:
                    result = True
                if result is None and controlfs.getmtime("").microsecond != 0:
                    result = True
                if result is None:
                    tempfs = self.get_control_filesystem("/temp")
                    result = (tempfs.getmtime("").microsecond != 0) \
                        or (tempfs.getmtime("mtime.sensor.1").microsecond != 0) \
                        or (tempfs.getmtime("mtime.sensor.2").microsecond != 0) \
                        or (tempfs.getmtime("mtime.sensor.3").microsecond != 0)
            self._is_mtime_precision_fine = result
        if result is None:
            raise parzzley.exceptions.ParzzleyEngineExecutionError(f"Unable to determine mtime precision for '{self}'")
        return result
