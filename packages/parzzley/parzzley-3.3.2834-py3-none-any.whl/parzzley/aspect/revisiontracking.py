# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import tarfile

import parzzley.aspect.abstractaspect
import parzzley.runtime.datastorage
import parzzley.runtime.returnvalue
import parzzley.syncengine.common


# noinspection PyProtectedMember
class RevisionTracking(parzzley.aspect.abstractaspect.Aspect):
    """
    Keeps all versions of all files that Parzzley has seen into a revision storage in the control directory.
    """

    def __init__(self, number_unarchived_revisions=3, number_revisions_per_archive=20):
        """
        :param number_unarchived_revisions: Number of revisions per file to be stored directly, not inside an archive
                                            file.
        :param number_revisions_per_archive: Number of revisions per file to be stored in one archive, before the next
                                             archive file begins.
        """
        super().__init__()
        self.number_unarchived_revisions = int(number_unarchived_revisions)
        self.number_revisions_per_archive = int(number_revisions_per_archive)

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def revisiontracking_init(self, ctx, filesystem):
        """
        Some initialization.
        """
        if not hasattr(ctx.syncglobaldata, "_revisiontracking_storage"):
            ctx.syncglobaldata._revisiontracking_storage = parzzley.runtime.datastorage.get_storage_department(
                ctx, "content_revisions", location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
                scope=parzzley.runtime.datastorage.StorageScope.SHARED)

    @staticmethod
    def _updatefile_helper(ctx, filesystem, path, number_unarchived_revisions, number_revisions_per_archive):
        if ctx.getinfo_current_ftype(filesystem, path) == parzzley.syncengine.common.EntryType.File:
            rpfs = ctx.syncglobaldata._revisiontracking_storage.get_filesystem(filesystem=filesystem)
            mtime = ctx.getinfo_current_mtime(filesystem, path).strftime("%Y-%m-%d %H.%M.%S.%f")
            rcpath = f"{path}/{mtime}"
            if not rpfs.exists(rcpath):
                rpfs.createdirs(os.path.dirname(rcpath))
                _t, _s = rpfs.copyfile(filesystem.getfulllocalpath(path), rcpath)
                if _t is None:
                    ctx.delete_file(rpfs, rcpath)  # next time...
                    ctx.set_retval(parzzley.runtime.returnvalue.ReturnValue.DIRTY)
                revlroot = f"{rpfs.getfulllocalpath(path)}/"
                for doarchiverev in [x for x in sorted(rpfs.listdir(path))
                                     if ".archive." not in x][:-number_unarchived_revisions]:
                    lastarchive = ([""] + [x for x in sorted(rpfs.listdir(path)) if x.endswith(".archive.tbz2")])[-1]
                    if lastarchive:
                        with tarfile.open(revlroot + lastarchive, "r:bz2") as tf:
                            if len(list(tf.getmembers())) >= number_revisions_per_archive:
                                lastarchive = None
                    if not lastarchive:
                        lastarchive = f"{doarchiverev}.archive.tbz2"
                    tempfs = filesystem.get_control_filesystem("/temp")
                    ftmparch = tempfs.getfulllocalpath(lastarchive)
                    with tarfile.open(ftmparch, "w:bz2") as ntf:
                        if os.path.exists(revlroot + lastarchive):
                            with tarfile.open(revlroot + lastarchive, "r:bz2") as tf:
                                for ox in tf.getmembers():
                                    with tf.extractfile(ox) as cox:
                                        ntf.addfile(ox, cox)
                        nx = ntf.gettarinfo(revlroot + doarchiverev, arcname=doarchiverev)
                        with open(revlroot + doarchiverev, "rb") as nox:
                            ntf.addfile(nx, nox)
                    rpla = f"{path}/{lastarchive}"
                    if rpfs.exists(rpla):
                        rpfs.removefile(rpla)
                    os.rename(ftmparch, revlroot + lastarchive)
                    rpfs.removefile(f"{path}/{doarchiverev}")

    @parzzley.aspect.hook("*metadata", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_AfterUpdate)
    @parzzley.aspect.execute_only_if_not_update_set_skipped()
    def revisiontracking_store1(self, ctx, filesystem):
        """
        Checks if the version with the current mtime of this entry is already stored in the version history, and if not, 
        do so.
        """
        if ctx.existsonmaster:
            return RevisionTracking._updatefile_helper(ctx, filesystem, ctx.path, self.number_unarchived_revisions,
                                                       self.number_revisions_per_archive)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def revisiontracking_store2(self, ctx, filesystem):
        """
        Checks if the version with the current mtime of this entry is already stored in the version history, and if not, 
        do so.
        """
        return RevisionTracking._updatefile_helper(ctx, filesystem, ctx.path, self.number_unarchived_revisions,
                                                   self.number_revisions_per_archive)
