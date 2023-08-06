# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
The implementation for some Parzzley core features.
"""

import copy
import time
import types
import typing as t

import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.runtime.returnvalue
import parzzley.runtime.successtracker

if t.TYPE_CHECKING:
    import parzzley.syncengine.sync


class RuntimeData:
    """
    Runtime data for synchronization runs used by the Parzzley engine and some higher layers. Used by the
    synchronization implementations for logging, for communicating success values and for retrieving/setting some
    environment values. There is one instance for each Parzzley engine run (which can do multiple synchronizations).
    """

    def __init__(self, datadir: str, loggers: t.List[parzzley.logger.Logger],
                 syncs: t.List[parzzley.syncengine.sync.Sync]):
        """
        :param datadir: Path to the directory for local Parzzley control data.
        :param loggers: List of loggers.
        :param syncs: List of sync tasks.
        """
        class MyGlobalData:
            def __init__(self):
                self.retval = 0
        self._globaldata = MyGlobalData()
        self.datadir = datadir
        self.syncs = syncs
        self._loggers = loggers
        self._logmessages = []
        self.sync_success_storage = parzzley.runtime.datastorage.get_storage_department(
            self, "sync_success", scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC,
            location=parzzley.runtime.datastorage.StorageLocation.SYSTEM)
        self._last_warned_storage = parzzley.runtime.datastorage.get_storage_department(
            self, "last_warned", scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC,
            location=parzzley.runtime.datastorage.StorageLocation.SYSTEM)
        self.successtracker = parzzley.runtime.successtracker.SuccessTracker(self)
        self.successtracker.setscope(syncs)

    def set_retval(self, flag: int) -> None:
        """
        Sets a flag from parzzley.runtime.returnvalue.ReturnValue to the return value.
        """
        self._globaldata.retval |= flag

    def get_retval(self) -> int:
        """
        Gets the return value as combination of parzzley.runtime.returnvalue.ReturnValue.
        """
        return self._globaldata.retval

    def mark_dirty(self) -> None:
        """
        Marks the current sync run as dirty, which leads to a faster re-execution (e.g. since one or more file was 
        skipped).
        """
        self.set_retval(parzzley.runtime.returnvalue.ReturnValue.DIRTY)

    def clone(self, merge_also_from: t.Optional[t.Any] = None,
              merge_also: t.Optional[t.Dict[str, t.Optional[t.Any]]] = None) -> 'RuntimeData':
        """
        Clones this object.
        
        This is used for providing objects for repeating sub-processes, so they always get a fresh but pre-populated
        RuntimeData object. This method returns a shallow copy, which is used for writing stuff to the original from a 
        clone in some ways.

        :param merge_also_from: Take all members from this object into the new clone as well.
        :param merge_also: Take all entries from this dictionary as members into the new clone as well.
        """
        result = copy.copy(self)
        def _val(o):
            if callable(o):
                # noinspection PyUnresolvedReferences
                o = types.MethodType(o.__func__, result)
            return o
        if merge_also:
            for a in merge_also:
                if not a.startswith("__"):
                    setattr(result, a, _val(merge_also[a]))
        if merge_also_from:
            for a in dir(merge_also_from):
                if not a.startswith("__"):
                    setattr(result, a, _val(getattr(merge_also_from, a)))
        for fn in dir(result):
            ff = getattr(result, fn)
            if isinstance(ff, types.MethodType):
                setattr(result, fn, types.MethodType(ff.__func__, result))
        return result

    def log(self, *, subject: str = "", verb: str = "", comment: str = "", severity: int = parzzley.logger.Severity.INFO,
            symbol: str = "") -> None:
        """
        This is the log method that is actually used by clients.

        :param subject: The name of the subject, e.g. a file name (arbitrary string).
        :param verb: A description what happened with the subject, e.g. 'deleted' or 'created' (arbitrary string).
        :param comment: A description following after the verb (arbitrary string).
        :param severity: A parzzley.logger.severity.Severity describes how important this message is. This value
                         decides if the message will be really logged.
        :param symbol: One character that describes the kind of log message (arbitrary string).
        """
        sync = getattr(self, "sync", None)
        name = sync.name if sync else ""
        if severity >= parzzley.logger.Severity.INFO:
            self._logmessages.append((time.time(), name, subject, verb, comment, severity, symbol))
        for logger in self._loggers:
            logger.log(name, subject, verb, comment, severity, symbol)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.successtracker.end()
        for logger in self._loggers:
            logger.flush()
