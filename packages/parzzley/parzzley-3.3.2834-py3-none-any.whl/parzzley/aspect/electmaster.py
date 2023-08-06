# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.syncengine.common


class ElectMasterFileByMtime(parzzley.aspect.abstractaspect.Aspect):
    """
    Elects a master file by mtime. Default master election strategy for files.
    Part of parzzley.aspect.defaults.DefaultBase.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def electfilebymtime(self, ctx, filesystem):
        """
        Returns the mtime of this entry as election key.
        """
        if ctx.getinfo_current_exists(filesystem, ctx.path):
            ftype = ctx.getinfo_current_ftype(filesystem, ctx.path)
            if ftype and ftype != parzzley.syncengine.common.EntryType.Link:
                mtime = ctx.getinfo_current_mtime(filesystem, ctx.path)
                ctx.promote_master_filesystem(filesystem, mtime.timestamp())


class ElectMasterLinkByTargetHistory(parzzley.aspect.abstractaspect.Aspect):
    """
    Elects a master link by changes in history. Default master election strategy for links.
    Part of parzzley.aspect.defaults.DefaultBase.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def electlinkbyparam(self, ctx, filesystem):
        """
        Returns 0 if the link remained unchanged since last sync, or 1 otherwise as election key.
        """
        paramc = ctx.getinfo_current_param(filesystem, ctx.path)
        paraml = ctx.getinfo_lastrun_param(filesystem, ctx.path)
        ctx.promote_master_filesystem(filesystem, -9999 if paramc == paraml else 1)
