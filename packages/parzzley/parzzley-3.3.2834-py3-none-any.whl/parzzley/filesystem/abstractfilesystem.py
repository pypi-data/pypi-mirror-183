# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Abstract base class for filesystem implementations.
"""

import datetime
import typing as t

import parzzley.config.configpiece
import parzzley.exceptions
import parzzley.tools.common

if t.TYPE_CHECKING:
    import parzzley.aspect.abstractaspect
    import parzzley.runtime.runtime
    import parzzley.syncengine.sync


class SyncFilesystemError(parzzley.exceptions.ParzzleyError):
    pass


class Filesystem:
    """
    Base class for a filesystem implementation. 
    
    It's an abstraction layer for all filesystem operations like 'create file' or 'remove x'. 
    See parzzley.filesystem for existing implementations.
    """

    def __init__(self, *aspects: parzzley.aspect.abstractaspect.Aspect, name: str, checkaliveskeptically: str = "0"):
        self.aspects = aspects
        self.name = name
        self.checkaliveskeptically = parzzley.config.configpiece.getbool(checkaliveskeptically)
        self._controlfs = None
        self._controlfs_isreallyonvolume = None
        self._iscontrolfs = False
        self._parentfs = None
        self._is_hot = False

    def listdir(self, path: str) -> t.List[str]:
        """
        Returns a list of the names of all items in the given location.
        |dooverride|
        """
        raise NotImplementedError()

    def copyfile(self, srcpath: str, dstpath: str,
                 verifier=lambda path, tempfile, mtime, size: True) -> t.Tuple[datetime.datetime, int]:
        """
        Copies a file from the local filesystem to a destination.
        |dooverride|
        """
        raise NotImplementedError()

    def removefile(self, path: str) -> None:
        """
        Removes a file.
        |dooverride|
        """
        raise NotImplementedError()

    def createdirs(self, path: str, recursive: bool = True) -> t.List[str]:
        """
        Creates a directory (or a chain of directories).
        |dooverride|
        """
        raise NotImplementedError()

    def removedir(self, path: str, recursive: bool = False) -> None:
        """
        Removes a directory.
        |dooverride|
        """
        raise NotImplementedError()

    def createlink(self, srcpath: str, dstpath: str) -> None:
        """
        Creates a link.
        |dooverride|
        """
        raise NotImplementedError()

    def removelink(self, path: str) -> None:
        """
        Removes a link.
        |dooverride|
        """
        raise NotImplementedError()

    def move(self, path: str, dst: str) -> None:
        """
        Moves an item.
        |dooverride|
        """
        raise NotImplementedError()

    def getftype(self, path: str) -> t.Optional[str]:
        """
        Returns the parzzley.syncengine.common.EntryType item type of an item.
        |dooverride|
        """
        raise NotImplementedError()

    def exists(self, path: str) -> bool:
        """
        Returns if an item at a given location exists.
        |dooverride|
        """
        raise NotImplementedError()

    def getsize(self, path: str) -> int:
        """
        Returns the file size of a file.
        |dooverride|
        """
        raise NotImplementedError()

    def getmtime(self, path: str) -> datetime.datetime:
        """
        Returns the time of last modification of a file.
        |dooverride|
        """
        raise NotImplementedError()

    def getlinktarget(self, path: str) -> str:
        """
        Returns the link target of a link.
        |dooverride|
        """
        raise NotImplementedError()

    # noinspection PyUnusedLocal
    def getfulllocalpath(self, path: str) -> t.Optional[str]:
        """
        Returns the local filesystem path of a file.
        Returns `None` if there is representation in the local filesystem.
        |dooverride_optional|
        @note Returning `None` or not implementing it will probably restrict the things Parzzley can do.
        """
        return None

    def getfulllocalpathorfallback(self, path: str) -> str:
        """
        Returns a string representation, containing the local filesystem path of a file or something else.
        """
        return self.getfulllocalpath(path) or f"{self.name}:{path}"

    def writetofile(self, path: str, content: bytes) -> None:
        """
        Writes a byte array to a file.
        |dooverride|
        """
        raise NotImplementedError()

    def readfromfile(self, path: str) -> bytes:
        """
        Reads the content of a file and returns it.
        |dooverride|
        """
        raise NotImplementedError()

    def getoutputstream(self, path: str) -> t.BinaryIO:
        """
        Returns a binary file stream (like Python's `open` would do) for writing to a path.
        |dooverride|
        """
        raise NotImplementedError()

    def getinputstream(self, path: str) -> t.BinaryIO:
        """
        Returns a binary file stream (like Python's `open` would do) for reading from a path.
        |dooverride|
        """
        raise NotImplementedError()

    def listxattrkeys(self, path: str) -> t.List[str]:
        """
        Returns a list of names of extended attributes stored for a file.
        |dooverride|
        """
        raise NotImplementedError()

    def getxattrvalue(self, path: str, key: str) -> str:
        """
        Returns the extended attribute value for a file and a key.
        |dooverride|
        """
        raise NotImplementedError()

    def setxattrvalue(self, path: str, key: str, value: str) -> None:
        """
        Sets an extended attribute value on a file.
        |dooverride|
        """
        raise NotImplementedError()

    def unsetxattrvalue(self, path: str, key: str) -> None:
        """
        Unsets an extended attribute value on a file.
        |dooverride|
        """
        raise NotImplementedError()

    def initialize(self, sync: 'parzzley.syncengine.sync.Sync', runtime: 'parzzley.runtime.runtime.RuntimeData') -> None:
        """
        Runs initialization (before preparations are executed).
        |dooverride_optional|
        """
        pass

    # noinspection PyUnusedLocal
    def initialize_late(self, sync: 'parzzley.syncengine.sync.Sync',
                        runtime: 'parzzley.runtime.runtime.RuntimeData') -> None:
        """
        Runs late initialization (after it is prepared).
        |dooverride_optional|
        """
        self._is_hot = True

    # noinspection PyUnusedLocal
    def shutdown(self, sync: 'parzzley.syncengine.sync.Sync', runtime: 'parzzley.runtime.runtime.RuntimeData') -> None:
        """
        Shuts down the filesystem.
        """
        self._is_hot = False

    def is_mtime_precision_fine(self) -> bool:
        """
        Checks if the filesystem has fine (typically milliseconds) time granularity.
        |dooverride_optional|
        """
        return False

    def checkalive(self) -> None:
        """
        Ensures that the filesystem is alive and throws an exception otherwise.
        Call this method whenever you have fetched some infos whose correctness is critical for the further processing.
        """
        controlfs = self.get_control_filesystem()
        if not controlfs.exists(""):
            raise SyncFilesystemError(f"filesystem {self.name} disconnected")
        if self.checkaliveskeptically:
            try:
                controlfs.writetofile("checkalive_test", b"")
                if not controlfs.exists("checkalive_test"):
                    raise SyncFilesystemError(f"filesystem {self.name} disconnected")
            finally:
                controlfs.removefile("checkalive_test")

    def get_control_filesystem(self, path: t.Optional[str] = None) -> 'Filesystem':
        """
        Returns a parzzley.filesystem.abstractfilesystem.Filesystem wrapper to the control directory. This is typically 
        backed within sync volume itself and can be used for storing control information on that (potentially remote) 
        place.
        """
        def _initctrlfs(ctrlfs, is_really_onvolume):
            ctrlfs._iscontrolfs = True
            ctrlfs.is_really_onvolume = is_really_onvolume
            ctrlfs._parentfs = self
        if self._iscontrolfs:
            return self._parentfs.get_control_filesystem(path=path)
        if not self._is_hot:
            raise parzzley.exceptions.ParzzleyEngineExecutionError("it is not allowed to fetch the control filesystem of "
                                                                 "an un-hot filesystem.")
        if path is None:
            if self._controlfs is None:
                self._controlfs, _controlfs_isreallyonvolume = self._create_control_filesystem("")
                _initctrlfs(self._controlfs, _controlfs_isreallyonvolume)
            return self._controlfs
        else:
            cfs, cfsisrov = self._create_control_filesystem(path)
            _initctrlfs(cfs, cfsisrov)
            return cfs

    def get_parent_filesystem(self) -> 'Filesystem':
        """
        If this is a control filesystem, it returns the original one, otherwise `self`.
        """
        return self._parentfs if self._iscontrolfs else self

    def is_control_filesystem(self) -> bool:
        """
        Checks if this is a control filesystem.
        """
        return self._iscontrolfs

    def _create_control_filesystem(self, path) -> t.Tuple['Filesystem', bool]:
        """
        Creates a control filesystem.
        |dooverride|
        """
        raise NotImplementedError()

    def translate_path(self, path: str, dstfs: 'Filesystem') -> t.Optional[str]:
        """
        Translates a path from this filesystem into a path valid for another one.
        Returns `None` if this translation is not possible.
        """
        if dstfs == self:
            return path
        fullpath = self.getfulllocalpath(path)
        if fullpath:
            dstrpath = dstfs.getfulllocalpath("")
            if dstrpath:
                fullpath = parzzley.tools.common.abspath(fullpath)
                dstrpath = parzzley.tools.common.abspath(dstrpath)
                if fullpath.startswith(dstrpath):
                    return parzzley.tools.common.abspath("/" + fullpath[len(dstrpath):])
