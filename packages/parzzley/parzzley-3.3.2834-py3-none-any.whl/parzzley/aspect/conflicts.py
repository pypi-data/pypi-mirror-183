# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import parzzley.aspect.abstractaspect
import parzzley.filesystem.abstractfilesystem
import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.common


class DetectTypeConflicts(parzzley.aspect.abstractaspect.Aspect):
    """
    Detects type conflicts between two filesystems (file vs directory, for example).
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_CheckConflicts)
    @parzzley.aspect.execute_only_for_non_master_fs()
    def detect_type_conflict(self, ctx, filesystem):
        """
        Detects a type conflict to master.
        """
        t1 = ctx.getinfo_current_ftype(filesystem, ctx.path)
        t2 = ctx.getinfo_current_ftype(ctx.masterfs, ctx.path)
        if t1 is not None and t2 is not None and t1 != t2:
            ctx.add_conflict(filesystem, "by item type")


# noinspection PyProtectedMember
class TrackConflicts(parzzley.aspect.abstractaspect.Aspect):
    """
    Tracks conflict for handling outside of Parzzley (interactively in a gui for example).
    
    For a conflict in file p/f in a sync task t, a control file `conflicts/t/p/f`
    is created. The conflict can be resolved outside of Parzzley in an arbitrary way by modifying this
    file in a certain way (you find examples somewhere in the Parzzley sources).
    
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def prepare_trackconflicts(self, ctx, filesystem):
        """
        Prepares stuff.
        """
        if not hasattr(ctx.syncglobaldata, "_trackconflicts_paths"):
            ctx.syncglobaldata._trackconflicts_paths = []
            ctx.syncglobaldata._conflicts_storage = parzzley.runtime.datastorage.get_storage_department(
                ctx, "conflicts", location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
                scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_SkippedDueConflicts)
    def trackconflicts_trackskipped_skipconflict(self, ctx, filesystem):
        """
        Stores information about the conflict for resolving.
        """
        conflictsfs = ctx.syncglobaldata._conflicts_storage.get_filesystem(filesystem=filesystem)
        confdpath = os.path.dirname(ctx.path)
        conffpath = confdpath + "/" + os.path.basename(ctx.path)
        conflictsfs.createdirs(confdpath)
        if conflictsfs.exists(conffpath):
            conflictsfs.removefile(conffpath)
        lst = [ctx.masterfs] + [x for x in ctx.get_conflicts()[0]
                                if isinstance(x, parzzley.filesystem.abstractfilesystem.Filesystem)]
        conflictsfs.writetofile(conffpath, "\n".join([xl.name for xl in lst]).encode())
        ctx.syncglobaldata._trackconflicts_paths.append(ctx.path)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.EndSync)
    def cleanup_conflicts_dir(self, ctx, filesystem):
        """
        Cleans up old entries.
        """
        conflictsfs = ctx.syncglobaldata._conflicts_storage.get_filesystem(filesystem=filesystem)

        def _helper(rpath):
            for x in conflictsfs.listdir(rpath):
                xrpath = rpath + "/" + x
                xrftype = conflictsfs.getftype(xrpath)
                if xrftype == parzzley.syncengine.common.EntryType.File:
                    if xrpath not in ctx.syncglobaldata._trackconflicts_paths:
                        conflictsfs.removefile(xrpath)
                elif xrftype == parzzley.syncengine.common.EntryType.Directory:
                    _helper(xrpath)
            try:
                conflictsfs.removedir(rpath, recursive=False)
            except OSError:
                pass
        if conflictsfs.exists(""):
            _helper("")


class ResolveConflictsByHint(parzzley.aspect.abstractaspect.Aspect):
    """
    Resolve conflicts together with TrackConflicts.
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    # noinspection PyProtectedMember
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ResolveConflicts)
    def resolveconflicts_byhint(self, ctx, filesystem):
        """
        Resolves a type conflict by a conflict resolution hint stored in the control files.
        """
        conflictsfs = ctx.syncglobaldata._conflicts_storage.get_filesystem(filesystem=filesystem)
        if conflictsfs.getftype(ctx.path) == parzzley.syncengine.common.EntryType.File:
            lines = [x for x in [x.strip() for x in conflictsfs.readfromfile(ctx.path).decode().split("\n")] if x != ""]
            if len(lines) < 1:
                ctx.log(verb="Error", comment="unable to interpret conflict resolution info in '{0}'.".format(
                    conflictsfs.getfulllocalpathorfallback(ctx.path)), symbol="E",
                        severity=parzzley.logger.Severity.ERROR)
            elif len(lines) == 1:  # actually resolved
                nfsname = lines[0]
                for _fs in ctx.sync.filesystems:
                    if _fs.name == nfsname:
                        ctx.masterfs = _fs
                        while ctx.get_conflicts():
                            ctx.remove_conflict(0)
                        ctx.log(verb="conflict resolved", subject=ctx.path, comment="using " + nfsname,
                                severity=parzzley.logger.Severity.INFO)
                        return
                ctx.log(verb="Error", comment="unable to find name '{0}' in conflict resolution info '{1}'."
                        .format(nfsname, conflictsfs.getfulllocalpathorfallback(ctx.path)), symbol="E",
                        severity=parzzley.logger.Severity.ERROR)
