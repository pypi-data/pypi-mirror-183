# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Runtime additions for a sync event execution.
"""

import datetime
import os
import sys
import typing as t
import uuid

import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.benchmark
import parzzley.syncengine.common
import parzzley.syncengine.entrylist

if t.TYPE_CHECKING:
    import parzzley.filesystem.abstractfilesystem


class SyncEventRuntime:
    """
    Control interface for hook methods in parzzley.aspect.abstractaspect.Aspect implementations.
    
    Also holds all kinds of data for one run of parzzley.syncengine.sync.Sync.sync_directory.

    Dynamically extends :py:class:`parzzley.syncengine.syncruntime.SyncRuntime`.
    """

    def __init__(self, path: str):
        self.path = path
        self.masterfs = None
        self._masterfs_key = None
        self._skipupdate = False
        self._conflicts = []
        self._hadconflicts = False
        self._update_bad = False

    def add_conflict(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem',
                     comment: t.Optional[str] = None) -> None:
        """
        Adds a new conflict.
        """
        self._conflicts.append((fs, comment))
        self._hadconflicts = True

    def had_conflicts(self) -> bool:
        """
        Returns if there are or were any conflicts.
        """
        return self._hadconflicts

    def remove_conflict(self, i: int) -> None:
        """
        Removes a conflict by index.
        """
        self._conflicts.pop(i)

    def get_conflicts(self) -> t.List[t.Tuple['parzzley.filesystem.abstractfilesystem.Filesystem', t.Optional[str]]]:
        """
        Returns the list of all recognized conflicts.
        """
        return self._conflicts

    def skip_update(self) -> None:
        """
        Marks the update process to skip.
        """
        self._skipupdate = True

    def is_update_set_skipped(self) -> bool:
        """
        Returns if the update process is markes to skip (by skip_update).
        """
        return self._skipupdate

    def mark_update_bad(self) -> None:
        """
        Marks the current update as bad.
        """
        self._update_bad = True

    def is_update_marked_bad(self) -> bool:
        """
        Returns if the update is marked as bad.
        """
        return self._update_bad

    def promote_master_filesystem(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', key: t.Tuple) -> None:
        """
        Elects a master filesystem.

        :param fs: The filesystem.
        :param key: A tuple of numbers of comparison - the highest value wins.
        """
        if not isinstance(key, tuple):
            key = (key,)
        if (self._masterfs_key is None) or (key > self._masterfs_key):
            self.masterfs = fs
            self._masterfs_key = key

    def skip_master_filesystem_promotion(self) -> None:
        """
        Elects 'SKIP' filesystem with highest key. This will lead to skipping the current item.
        """
        self.promote_master_filesystem(parzzley.syncengine.common.SKIP, (sys.maxsize,))


class SyncRuntime:
    """
    Control interface for sync executions.

    Dynamically extends :py:class:`parzzley.runtime.runtime.RuntimeData`.
    """

    def _read_filelist(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem') -> None:
        self._filelists_last[fs] = _x = parzzley.syncengine.entrylist.EntryList()
        _y = self._filelists_storage.get_value_bytes(path=fs.name, throwonnotexists=False)
        _x.read(_y)
        _x = parzzley.syncengine.entrylist.EntryList()
        _x.read(_y)
        # we actually track two lists here: one primary and one derived from the old list for crashes
        self._filelists_curr[fs] = parzzley.syncengine.entrylist.CombinedEntryList(
            parzzley.syncengine.entrylist.EntryList(), _x)

    def _syncruntime_init(self) -> None:
        self._filelists_last = {}
        self._filelists_curr = {}
        self._filelists_storage = parzzley.runtime.datastorage.get_storage_department(
            self, "filelists", location=parzzley.runtime.datastorage.StorageLocation.SYSTEM,
            scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
        for fs in self.sync.filesystems:
            self._read_filelist(fs)
        self.benchmark = parzzley.syncengine.benchmark.BenchmarkRun(self)

    def _verify_filelists_cookies(self) -> None:
        lastcookiesstorage = parzzley.runtime.datastorage.get_storage_department(
            self, "lastfscookie", location=parzzley.runtime.datastorage.StorageLocation.SYSTEM,
            scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
        for fs in self.sync.filesystems:
            lastcookie = lastcookiesstorage.get_value_string(path=fs.name, throwonnotexists=False)
            currcookie = self.getfscookie(fs)
            if currcookie != lastcookie:
                if self._filelists_storage.has_value(path=fs.name, filesystem=None):
                    self._filelists_storage.remove_value(path=fs.name, filesystem=None)
                lastcookiesstorage.set_value(currcookie, path=fs.name)
                self._read_filelist(fs)

    def getfscookie(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem') -> str:
        """
        Gets the cookie of a filesystem (for checking if it was completely purged/replaced between sync runs)
        """
        cstorage = parzzley.runtime.datastorage.get_storage_department(
            self, "fscookie", location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
            scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
        cookie = cstorage.get_value_string(filesystem=fs, throwonnotexists=False)
        if not cookie:
            cookie = str(uuid.uuid4())
            cstorage.set_value(cookie, filesystem=fs)
        return cookie

    def getinfo_current_exists(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> bool:
        """
        Gets the info from the Parzzley bookkeeping, if an entry with given path current exists.
        """
        return self._filelists_curr[fs].getftype(path) is not None

    def getinfo_current_ftype(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> str:
        """
        Gets the info from the Parzzley bookkeeping, which type an entry with given path has currently.
        The type is one of parzzley.syncengine.common.EntryType.
        """
        return self._filelists_curr[fs].getftype(path)

    def getinfo_current_size(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> int:
        """
        Gets the info from the Parzzley bookkeeping, which size an entry with given path has currently.
        """
        return self._filelists_curr[fs].getsize(path)

    def getinfo_current_mtime(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem',
                              path: str) -> datetime.datetime:
        """
        Gets the info from the Parzzley bookkeeping, which modification time an entry with given path has currently.
        """
        return self._filelists_curr[fs].getmtime(path)

    def getinfo_current_param(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> str:
        """
        Gets the info from the Parzzley bookkeeping, which param an entry with given path has currently.
        The param is used for storing the target path of a symlink, but is designed to be a general purpose field.
        """
        return self._filelists_curr[fs].getparam(path)

    def getinfo_lastrun_exists(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> bool:
        """
        Gets the info from the Parzzley bookkeeping, if an entry with given path existed after last run.
        """
        return self._filelists_last[fs].getftype(path) is not None

    def getinfo_lastrun_ftype(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> str:
        """
        Gets the info from the Parzzley bookkeeping, which type an entry with given path had after last run.
        The type is one of parzzley.syncengine.common.EntryType.
        """
        return self._filelists_last[fs].getftype(path)

    def getinfo_lastrun_size(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> int:
        """
        Gets the info from the Parzzley bookkeeping, which size an entry with given path had after last run.
        """
        return self._filelists_last[fs].getsize(path)

    def getinfo_lastrun_mtime(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem',
                              path: str) -> datetime.datetime:
        """
        Gets the info from the Parzzley bookkeeping, which modification time an entry with given path had after last run.
        """
        return self._filelists_last[fs].getmtime(path)

    def getinfo_lastrun_param(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> str:
        """
        Gets the info from the Parzzley bookkeeping, which param an entry with given path had after last run.
        The param is used for storing the target path of a symlink, but is designed to be a general purpose field.
        """
        return self._filelists_last[fs].getparam(path)

    def setinfo_updatefile(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str, ftype: str,
                           size: t.Optional[int] = None, mtime: t.Optional[datetime.datetime] = None,
                           param: t.Optional[str] = None) -> None:
        """
        Updates the info stored for a given path in the Parzzley bookkeeping.
        """
        self._filelists_curr[fs].updatefile(path, ftype, size, mtime, param)

    def setinfo_removefile(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> None:
        """
        Mark a file as removed for a given path in the Parzzley bookkeeping.
        """
        self._filelists_curr[fs].removefile(path)

    def getinfo_lastrun_gettags(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> t.List[str]:
        """
        Gets the tags this entry currently got. See also setinfo_current_addtag().
        """
        return self._filelists_last[fs].gettags(path)

    def getinfo_current_gettags(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> t.List[str]:
        """
        Gets the tags this entry got in the last run. See also setinfo_current_addtag().
        """
        return self._filelists_curr[fs].gettags(path)

    def setinfo_current_addtag(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str,
                               tag: str) -> None:
        """
        Adds a tag to this entry.
        Tags are strings that can be set and retrieved from different places in order to exchange state information.
        For example, the engine sets the tag `'S+'` to an entry after successful synchronization.
        """
        self._filelists_curr[fs].addtag(path, tag)

    def create_directory(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> None:
        """
        Creates a directory in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        for createdpath in fs.createdirs(path, recursive=True):
            self.syncglobaldata.changed_flag = True
            mtime = fs.getmtime(createdpath)
            self.setinfo_updatefile(fs, createdpath, parzzley.syncengine.common.EntryType.Directory, 0, mtime, None)

    def delete_directory(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str, *,
                         recursive: bool = False) -> None:
        """
        Deletes a directory in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        self.syncglobaldata.changed_flag = True
        fs.removedir(path, recursive=recursive)
        self.setinfo_removefile(fs, path)

    def delete_item(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> None:
        """
        Deletes an item (file, directory, ...) in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        ftype = self.getinfo_current_ftype(fs, path)
        if ftype == parzzley.syncengine.common.EntryType.File:
            self.delete_file(fs, path)
        elif ftype == parzzley.syncengine.common.EntryType.Link:
            self.delete_link(fs, path)
        elif ftype == parzzley.syncengine.common.EntryType.Directory:
            self.delete_directory(fs, path, recursive=True)

    def write_file(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', source: str, path: str, *,
                   verifier: t.Callable = lambda path, tempfile, mtime, size: True,
                   forcedupdate: bool = False) -> t.Tuple[datetime.datetime, int]:
        """
        Creates a file in a filesystem with some content.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        def fileverifier(spath, tempfile, mtime, size):
            if not verifier(spath, tempfile, mtime, size):
                return False
            if forcedupdate:
                self.delete_item(fs, path)
            self.create_directory(fs, os.path.dirname(path))
            return True
        _mt, _msize = fs.copyfile(source, path, fileverifier)
        if _mt is not None:
            self.setinfo_updatefile(fs, path, parzzley.syncengine.common.EntryType.File, _msize, fs.getmtime(path), None)
        self.syncglobaldata.changed_flag = True
        return _mt, _msize

    def delete_file(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> None:
        """
        Deletes a file in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        fs.removefile(path)
        self.setinfo_removefile(fs, path)
        self.syncglobaldata.changed_flag = True

    def create_link(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str, linktgt: str, *,
                    forcedupdate: bool = False) -> None:
        """
        Creates a link in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        if forcedupdate:
            self.delete_item(fs, path)
        elif self.getinfo_current_ftype(fs, path) == parzzley.syncengine.common.EntryType.Link:
            self.delete_link(fs, path)
        self.create_directory(fs, os.path.dirname(path))
        fs.createlink(linktgt, path)
        self.setinfo_updatefile(fs, path, parzzley.syncengine.common.EntryType.Link, None, None, linktgt)
        self.syncglobaldata.changed_flag = True

    def delete_link(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', path: str) -> None:
        """
        Deletes a link in a filesystem.
        This is a high-level function that automatically handles the Parzzley bookkeeping and have some safeguards.
        """
        fs.removelink(path)
        self.setinfo_removefile(fs, path)
        self.syncglobaldata.changed_flag = True

    def logcreate(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', subject: str, verb: str = "created",
                  comment: str = "", symbol: str = "+", severity: int = parzzley.logger.Severity.INFO) -> None:
        """
        Logs events around item creation.
        """
        self.sync.executeevent(parzzley.syncengine.common.SyncEvent.LogCreate, eventcontext=self.clone(),
                               subject=subject, verb=verb, comment=comment, symbol=symbol, severity=severity, logfs=fs)

    def logremove(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', subject: str, verb: str = "removed",
                  comment: str = "", symbol: str = "-", severity=parzzley.logger.Severity.MOREIMPORTANT) -> None:
        """
        Logs events around item removal.
        """
        self.sync.executeevent(parzzley.syncengine.common.SyncEvent.LogRemove, eventcontext=self.clone(),
                               subject=subject, verb=verb, comment=comment, symbol=symbol, severity=severity, logfs=fs)

    def logupdate(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', subject: str, verb: str = "updated",
                  comment: str = "", symbol: str = "*", severity=parzzley.logger.Severity.IMPORTANT) -> None:
        """
        Logs events around updates of exiting items.
        """
        self.sync.executeevent(parzzley.syncengine.common.SyncEvent.LogUpdate, eventcontext=self.clone(),
                               subject=subject, verb=verb, comment=comment, symbol=symbol, severity=severity, logfs=fs)

    def logproblem(self, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem', subject: str,
                   verb: str = "has problems", comment: str = "", symbol: str = "E",
                   severity=parzzley.logger.Severity.ERROR) -> None:
        """
        Logs events around problems.
        """
        self.sync.executeevent(parzzley.syncengine.common.SyncEvent.LogProblem, eventcontext=self.clone(),
                               subject=subject, verb=verb, comment=comment, symbol=symbol, severity=severity, logfs=fs)
