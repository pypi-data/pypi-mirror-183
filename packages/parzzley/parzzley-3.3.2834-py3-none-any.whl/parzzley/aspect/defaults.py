# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys

import parzzley.aspect.applypathacceptor
import parzzley.aspect.collectinformation
import parzzley.aspect.conflicts
import parzzley.aspect.defaultiteration
import parzzley.aspect.electmaster
import parzzley.aspect.readmefile
import parzzley.aspect.remove
import parzzley.aspect.update
import parzzley.aspect.volumepathbreadcrumb
import parzzley.aspect.volumesyncreport
import parzzley.syncengine.common
import parzzley.tools.pathacceptors


class DefaultBaseBare(parzzley.aspect.defaultiteration.DefaultIteration,
                      parzzley.aspect.collectinformation.CollectInformation,
                      parzzley.aspect.applypathacceptor.ApplyPathAcceptor,
                      parzzley.aspect.readmefile.ReadmeFile,
                      parzzley.aspect.volumepathbreadcrumb.VolumePathBreadcrumb,
                      parzzley.aspect.volumesyncreport.VolumeSyncReport):
    """
    Very basic part of default behavior for a plain synchronization.
    Part of parzzley.aspect.defaults.DefaultBase.
    """

    def __init__(self):
        parzzley.aspect.defaultiteration.DefaultIteration.__init__(self)
        parzzley.aspect.collectinformation.CollectInformation.__init__(self)
        parzzley.aspect.applypathacceptor.ApplyPathAcceptor.__init__(self,
                                                                    parzzley.tools.pathacceptors.builtinpathacceptor)
        parzzley.aspect.readmefile.ReadmeFile.__init__(self)
        parzzley.aspect.volumepathbreadcrumb.VolumePathBreadcrumb.__init__(self)
        parzzley.aspect.volumesyncreport.VolumeSyncReport.__init__(self)


class DefaultBase(DefaultBaseBare,
                  parzzley.aspect.electmaster.ElectMasterFileByMtime,
                  parzzley.aspect.electmaster.ElectMasterLinkByTargetHistory,
                  ):
    """
    Mid-basic part of default behavior for a plain synchronization.
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    def __init__(self):
        DefaultBaseBare.__init__(self)
        parzzley.aspect.electmaster.ElectMasterFileByMtime.__init__(self)
        parzzley.aspect.electmaster.ElectMasterLinkByTargetHistory.__init__(self)


class DefaultSync(DefaultBase, parzzley.aspect.update.DefaultUpdateItems, parzzley.aspect.conflicts.DetectTypeConflicts,
                  parzzley.aspect.conflicts.TrackConflicts, parzzley.aspect.conflicts.ResolveConflictsByHint,
                  parzzley.aspect.remove.DetectRemoval, parzzley.aspect.remove.DefaultRemoveDirs):
    """
    Default behavior for a plain synchronization.
    """

    def __init__(self):
        DefaultBase.__init__(self)
        parzzley.aspect.update.DefaultUpdateItems.__init__(self)
        parzzley.aspect.conflicts.DetectTypeConflicts.__init__(self)
        parzzley.aspect.conflicts.TrackConflicts.__init__(self)
        parzzley.aspect.conflicts.ResolveConflictsByHint.__init__(self)
        parzzley.aspect.remove.DetectRemoval.__init__(self)
        parzzley.aspect.remove.DefaultRemoveDirs.__init__(self)


class PullAndPurgeSyncSource(DefaultBase):
    """
    Default behavior for a source filesystem in a pull-and-purge configuration.
    """

    @parzzley.aspect.hook("defaultupdate", "", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_master_fs()
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.File)
    @parzzley.aspect.execute_only_if_not_update_set_skipped()
    def ppsyncsource_removefromsource(self, ctx, filesystem):
        """
        Removes the file in the source filesystem.
        """
        ctx.delete_file(filesystem, ctx.path)


class PullAndPurgeSyncSink(DefaultBaseBare, parzzley.aspect.update.DefaultUpdateItems,
                           parzzley.aspect.remove.CleanupTrashBin):
    """
    Default behavior for a sink filesystem in a pull-and-purge configuration.
    """

    def __init__(self):
        DefaultBaseBare.__init__(self)
        parzzley.aspect.update.DefaultUpdateItems.__init__(self)
        parzzley.aspect.remove.CleanupTrashBin.__init__(self)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def ppsyncsink_electifnowhereelse(self, ctx, filesystem):
        """
        Elects the sink filesystem if the item exists here ...
        - by a minimal key, if it is a file, so it gets elected if there are no others
        - by a maximum key, if it is a directory, so the sync can go deeper
        """
        if ctx.getinfo_current_exists(filesystem, ctx.path):
            key = sys.maxsize \
                if (ctx.getinfo_current_ftype(filesystem, ctx.path) == parzzley.syncengine.common.EntryType.Directory) \
                else -1
            ctx.promote_master_filesystem(filesystem, key)

    @parzzley.aspect.hook("", "", "defaultupdate", event=parzzley.syncengine.common.SyncEvent.UpdateItem_CheckConflicts)
    @parzzley.aspect.execute_only_if_not_update_set_skipped()
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.File)
    def ppsyncsink_renameexistingtonew(self, ctx, filesystem):
        """
        Renames an already existing entry to some new name.
        """
        _p = ctx.path
        i = 1
        _pd = os.path.dirname(ctx.path)
        _pb = os.path.basename(ctx.path)
        _pi = _pb.rfind(".")
        rename = False
        while filesystem.exists(_p):
            rename = True
            if _pi > 0:  # sic!
                _p = "{pd}/{pb1}.{i}.{pb2}".format(pd=_pd, pb1=_pb[:_pi], i=i, pb2=_pb[_pi + 1:])
            else:
                _p = ctx.path + "." + str(i)
            i += 1
        if rename:
            filesystem.move(ctx.path, _p)
            ctx.setinfo_removefile(filesystem, ctx.path)
            # noinspection PyProtectedMember
            ctx.syncglobaldata.changed_flag = True
