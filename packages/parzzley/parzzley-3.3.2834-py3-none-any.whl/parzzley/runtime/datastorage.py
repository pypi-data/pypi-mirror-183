# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Implements an abstraction layer for storing arbitrary process data, like sync states or file history information.
"""

import os
import typing as t

import parzzley.exceptions
import parzzley.filesystem.local
import parzzley.syncengine.common
import parzzley.tools.common

if t.TYPE_CHECKING:
    import parzzley.filesystem.abstractfilesystem
    import parzzley.runtime.runtime
    import parzzley.syncengine.sync


class StorageLocation:
    """
    Enumeration of storage locations.
    """

    SYSTEM = "system"
    SYNC_VOLUME = "sync_volume"


class StorageScope:
    """
    Enumeration of storage scopes.
    """

    PER_SYNC = "per_sync"
    SHARED = "shared"


class StorageDepartment:
    """
    One main hive for data storage.
    
    A main hive has a name and can store data in a tree-like structure (as in filesystems).
    Different subclasses exist and can be configured in different flavours.
    """

    #: Internally used as special file name for value storage.
    VALUE_FILENAME = ".~parzzley+~value."  # TODO zz

    def set_value(self, value: t.AnyStr, *, path: str = "/",
                  filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                  sync: t.Optional['parzzley.syncengine.sync.Sync'] = None) -> None:
        """
        Sets and stores a value.

        :param value: The value data.
        :param path: The data path.
        :param filesystem: The filesystem to store the data for. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        """
        raise NotImplementedError()

    def get_value_bytes(self, *, path: str = "/",
                        filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                        sync: t.Optional['parzzley.syncengine.sync.Sync'] = None, throwonnotexists: bool = True,
                        defaultval: t.Optional[bytes] = b"") -> t.Optional[bytes]:
        """
        Gets a value as `bytes` (byte array).

        :param path: The data path.
        :param filesystem: The filesystem to get the data for. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        :param throwonnotexists: If to throw an exception if there is no data stored for this path.
        :param defaultval: The default value (when no one exists and throwonnotexists=False).
        """
        raise NotImplementedError()

    def get_value_string(self, *, path: str = "/",
                         filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'] = None,
                         sync: t.Optional['parzzley.syncengine.sync.Sync'] = None, throwonnotexists: bool = True,
                         defaultval: t.Optional[str] = "") -> t.Optional[str]:
        """
        Gets a value as `string`.

        :param path: The data path.
        :param filesystem: The filesystem to get the data for. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        :param throwonnotexists: If to throw an exception if there is no data stored for this path.
        :param defaultval: The default value (when no one exists and throwonnotexists=False).
        """
        res = self.get_value_bytes(path=path, filesystem=filesystem, sync=sync, throwonnotexists=throwonnotexists,
                                   defaultval=None)
        return defaultval if (res is None) else res.decode()

    def get_filesystem(self, *, filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                       sync: t.Optional['parzzley.syncengine.sync.Sync'] = None
                       ) -> 'parzzley.filesystem.abstractfilesystem.Filesystem':
        """
        Gets the hive filesystem for more complex custom operations.

        :param filesystem: The filesystem to get the data for. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        """
        raise NotImplementedError()

    def list_path(self, *, path: str, filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                  sync: t.Optional['parzzley.syncengine.sync.Sync'] = None) -> t.List[str]:
        """
        Returns a list of names of all subitems in the given path.
        Those can either lead to further subitems, or can have a value, or both!

        :param path: The data path.
        :param filesystem: The filesystem to list the items for. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        """
        fs = self.get_filesystem(filesystem=filesystem, sync=sync)
        return [x for x in fs.listdir(path) if fs.getftype(path+"/"+x) == parzzley.syncengine.common.EntryType.Directory]

    def has_value(self, *, path: str = "/", filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                  sync: t.Optional['parzzley.syncengine.sync.Sync'] = None) -> bool:
        """
        Checks if some value is stored for a path.

        :param path: The data path.
        :param filesystem: The filesystem to check. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        """
        fs = self.get_filesystem(filesystem=filesystem, sync=sync)
        return fs.exists(path+"/"+StorageDepartment.VALUE_FILENAME)

    def remove_value(self, *, path: str, filesystem: t.Optional['parzzley.filesystem.abstractfilesystem.Filesystem'],
                     sync: t.Optional['parzzley.syncengine.sync.Sync'] = None, recursive: bool = False,
                     throwonnotexists: bool = True) -> None:
        """
        Removes a value from storage.

        :param path: The data path.
        :param filesystem: The filesystem to remove data from. Not used in some implementations.
        :param sync: The sync. Typically not needed to specify it.
        :param recursive: If to remove also all subitems.
        :param throwonnotexists: If to throw an exception if there is no data stored for this path.
        """
        fs = self.get_filesystem(filesystem=filesystem, sync=sync)
        if recursive:
            if throwonnotexists or fs.exists(path):
                fs.removedir(path, recursive=True)
        else:
            apath = parzzley.tools.common.abspath(f"/{path}")
            vpath = f"{apath}/{StorageDepartment.VALUE_FILENAME}"
            if throwonnotexists or fs.exists(vpath):
                fs.removefile(vpath)
                p = path
                while fs.exists(p) and len(fs.listdir(p)) == 0 and p != "/":
                    fs.removedir(p, recursive=False)
                    p = os.path.dirname(p)


class SyncVolumeStorageDepartment(StorageDepartment):
    """
    Implementation of StorageDepartment for storage of data inside the sync volume
    (i.e. potentially on the remote device).
    
    @note Although the data is stored in the sync volume, this data is not part of what gets synchronized 
          (but resides in a hidden part).
    """

    def __init__(self, runtime, name, scope):
        super().__init__()
        self._runtime = runtime
        self._name = name
        self._scope = scope

    def _get_rootpath(self, sync):
        if sync is None:
            sync = self._runtime.sync
        if self._scope == StorageScope.PER_SYNC:
            return f"/{self._name}/{sync.name}/"
        elif self._scope == StorageScope.SHARED:
            return f"/{self._name}/"

    def get_value_path(self, sync, path="/"):
        return f"{self._get_rootpath(sync)}{path}/{StorageDepartment.VALUE_FILENAME}"

    def set_value(self, value, *, path="/", filesystem="", sync=None):
        fss = []
        if sync is None:
            sync = self._runtime.sync
        if filesystem is None:
            fss = sync.filesystems
        elif filesystem != "":
            fss.append(filesystem)
        else:
            raise parzzley.exceptions.ParzzleyEngineExecutionError(
                "SyncVolumeStorageDepartment.set_value requires 'filesystem' parameter. Use None for all.")
        if not isinstance(value, bytes):
            value = value.encode()
        for fs in fss:
            ctrlfs = fs.get_control_filesystem()
            p = self.get_value_path(sync, path)
            ctrlfs.createdirs(os.path.dirname(p))
            ctrlfs.writetofile(p, value)

    def get_value_bytes(self, *, path="/", filesystem, sync=None, throwonnotexists=True, defaultval=b""):
        p = self.get_value_path(sync, path)
        ctrlfs = filesystem.get_control_filesystem()
        if throwonnotexists or ctrlfs.exists(p):
            return ctrlfs.readfromfile(p)
        return defaultval

    def get_filesystem(self, *, filesystem, sync=None):
        rp = self._get_rootpath(sync)
        controlfs = filesystem.get_control_filesystem(path=rp)
        controlfs.createdirs("")
        return controlfs


class SystemStorageDepartment(StorageDepartment):
    """
    Implementation of StorageDepartment for storage of data inside the system, i.e. not on some remote place.
    """

    def __init__(self, runtime, name, scope):
        super().__init__()
        self._runtime = runtime
        self._name = name
        self._scope = scope

    def _get_rootpath(self, sync):
        if sync is None:
            sync = self._runtime.sync
        res = f"{self._runtime.datadir}/{self._name}/"
        if self._scope == StorageScope.PER_SYNC:
            return f"{res}{sync.name}/"
        if self._scope == StorageScope.SHARED:
            return res

    def get_value_path(self, sync, path="/"):
        return f"{self._get_rootpath(sync)}{path}/{StorageDepartment.VALUE_FILENAME}"

    def set_value(self, value, *, path="/", filesystem=None, sync=None):
        if sync is None:
            sync = self._runtime.sync
        if filesystem is not None:
            raise parzzley.exceptions.ParzzleyEngineExecutionError(
                "SystemStorageDepartment does not allow to specify 'filesystem'.")
        p = self.get_value_path(sync, path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb" if isinstance(value, bytes) else "w") as f:
            f.write(value)

    def get_value_bytes(self, *, path="/", filesystem=None, sync=None, throwonnotexists=True, defaultval=b""):
        if filesystem is not None:
            raise parzzley.exceptions.ParzzleyEngineExecutionError(
                "SystemStorageDepartment does not allow to specify 'filesystem'.")
        p = self.get_value_path(sync, path)
        if throwonnotexists or os.path.exists(p):
            with open(p, "rb") as f:
                return f.read()
        return defaultval

    def get_filesystem(self, *, filesystem=None, sync=None):
        if filesystem is not None:
            raise parzzley.exceptions.ParzzleyEngineExecutionError(
                "SystemStorageDepartment does not allow to specify 'filesystem'.")
        path = self._get_rootpath(sync)
        os.makedirs(path, exist_ok=True)
        return parzzley.filesystem.local.LocalFilesystem(path=path, name=None)

    def has_value(self, **kwa):
        kwa["filesystem"] = None
        return super().has_value(**kwa)


def get_storage_department(ctx: 'parzzley.runtime.runtime.RuntimeData', name: str, *,
                           location: str = StorageLocation.SYNC_VOLUME,
                           scope: str = StorageScope.PER_SYNC
                           ) -> t.Union[SyncVolumeStorageDepartment, SystemStorageDepartment]:
    """
    Creates a StorageDepartment for storage of process data.

    :param ctx: The current runtime context.
    :param name: The name of this storage department name.
    :param location: The storage location. One of StorageLocation.
    :param scope: The storage scope. One of StorageScope.
    """
    if location == StorageLocation.SYNC_VOLUME:
        return SyncVolumeStorageDepartment(ctx, name, scope)
    elif location == StorageLocation.SYSTEM:
        return SystemStorageDepartment(ctx, name, scope)
    else:
        raise parzzley.exceptions.ParzzleyEngineExecutionError(f"Invalid location: {location}")
