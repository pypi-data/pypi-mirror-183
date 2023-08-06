# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import os

import parzzley.aspect.abstractaspect
import parzzley.aspect.update
import parzzley.config.configpiece
import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.common


class DetectRemoval(parzzley.aspect.abstractaspect.Aspect):
    """
    Detects removed entries.
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    @staticmethod
    def _mtimes_equal(t1, t2, precise):
        if precise:
            return t1 == t2
        else:
            if (t1 is None) or (t2 is None):
                return False
            else:
                return abs((t1-t2).total_seconds()) < 1

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def detectremoval_elect(self, ctx, filesystem):
        """
        Detects if an entry is to be removed and if so, returns the current time as election key.
        """
        if not ctx.getinfo_current_exists(filesystem, ctx.path):  # if it does not exist now
            if ctx.getinfo_lastrun_exists(filesystem, ctx.path):  # ... and if it existed before
                changedonotherplaces = False
                for _fs in ctx.sync.filesystems:
                    precise = _fs.is_mtime_precision_fine() and filesystem.is_mtime_precision_fine()
                    if filesystem != _fs and ctx.getinfo_current_exists(_fs, ctx.path):
                        if ctx.getinfo_current_ftype(_fs, ctx.path) == parzzley.syncengine.common.EntryType.Directory:
                            return
                        amtime = ctx.getinfo_current_mtime(_fs, ctx.path)
                        aparam = ctx.getinfo_current_param(_fs, ctx.path)
                        if ctx.getinfo_lastrun_exists(_fs, ctx.path):
                            lmtime = ctx.getinfo_lastrun_mtime(_fs, ctx.path)
                            lparam = ctx.getinfo_lastrun_param(_fs, ctx.path)
                            if (not DetectRemoval._mtimes_equal(lmtime, amtime, precise)) or lparam != aparam:
                                changedonotherplaces = True
                                break
                        else:
                            changedonotherplaces = True
                            break
                if not changedonotherplaces:
                    ctx.promote_master_filesystem(filesystem, datetime.datetime.now().timestamp())


class DefaultRemoveDirs(parzzley.aspect.abstractaspect.Aspect):
    """
    Removes directories via the filesystem.
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_NotExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.Directory)
    def defaultremovedirs_removedir(self, ctx, filesystem):
        """
        Removes a directory (recursively or safely) in the filesystem.
        """
        ctx.delete_directory(filesystem, ctx.path, recursive=True)


