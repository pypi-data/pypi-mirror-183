# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.syncengine.common


class DefaultIteration(parzzley.aspect.abstractaspect.Aspect):
    """
    Lists child elements via the filesystem.
    Part of parzzley.aspect.defaults.DefaultBase.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_ListDir)
    def defaultiteration_listdir(self, ctx, filesystem):
        """
        Adds all the child entries to the list (as returned by the underlying filesystem).
        """
        if filesystem.getftype(ctx.path) == parzzley.syncengine.common.EntryType.Directory:
            ctx.entrylist.update(filesystem.listdir(ctx.path))
