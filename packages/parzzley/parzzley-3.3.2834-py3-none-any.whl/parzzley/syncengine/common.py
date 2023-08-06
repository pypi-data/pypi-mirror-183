# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Boring common data structures.
"""

import parzzley.exceptions


class SyncEvent:
    """
    Names of well known synchronization events.
    """

    #: Occurs in updating directories, when the preparation phase takes places, but before the directory is listed.
    #: Use this state for preparing directory synchronization or for some bookkeeping.
    UpdateDir_Prepare = "UpdateDir_Prepare"

    #: Occurs in updating directories, when the list of entry names must be fetched.
    #: Use this state for listing the directory. The code must call `ctx.entrylist.update` with a list of entry names
    #: in order to participate to listing the directory.
    UpdateDir_ListDir = "UpdateDir_ListDir"

    #: Occurs in updating directories, when the directory was updated completely.
    #: Use this state for executing code after a directory was synchronized, e.g. for bookkeeping.
    UpdateDir_AfterUpdate = "UpdateDir_AfterUpdate"

    #: Occurs in updating items, when very early initialization can happen, before the actual
    #: master election phase begins. Use this state for executing code at the very beginning of
    #: item synchronization, even before the master election takes place, e.g. for some bookkeeping.
    UpdateItem_BeforeElectMaster = "UpdateItem_BeforeElectMaster"

    #: Occurs in updating items, when the master election phase began. Elect a master filesystem
    #: here in order to control which filesystems gets updated from which one.
    #: Use parzzley.syncengine.syncruntime.SyncEventRuntime.promote_master_filesystem on `ctx`
    #: in order to elect a master filesystem or
    #: parzzley.syncengine.syncruntime.SyncEventRuntime.skip_master_filesystem_promotion for ultimatively
    #: vote for skipping the synchronization of this entry completely.
    #: In all subsequent steps, the elected master filesystem is available in `ctx.masterfs`.
    UpdateItem_ElectMaster = "UpdateItem_ElectMaster"

    #: Occurs in updating items, when a master filesystem is just elected, for checking for conflicts. Hook methods
    #: here which checks for conflicts between the master filesystem and the filesystems it is hooked for.
    #: Signal conflicts by calling `ctx.add_conflict`.
    UpdateItem_CheckConflicts = "UpdateItem_CheckConflicts"

    #: Occurs in updating items, when conflicts occurred, in order to solve them. If this phase cannot resolve the
    #: conflicts, the usual update is skipped.
    #: Use this state for executing code that can resolve conflicts detected in SyncEvent.UpdateItem_CheckConflicts.
    #: For signalling that a conflict is resolved, call `ctx.remove_conflict`.
    #: It may decide to set a new `ctx.masterfs` for a new master filesystem.
    UpdateItem_ResolveConflicts = "UpdateItem_ResolveConflicts"

    #: Occurs in updating items, when conflicts were not resolved and the item is skipped due to that.
    #: Use this state for executing code that handles unresolved conflicts that led to skipping this item.
    UpdateItem_SkippedDueConflicts = "UpdateItem_SkippedDueConflicts"

    #: Occurs after conflict resolution took place and the actual update phase is just before beginning.
    UpdateItem_Update_Prepare = "UpdateItem_Update_Prepare"

    #: Occurs in updating items, when the actual update must take place and there exists an item in the master
    #: filesystem (typical update scenario).
    #: Use this state for actually transfer content from the master to the filesystem on which the hook runs.
    UpdateItem_Update_ExistsInMaster = "UpdateItem_Update_ExistsInMaster"

    #: Occurs in updating items, when the actual update must take place and there does not exist an item in the master
    #: filesystem (typical removal scenario).
    #: Use this state for actually remove content from the filesystem on which the hook runs.
    UpdateItem_Update_NotExistsInMaster = "UpdateItem_Update_NotExistsInMaster"

    #: Occurs in updating items, when the actual update phase is done.
    #: Use this state for executing code after the update took place, e.g. for some bookkeeping.
    UpdateItem_AfterUpdate = "UpdateItem_AfterUpdate"

    #: Occurs once at the very beginning of a synchronization task execution.
    BeginSync = "BeginSync"

    #: Occurs once at the very end of a synchronization task execution.
    EndSync = "EndSync"

    #: Occurs after EndSync, even when a fatal error occurred, i.e. typically an unhandled exception.
    #: This event is not used for typical stuff but only for infrastructures.
    CloseSync = "CloseSync"

    #: Logging.
    LogCreate = "LogCreate"

    #: Logging.
    LogUpdate = "LogUpdate"

    #: Logging.
    LogRemove = "LogRemove"

    #: Logging.
    LogProblem = "LogProblem"


class EntryType:
    """
    A type of an entry (sometimes the word 'file' is wrongly used instead of 'entry') in the filesystem.
    """

    #: Regular file
    File = "F"

    #: Symlink
    Link = "L"

    #: Directory
    Directory = "D"


#: A flag that means skipping parts of execution. It is a general purpose signalling object.
#: It might be interpreted from different parties at different places in a different way.
#: Used e.g. in master election as a special master for skipping the synchronization process
#: (read parzzley.syncengine.syncruntime.SyncEventRuntime.skip_master_filesystem_promotion)
#: and in the update process for signalling skipping due to lately found conflicts
#: (read parzzley.aspect.execute_only_if_not_update_set_skipped).
SKIP = object()


class SyncError(parzzley.exceptions.ParzzleyError):
    """
    Errors happening in the sync engine.
    """
    pass


class SyncConfigurationError(SyncError):
    """
    Errors while processing the sync configuration.
    """
    pass


class SyncExecutionError(SyncError):
    """
    Errors while executing the synchronization task.
    """
    pass
