# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import getpass

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef
import parzzley.filesystem.sshfs


@parzzley.gui.apidef.registerfilesystemhelper(parzzley.filesystem.sshfs.SshfsFilesystem)
class SshFilesystemGuiCreateHelper:

    def __init__(self):
        self.label = tr("ssh filesystem")

    # noinspection PyUnusedLocal
    def configfs(self, entry, sync):
        host = parzzley.gui.apidef.userfeedback.inputdialog(tr("Please specify the destination machine hostname."),
                                                           "localhost")
        if host is None:
            return
        entry.params["port"] = "22"
        user = parzzley.gui.apidef.userfeedback.inputdialog(tr("Please specify the ssh user name."), getpass.getuser())
        if user is None:
            return
        entry.params["sshtarget"] = user + "@" + host
        path = parzzley.gui.apidef.userfeedback.inputdialog(tr("Please specify the filesystem path on the destination"
                                                              " machine."), f"/home/{user}")
        if path is None:
            return
        entry.params["path"] = path
        parzzley.gui.apidef.userfeedback.messagedialog(tr(
            "Be aware that ssh filesystems will only work if the destination is a known host to ssh and the ssh "
            "program can connect without doubts.\n\nIt will also need an 'ssh identity file' for it as well (search "
            "the internet for more info).\n\nPlease choose one in the next dialog."))
        idfile = parzzley.gui.apidef.userfeedback.filesystemdialog(fstype="file", startpath=os.path.expanduser("~"),
                                                                  question=tr("Please choose an ssh identity file."))
        if (not idfile) or len(idfile) == 0:
            return
        entry.params["idfile"] = idfile
        return True
