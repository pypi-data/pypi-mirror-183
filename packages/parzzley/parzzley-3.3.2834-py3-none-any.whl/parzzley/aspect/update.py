# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.runtime.returnvalue
import parzzley.syncengine.common


# noinspection PyProtectedMember
class DefaultUpdateItems(parzzley.aspect.abstractaspect.Aspect):
    """
    Default handling for updating non-directory items (i.e. files, links).
    Part of parzzley.aspect.defaults.DefaultSync.
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("defaultupdateitem_skipidentical_aux", "defaultupdate", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.File,
                                                        parzzley.syncengine.common.EntryType.Link)
    def defaultupdateitem_skipidentical(self, ctx, filesystem):
        """
        Skips an entry if they have identical mtime (or link target, for links) in both filesystems.
        """
        if (getattr(ctx, "skipidentical_counter", 0) + 1) == len(ctx.sync.filesystems):
            ctx.skip_update()

    @parzzley.aspect.hook("", "defaultupdate", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.File,
                                                        parzzley.syncengine.common.EntryType.Link)
    def defaultupdateitem_skipidentical_aux(self, ctx, filesystem):
        dstexists = ctx.getinfo_current_exists(filesystem, ctx.path)
        masterftype = ctx.getinfo_current_ftype(ctx.masterfs, ctx.path)
        if dstexists and ctx.getinfo_current_ftype(filesystem, ctx.path) == masterftype:
            skip = False
            if masterftype == parzzley.syncengine.common.EntryType.File:
                oldsrcexists = ctx.getinfo_lastrun_exists(ctx.masterfs, ctx.path)
                if oldsrcexists:
                    oldsrcmtime = ctx.getinfo_lastrun_mtime(ctx.masterfs, ctx.path)
                else:
                    oldsrcmtime = None
                olddstexists = ctx.getinfo_lastrun_exists(filesystem, ctx.path)
                if olddstexists:
                    olddstmtime = ctx.getinfo_lastrun_mtime(filesystem, ctx.path)
                else:
                    olddstmtime = None
                srcmtime = ctx.getinfo_current_mtime(ctx.masterfs, ctx.path)
                dstmtime = ctx.getinfo_current_mtime(filesystem, ctx.path)
                skip = oldsrcexists and olddstexists and oldsrcmtime == srcmtime and olddstmtime == dstmtime \
                    and ("S+" in ctx.getinfo_lastrun_gettags(ctx.masterfs, ctx.path)) \
                    and ("S+" in ctx.getinfo_lastrun_gettags(filesystem, ctx.path))
            elif masterftype == parzzley.syncengine.common.EntryType.Link:
                dsttgt = ctx.getinfo_current_param(filesystem, ctx.path)
                srctgt = ctx.getinfo_current_param(ctx.masterfs, ctx.path)
                skip = dsttgt == srctgt
            if skip:
                ctx.skipidentical_counter = getattr(ctx, "skipidentical_counter", 0) + 1

    @parzzley.aspect.hook("", "defaultupdate,", "baseinfrastructure_update_directory",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.Directory)
    def resolveconflicts_cleanupbeforenewdir(self, ctx, filesystem):
        """
        Forcefully remove files/links for paths that begin a directory sync (so they must be directories).
        """
        if ctx.had_conflicts():
            ftype = ctx.getinfo_current_ftype(filesystem, ctx.path)
            if ftype == parzzley.syncengine.common.EntryType.Link:
                ctx.delete_link(filesystem, ctx.path)
            elif ftype == parzzley.syncengine.common.EntryType.File:
                ctx.delete_file(filesystem, ctx.path)

    @parzzley.aspect.hook("", "defaultupdate", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_CheckConflicts)
    @parzzley.aspect.execute_only_for_non_master_fs()
    def defaultupdateitem_detectandskipupdateconflict(self, ctx, filesystem):
        """
        Checks if an entry stays in an update conflict (by mtime/param comparisons) and if so, mark and skip the entry.
        """
        conflictreasonstring = "by content"
        masterftype = ctx.getinfo_current_ftype(ctx.masterfs, ctx.path)
        dstexists = ctx.getinfo_current_exists(filesystem, ctx.path)
        if masterftype == parzzley.syncengine.common.EntryType.File:
            if not dstexists:
                return
            oldsrcexists = ctx.getinfo_lastrun_exists(ctx.masterfs, ctx.path)
            olddstexists = ctx.getinfo_lastrun_exists(filesystem, ctx.path)
            if olddstexists:
                olddstmtime = ctx.getinfo_lastrun_mtime(filesystem, ctx.path)
            else:
                olddstmtime = None
            if dstexists:
                dstmtime = ctx.getinfo_current_mtime(filesystem, ctx.path)
            else:
                dstmtime = None
            if oldsrcexists and olddstexists:
                pfstags = ctx.getinfo_lastrun_gettags(filesystem, ctx.path)
                if ("S+" in pfstags) or ("S~" in pfstags):
                    cfstags = ctx.getinfo_lastrun_gettags(ctx.masterfs, ctx.path)
                    if ("S+" in cfstags) or ("S~" in cfstags):
                        if olddstmtime == dstmtime:
                            return
            mastermtime = ctx.getinfo_current_mtime(ctx.masterfs, ctx.path)
            if ctx.getinfo_current_ftype(filesystem, ctx.path) == parzzley.syncengine.common.EntryType.File:
                contentequal = True
                size = -1
                with ctx.masterfs.getinputstream(ctx.path) as st1:
                    with filesystem.getinputstream(ctx.path) as st2:
                        cnt1 = b"x"
                        cnt2 = b"x"
                        while cnt1 and cnt2:
                            cmplen = min(len(cnt1), len(cnt2))
                            if cnt1[:cmplen] == cnt2[:cmplen]:
                                cnt1 = cnt1[cmplen:]
                                cnt2 = cnt2[cmplen:]
                                size += cmplen
                            else:
                                contentequal = False
                                break
                            cnt1 += st1.read(40960)
                            cnt2 += st2.read(40960)
                        contentequal = contentequal and (not cnt1) and (not cnt2)
                if contentequal:
                    ctx._filelists_curr[ctx.masterfs].updatefile(ctx.path, parzzley.syncengine.common.EntryType.File,
                                                                 size, mastermtime, None)
                    ctx._filelists_curr[filesystem].updatefile(ctx.path, parzzley.syncengine.common.EntryType.File, size,
                                                               ctx.getinfo_current_mtime(filesystem, ctx.path), None)
                    ctx._filelists_curr[ctx.masterfs].addtag(ctx.path, "S+")
                    ctx._filelists_curr[filesystem].addtag(ctx.path, "S+")
                    ctx.set_retval(parzzley.runtime.returnvalue.ReturnValue.DIRTY)
                    ctx.mark_update_bad()
                    conflictreasonstring = "temp"
        elif masterftype == parzzley.syncengine.common.EntryType.Link:
            oldsrcexists = ctx.getinfo_lastrun_exists(ctx.masterfs, ctx.path)
            if oldsrcexists:
                oldsrckey = ctx.getinfo_lastrun_param(ctx.masterfs, ctx.path)
            else:
                oldsrckey = None
            olddstexists = ctx.getinfo_lastrun_exists(filesystem, ctx.path)
            if olddstexists:
                olddstkey = ctx.getinfo_lastrun_param(filesystem, ctx.path)
            else:
                olddstkey = None
            if dstexists:
                dstkey = ctx.getinfo_current_param(filesystem, ctx.path)
            else:
                dstkey = None
            if (not dstexists) or (oldsrcexists and olddstexists and oldsrckey == olddstkey and olddstkey == dstkey):
                return
        else:
            return
        ctx.add_conflict(filesystem, conflictreasonstring)

    @parzzley.aspect.hook("", "defaultupdate", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_non_master_fs()
    @parzzley.aspect.execute_only_if_not_update_set_skipped()
    def defaultupdateitem_update(self, ctx, filesystem):
        """
        Updates the entry in the non-master filesystems.
        """
        masterftype = ctx.getinfo_current_ftype(ctx.masterfs, ctx.path)
        if masterftype == parzzley.syncengine.common.EntryType.File:
            srcpath = ctx.masterfs.getfulllocalpath(ctx.path)
            dstexists = ctx.getinfo_current_exists(filesystem, ctx.path)
            expecteddstmtime = ctx.getinfo_current_mtime(ctx.masterfs, ctx.path)
            expecteddstsize = ctx.getinfo_current_size(ctx.masterfs, ctx.path)

            # noinspection PyUnusedLocal
            def _copyverifier(path, tempfile, mtime, size):
                return mtime == expecteddstmtime and size == expecteddstsize
            fmtime, fsize = ctx.write_file(filesystem, srcpath, ctx.path, verifier=_copyverifier,
                                           forcedupdate=ctx.had_conflicts())
            if fmtime is None:  # skipped for this time (maybe due to a dirty copy)
                ctx.logproblem(filesystem, ctx.path, verb="skipped this time")
                # set file metadata on source side back to old known values for avoiding conflicts in subsequent runs...
                fsize = ctx.getinfo_lastrun_size(ctx.masterfs, ctx.path)
                fmtime = ctx.getinfo_lastrun_mtime(ctx.masterfs, ctx.path)
                if fsize is None:
                    ctx.setinfo_removefile(ctx.masterfs, ctx.path)
                else:
                    ctx.setinfo_updatefile(ctx.masterfs, ctx.path, parzzley.syncengine.common.EntryType.File, fsize,
                                           fmtime, None)
                ctx.set_retval(parzzley.runtime.returnvalue.ReturnValue.DIRTY)
                ctx.mark_update_bad()
            else:
                if dstexists:
                    ctx.logupdate(filesystem, ctx.path, comment="on " + filesystem.name)
                else:
                    ctx.logcreate(filesystem, ctx.path, comment="on " + filesystem.name)
                ctx.setinfo_updatefile(ctx.masterfs, ctx.path, parzzley.syncengine.common.EntryType.File, fsize, fmtime,
                                       None)  # same data for master
        elif masterftype == parzzley.syncengine.common.EntryType.Link:
            lnktgt = ctx.masterfs.getlinktarget(ctx.path)
            dstexists = ctx.getinfo_current_exists(filesystem, ctx.path)
            ctx.create_link(filesystem, ctx.path, lnktgt, forcedupdate=ctx.had_conflicts())
            if dstexists:
                ctx.logupdate(filesystem, ctx.path, comment="on " + filesystem.name)
            else:
                ctx.logcreate(filesystem, ctx.path, comment="on " + filesystem.name)
