# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.config.configpiece
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _setinterval():
        lsfs = []
        for i, fs in enumerate(sync.filesystems):
            lsfs.append(parzzley.gui.apidef.getfsname(fs, i))
        ifs = parzzley.gui.apidef.userfeedback.choicedialog(
                    tr("Please choose on which filesystem you want to setup the trashbin."), lsfs)
        if ifs is None:
            return
        fs = sync.filesystems[ifs]
        fsname = parzzley.gui.apidef.getfsname(fs, ifs)
        im = parzzley.gui.apidef.userfeedback.messagedialog(tr("Please choose if you want to enable or disable the"
                                                              " trashbin in '{0}'.").format(fsname),
                                                           [tr("enable"), tr("disable")])
        if im == 0:
            interval = None
            while interval is None:
                interval = parzzley.gui.apidef.userfeedback.inputdialog(tr("Please choose a trash-to-cleanup interval"
                                                                          " (e.g. '100h' or '4d')."), "")
                if interval is None:
                    break
                elif interval == "":
                    break
                else:
                    try:
                        parzzley.config.configpiece.gettimedelta(interval)
                    except:
                        interval = None
            if interval is not None:
                if not sync.hasaspect("TrashRemove", fs=ifs):
                    sync.addaspect("TrashRemove", fs=ifs)
                p = sync.getaspects("TrashRemove", fs=ifs)[0].params
                if interval == "":
                    if "trashdelay" in p:
                        p.pop("trashdelay")
                else:
                    p["trashdelay"] = interval
        elif im == 1:
            sync.removeaspect("TrashRemove", fs=ifs)
        return True
    if not sync.hasaspect("DefaultSync"):
        return
    return [(10003, tr("Setup trashbin"), _setinterval)]
