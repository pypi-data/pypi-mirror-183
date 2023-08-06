# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef
import parzzley.filesystem.local


@parzzley.gui.apidef.registerfilesystemhelper(parzzley.filesystem.local.LocalFilesystem)
class LocalFilesystemGuiCreateHelper:

    def __init__(self):
        self.label = tr("local filesystem")

    # noinspection PyUnusedLocal
    def configfs(self, entry, sync):
        path = parzzley.gui.apidef.userfeedback.filesystemdialog(
            fstype="directory", question=tr("Please specify the root directory."))
        if path:
            entry.params["path"] = path
            return True