class RemoveOrphanedDirs(parzzley.aspect.abstractaspect.Aspect):
    """
    Removes empty orphaned directories.
    Part of parzzley.aspect.remove.DefaultRemove and parzzley.aspect.remove.TrashRemove.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def check_orphaned_dirs(self, ctx, filesystem):
        if not ctx.getinfo_current_exists(filesystem, ctx.path) and ctx.getinfo_lastrun_exists(filesystem, ctx.path):
            ctx.is_orphaned_dir = True

    @parzzley.aspect.hook("check_orphaned_dirs", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def remove_orphaned_dirs(self, ctx, filesystem):
        """
        Removes a directory in the filesystem if it is empty and was removed in another filesystem.
        """
        if getattr(ctx, "is_orphaned_dir", False) and filesystem.exists(ctx.path) \
                and len(filesystem.listdir(ctx.path)) == 0:
            ctx.delete_directory(filesystem, ctx.path, recursive=False)


# noinspection PyProtectedMember
class CleanupTrashBin(parzzley.aspect.abstractaspect.Aspect):
    """
    Cleans up the trash bin.
    Part of parzzley.aspect.remove.DefaultRemove and parzzley.aspect.remove.TrashRemove.
    """

    def __init__(self, trashdelay="7d"):
        super().__init__()
        self.trashdelay = parzzley.config.configpiece.gettimedelta(trashdelay)

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def cleanup_init(self, ctx, filesystem):
        """
        Some initialization.
        """
        if not hasattr(ctx.syncglobaldata, "_deleted_items_storage"):
            ctx.syncglobaldata._deleted_items_storage = parzzley.runtime.datastorage.get_storage_department(
                ctx, "deleted_items", scope=parzzley.runtime.datastorage.StorageScope.SHARED,
                location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME)
            ctx.syncglobaldata._deleted_items_trashtime_storage = parzzley.runtime.datastorage.get_storage_department(
                ctx, "deleted_items_trashtime", scope=parzzley.runtime.datastorage.StorageScope.SHARED,
                location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def cleanup_trashbin(self, ctx, filesystem):
        """
        Cleans up files in the trashbin control directory that fulfill certain conditions.
        """
        deleted_items_fs = ctx.syncglobaldata._deleted_items_storage.get_filesystem(filesystem=filesystem)
        if ctx.path == "":
            ctx.log(verb="begin cleaning up the trash bin", severity=parzzley.logger.Severity.DEBUG)

            def helper1(ppath):
                if deleted_items_fs.exists(ppath):
                    for x in deleted_items_fs.listdir(ppath):
                        px = ppath + "/" + x
                        fxtype = deleted_items_fs.getftype(px)
                        if fxtype == parzzley.syncengine.common.EntryType.Directory:
                            helper1(px)
                            try:
                                deleted_items_fs.removedir(px, recursive=False)
                            except OSError:
                                pass
                        else:
                            remove = True
                            strashtime = ctx.syncglobaldata._deleted_items_trashtime_storage.get_value_string(
                                filesystem=filesystem, path=px, throwonnotexists=False)
                            if strashtime:
                                trashtime = datetime.datetime.fromtimestamp(int(strashtime))
                                if datetime.datetime.now() - trashtime < self.trashdelay:
                                    remove = False
                            if remove:
                                if fxtype == parzzley.syncengine.common.EntryType.Link:
                                    deleted_items_fs.removelink(px)
                                else:
                                    deleted_items_fs.removefile(px)
                                ctx.logremove(filesystem, px, verb="purged from trash", comment="on "+filesystem.name)

            def helper2(ppath):
                for x in ctx.syncglobaldata._deleted_items_trashtime_storage.list_path(path=ppath,
                                                                                       filesystem=filesystem):
                    px = ppath + "/" + x
                    if deleted_items_fs.exists(px):
                        helper2(px)
                    else:
                        ctx.syncglobaldata._deleted_items_trashtime_storage.remove_value(path=px,
                                                                                         filesystem=filesystem,
                                                                                         recursive=True,
                                                                                         throwonnotexists=False)

            helper1("")
            helper2("")


class DefaultRemove(RemoveOrphanedDirs, CleanupTrashBin):
    """
    Default removal strategy without a trashbin.
    """

    def __init__(self):
        RemoveOrphanedDirs.__init__(self)
        CleanupTrashBin.__init__(self)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_NotExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.Link,
                                                       parzzley.syncengine.common.EntryType.File)
    def defaultremove_file_link(self, ctx, filesystem):
        """
        Removes the file or link from the filesystem.
        """
        ftype = ctx.getinfo_current_ftype(filesystem, ctx.path)
        if ftype == parzzley.syncengine.common.EntryType.Link:
            ctx.delete_link(filesystem, ctx.path)
        else:
            ctx.delete_file(filesystem, ctx.path)
        ctx.logremove(filesystem, ctx.path, comment="on "+filesystem.name)


class TrashRemove(RemoveOrphanedDirs, CleanupTrashBin):
    """
    Removal strategy with a trashbin.
    """

    def __init__(self, trashdelay="7d"):
        RemoveOrphanedDirs.__init__(self)
        CleanupTrashBin.__init__(self, trashdelay=trashdelay)

    # noinspection PyProtectedMember
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_NotExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.Link,
                                                       parzzley.syncengine.common.EntryType.File)
    def trashremove_file_link(self, ctx, filesystem):
        """
        Moves a file or link to the trash bin.
        """
        deleted_items_fs = ctx.syncglobaldata._deleted_items_storage.get_filesystem(filesystem=filesystem)
        i = 0
        drelpath = ctx.path
        while deleted_items_fs.exists(drelpath):
            drelpath = ctx.path + ".." + str(i)
            i += 1
        deleted_items_fs.createdirs(os.path.dirname(drelpath))
        ts = str(int(datetime.datetime.now().timestamp()))
        ctx.syncglobaldata._deleted_items_trashtime_storage.set_value(path=drelpath, filesystem=filesystem, value=ts)
        filesystem.move(ctx.path, deleted_items_fs.translate_path(drelpath, filesystem))
        ctx.setinfo_removefile(filesystem, ctx.path)
        ctx.logremove(filesystem, ctx.path, verb="trashed", comment="on "+filesystem.name,
                      severity=parzzley.logger.Severity.MOREIMPORTANT)
        ctx.syncglobaldata.changed_flag = True
