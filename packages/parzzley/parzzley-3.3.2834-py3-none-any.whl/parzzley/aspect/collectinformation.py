# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.syncengine.common


class CollectInformation(parzzley.aspect.abstractaspect.Aspect):
    """
    Used for populating the `._filelists_curr` lists.
    """

    # noinspection PyProtectedMember
    @parzzley.aspect.hook("applypathacceptor", "collectinfo", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_BeforeElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def collectinformation_collectinfo(self, ctx, filesystem):
        """
        Collects information (type, size, ...) for this entry from the filesystem and stores it to _filelists_curr.
        """
        ftype = filesystem.getftype(ctx.path)
        if ftype:
            if ftype == parzzley.syncengine.common.EntryType.Link:
                param = filesystem.getlinktarget(ctx.path)
                size = None
                mtime = None
            else:
                mtime = filesystem.getmtime(ctx.path)
                size = filesystem.getsize(ctx.path)
                param = None
            ctx._filelists_curr[filesystem].foundfile(ctx.path, ftype, size, mtime, param)
        else:
            ctx._filelists_curr[filesystem].notfoundfile(ctx.path)
