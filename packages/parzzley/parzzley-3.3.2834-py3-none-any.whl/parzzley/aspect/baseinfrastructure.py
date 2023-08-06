# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.syncengine.common


class BaseInfrastructure(parzzley.aspect.abstractaspect.Aspect):
    """
    Provides very basic infrastructure functionality like the workflow described in parzzley.syncengine.sync.Sync.
    It is implicitly available and must never be added explicitely to a configuration.
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "defaultupdate", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_master_fs_filetype(parzzley.syncengine.common.EntryType.Directory)
    @parzzley.aspect.execute_only_for_master_fs()
    def baseinfrastructure_update_directory(self, ctx, filesystem):
        """
        Triggers the directory synchronization if the item is a directory.
        """
        ctx.sync.sync_directory(ctx.path)
