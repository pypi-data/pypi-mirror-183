# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):
    notepad = {}  # used e.g. between _setsinkpre (collecting information) and _setsink (actually executing stuff)

    def _removeall(fct, pre=None):
        def _f():
            if pre is not None:
                if not pre():
                    return False
            for sa in ["PullAndPurgeSyncSink", "PullAndPurgeSyncSource", "TrashRemove", "DefaultSync"]:
                sync.removeaspect(sa, everywhere=True)
            fct()
            return True
        return _f

    def _setdefault():
        sync.addaspect("DefaultSync")
        for fs in list(range(len(sync.filesystems))):
            sync.addaspect("TrashRemove", fs=fs)

    def _setsinkpre():
        lsfs = []
        for i, fs in enumerate(sync.filesystems):
            lsfs.append(parzzley.gui.apidef.getfsname(fs, i))
        ifs = parzzley.gui.apidef.userfeedback.choicedialog(tr("Please choose which filesystem shall be the data sink"
                                                              " (the 'storage place'). The other filesystem will become"
                                                              " the source, which will regularly be pulled and"
                                                              " purged."),
                                                           lsfs)
        if ifs is None:
            return
        notepad["ifs"] = ifs
        return True

    def _setsink():
        ifs = notepad["ifs"]
        for i, fs in enumerate(sync.filesystems):
            if i == ifs:
                sync.addaspect("PullAndPurgeSyncSink", i)
            else:
                sync.addaspect("PullAndPurgeSyncSource", i)

    res = []
    if not sync.hasaspect("DefaultSync"):
        res.append((1, tr("Set major behavior to default"), _removeall(_setdefault)))
    if len(sync.filesystems) == 2 and \
            not (sync.hasaspect("PullAndPurgeSyncSource", fs=0) or sync.hasaspect("PullAndPurgeSyncSink", fs=0)):
        res.append((1, tr("Set major behavior to pull&purge"), _removeall(_setsink, pre=_setsinkpre)))
    return res


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides_readonly(cfg, sync):

    def _set():
        lsfs = []
        for i, fs in enumerate(sync.filesystems):
            lsfs.append(parzzley.gui.apidef.getfsname(fs, i))
        ifs = parzzley.gui.apidef.userfeedback.choicedialog(tr("Please choose which filesystem is the"
                                                              " read-only one."), lsfs)
        if ifs is None:
            return
        sync.filesystems[ifs].params["isreadonly"] = "1"
        return True

    def _unset():
        for fs in sync.filesystems:
            if "isreadonly" in fs.params:
                fs.params.pop("isreadonly")
        return True

    if [x for x in sync.filesystems if "isreadonly" in x.params]:
        return [(20025, tr("Unset replication mode for a read-only filesystem"), _unset)]
    else:
        return [(20025, tr("Set to replication mode for a read-only filesystem"), _set)]
