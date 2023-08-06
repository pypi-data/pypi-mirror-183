# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.runtime.datastorage
import parzzley.syncengine.common


class VolumePathBreadcrumb(parzzley.aspect.abstractaspect.Aspect):
    """
    Writes a file to the data directory that helps finding the sync volumes after runtime.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def volumepathbreadcrumb_write(self, ctx, filesystem):
        """
        Writes the breadcrumb.
        """
        breadcrumb_storage = parzzley.runtime.datastorage.get_storage_department(
            ctx, "volume_path_breadcrumb", location=parzzley.runtime.datastorage.StorageLocation.SYSTEM,
            scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
        breadcrumb_storage.set_value(filesystem.getfulllocalpath("/"), path=filesystem.name)
