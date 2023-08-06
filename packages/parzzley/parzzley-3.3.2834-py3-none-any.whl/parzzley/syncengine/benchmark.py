# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Time measurement of sync runs.
"""

import pickle
import time
import typing as t

if t.TYPE_CHECKING:
    import parzzley.filesystem.abstractfilesystem
    import parzzley.runtime.runtime
    import parzzley.syncengine.sync


class BenchmarkRun:
    """
    Collects benchmark data for a sync run.
    
    This collection is populated with data by the engine during execution and stored afterwards, so external tools
    can inspect this data and get detailed ideas about the runtime performance.
    """

    version = 1

    def __init__(self, syncruntime: 'parzzley.runtime.runtime.RuntimeData'):
        self.syncruntime = syncruntime
        self._begintime = time.time()
        self._endtime = None
        self._beginretval = syncruntime.get_retval()
        self._endretval = ""
        self._syncevents = []
        self._currentsyncevent = []
        self._currentsynceventhandler = [[None, None, None, None, self._syncevents]]

    def beginsync(self) -> None:
        self._begintime = time.time()
        self._beginretval = self.syncruntime.get_retval()

    def endsync(self) -> None:
        if self._endtime is None:
            self._endtime = time.time()
            self._endretval = self.syncruntime.get_retval()

    def beginsyncevent(self, syncevent: str, path: str) -> None:
        x = [syncevent, path, time.time(), None, []]
        self._currentsyncevent.append(x)
        self._currentsynceventhandler[-1][4].append(x)

    def endsyncevent(self) -> None:
        self._currentsyncevent[-1][3] = time.time()
        self._currentsyncevent.pop()

    def beginsynceventhandler(self, handler: 'parzzley.syncengine.sync.Sync.EventHandler',
                              filesystem: 'parzzley.filesystem.abstractfilesystem.Filesystem') -> None:
        x = [handler.func.__name__, filesystem, time.time(), None, []]
        self._currentsynceventhandler.append(x)
        self._currentsyncevent[-1][4].append(x)

    def endsynceventhandler(self) -> None:
        self._currentsynceventhandler[-1][3] = time.time()
        self._currentsynceventhandler.pop()

    def get_report(self):
        return pickle.dumps([self._syncevents, BenchmarkRun.version, self.syncruntime.runname, self._beginretval,
                             self._endretval, self._begintime, self._endtime])
