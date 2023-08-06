# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Tracks the success of sync runs, invokes warning messages after some time of sync problems, ...
"""

import datetime
import os
import typing as t

import parzzley.logger

if t.TYPE_CHECKING:
    import parzzley.runtime.runtime
    import parzzley.syncengine.sync


# noinspection PyProtectedMember
class SuccessTracker:
    """
    Tracks the success of sync runs.
    
    Used internally for logging warnings when a synchronization did not run successfully since a certain timespan. It 
    stores timestamps on the filesystem for this functionality.
    """

    def __init__(self, runtime: 'parzzley.runtime.runtime.RuntimeData'):
        self.runtime = runtime
        self.syncs = None

    def setscope(self, syncs: t.List['parzzley.syncengine.sync.Sync']) -> None:
        """
        Sets the list of sync tasks for processing.
        """
        self.syncs = syncs

    def begincall(self, sync: 'parzzley.syncengine.sync.Sync') -> None:
        """
        Called by the infrastructure when a sync run begins, for bookkeeping.
        """
        rp = self.runtime.sync_success_storage.get_value_path(sync)
        if os.path.exists(rp):
            self.runtime._successtracker_dt1 = os.path.getmtime(rp)
        else:
            self.runtime._successtracker_dt1 = None

    def successfulcall(self, sync: 'parzzley.syncengine.sync.Sync') -> None:
        """
        Marks a sync task as successfully executed.
        """
        now = datetime.datetime.now().timestamp()
        syncrequestedmeanwhile = False
        if self.runtime.sync_success_storage.get_value_string(sync=sync, throwonnotexists=False).startswith(" "):
            rp = self.runtime.sync_success_storage.get_value_path(sync)
            dt = os.path.getmtime(rp)
            # noinspection PyUnresolvedReferences
            if dt != self.runtime._successtracker_dt1:
                syncrequestedmeanwhile = True
        val = (" " if syncrequestedmeanwhile else "") + str(int(now)) + "\n"
        self.runtime.sync_success_storage.set_value(sync=sync, value=val)

    def forceexecution(self, sync: 'parzzley.syncengine.sync.Sync') -> None:
        """
        Marks a sync task so it gets executed next time regardless of the sync interval.
        """
        if self.runtime.sync_success_storage.has_value(sync=sync):
            vv = " " + self.runtime.sync_success_storage.get_value_string(sync=sync).lstrip()
            self.runtime.sync_success_storage.set_value(sync=sync, value=vv)

    def getlastsuccessfulcall(self,
                              sync: 'parzzley.syncengine.sync.Sync') -> t.Tuple[t.Optional[datetime.datetime], bool]:
        """
        Gets a tuple of the time of last successful execution and the forced flag of a task.
        """
        forced = True
        lastsucc = None
        succcnt = self.runtime.sync_success_storage.get_value_string(sync=sync, throwonnotexists=False)
        if succcnt:
            forced = succcnt.startswith(" ")
            lastsucc = datetime.datetime.fromtimestamp(int(succcnt.strip()))
        return lastsucc, forced

    def shall_skip(self, sync: 'parzzley.syncengine.sync.Sync') -> bool:
        """
        Determines if a sync task should be skipped now.
        """
        lastsucc, forced = self.getlastsuccessfulcall(sync)
        return (not forced) and (datetime.datetime.now() - lastsucc < sync.interval)

    def end(self) -> None:
        """
        Signals that a task execution was scheduled for now and the process is over. This happens for successful
        and for failed executions and triggers a warning notification in certain situations.
        """
        for sync in self.syncs:
            slastsucc = self.runtime.sync_success_storage.get_value_string(sync=sync, throwonnotexists=False)
            if slastsucc:
                lastsucc = datetime.datetime.fromtimestamp(int(slastsucc))
            else:
                lastsucc = datetime.datetime(1999, 1, 1)
            if datetime.datetime.now() - lastsucc > sync.warn_after:
                slastwarned = self.runtime._last_warned_storage.get_value_string(sync=sync, throwonnotexists=False)
                if slastwarned:
                    lastwarned = datetime.datetime.fromtimestamp(int(slastwarned))
                else:
                    lastwarned = datetime.datetime(2000, 1, 1)
                if datetime.datetime.now() - lastwarned > sync.warn_interval:
                    if slastsucc:
                        i = datetime.datetime.now() - lastsucc
                        if i.total_seconds() < 60:
                            d = str(int(i.total_seconds()))
                            d += " second" + ("s" if (d != "1") else "")
                        elif i.total_seconds() < 60 * 60:
                            d = str(int(i.total_seconds() / 60))
                            d += " minute" + ("s" if (d != "1") else "")
                        elif i.total_seconds() < 24 * 60 * 60:
                            d = str(int(i.total_seconds() / (60 * 60)))
                            d += " hour" + ("s" if (d != "1") else "")
                        elif i.days < 30:
                            d = str(int(i.days))
                            d += " day" + ("s" if (d != "1") else "")
                        elif i.days < 365:
                            d = str(int(i.days / 30))
                            d += " month" + ("s" if (d != "1") else "")
                        else:
                            d = str(int(i.days / 365))
                            d += " year" + ("s" if (d != "1") else "")
                        logverb = f"not exec'ed since {d}"
                    else:
                        logverb = "never exec'ed"
                    self.runtime.log(subject=sync.name, verb=logverb, severity=parzzley.logger.Severity.ERROR)
                    now = datetime.datetime.now().timestamp()
                    self.runtime._last_warned_storage.set_value(sync=sync, value=f"{int(now)}\n")
