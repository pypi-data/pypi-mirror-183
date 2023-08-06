# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.runtime._project_infos
import parzzley.syncengine.common


class ReadmeFile(parzzley.aspect.abstractaspect.Aspect):
    """
    Writes a readme file into the on-volume Parzzley control directory.
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def readmefile_writereadme(self, ctx, filesystem):
        """
        Writes the readme.
        """
        controlfs = filesystem.get_control_filesystem()
        if not controlfs.exists("README"):
            controlfs.writetofile("README", f"This directory structure is synchronized by Parzzley.\n"
                                            f"Visit {parzzley.runtime._project_infos.homepage_url} for more"
                                            f" information.".encode())
