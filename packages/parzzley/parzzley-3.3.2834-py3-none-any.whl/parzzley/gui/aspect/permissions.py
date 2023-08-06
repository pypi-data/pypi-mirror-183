# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _set():
        lsfs = []
        userfeedback = parzzley.gui.apidef.userfeedback
        for i, fs in enumerate(sync.filesystems):
                lsfs.append(parzzley.gui.apidef.getfsname(fs, i))
        ifs = userfeedback.choicedialog(tr("Please choose on which filesystem you want to force file ownerships and"
                                           " permissions."), lsfs)
        if ifs is None:
            return
        i = userfeedback.messagedialog(tr("Do you want to enable or disable a forced ownership and permission set?"),
                                       [tr("enable"), tr("disable")])
        if i == 0:
            uid = userfeedback.inputdialog(tr("Please specify the owner user (prepend '#' for a uid)."), "#1001")
            if uid is None:
                return
            gid = userfeedback.inputdialog(tr("Please specify the owner group (prepend '#' for a gid)."), "#1001")
            if gid is None:
                return
            af = userfeedback.inputdialog(tr("Please specify a bitmask of permissions to add on each file."), "0")
            if af is None:
                return
            ad = userfeedback.inputdialog(tr("Please specify a bitmask of permissions to add on each directory."), "0")
            if ad is None:
                return
            sf = userfeedback.inputdialog(tr("Please specify a bitmask of permissions to remove on each file."), "0")
            if sf is None:
                return
            sd = userfeedback.inputdialog(tr("Please specify a bitmask of permissions to remove on each directory."),
                                          "0")
            if sd is None:
                return
            sync.removeaspect("ApplyPermissions", fs=ifs)
            a = sync.addaspect("ApplyPermissions", fs=ifs)
            a.params["user"] = uid
            a.params["group"] = gid
            a.params["fileaddperms"] = af
            a.params["diraddperms"] = ad
            a.params["filesubtractperms"] = sf
            a.params["dirsubtractperms"] = sd
            return True
        elif i == 1:
            sync.removeaspect("ApplyPermissions", fs=ifs)
            return True

    return [(10029, tr("Force file ownerships and permissions"), _set)]
