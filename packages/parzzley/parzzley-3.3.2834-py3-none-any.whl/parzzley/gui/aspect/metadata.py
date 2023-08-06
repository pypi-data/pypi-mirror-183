# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _enable():
        lsfs = []
        lfs = []
        for i, fs in enumerate(sync.filesystems):
            if fs.otype == "LocalFilesystem":
                lsfs.append(parzzley.gui.apidef.getfsname(fs, i))
                lfs.append(fs)
        if len(lsfs) == 0:
            parzzley.gui.apidef.userfeedback.messagedialog(tr("You need at least one LocalFilesystem for that feature."))
            return
        elif len(lsfs) == 1:
            ifs = 0
        else:
            ifs = parzzley.gui.apidef.userfeedback.choicedialog(
                        tr("Please choose on which filesystem you want to store the metadata shadow."), lsfs)
            if ifs is None:
                return
        wfs = lfs[ifs]
        for ak in ["MetadataSynchronization", "MetadataSynchronizationWithShadow"]:
            sync.removeaspect(ak, everywhere=True)
        for i, fs in enumerate(sync.filesystems):
            if fs == wfs:
                sync.addaspect("MetadataSynchronizationWithShadow", fs=i)
            else:
                sync.addaspect("MetadataSynchronization", fs=i)
        return True

    def _disable():
        for ak in ["MetadataSynchronization", "MetadataSynchronizationWithShadow"]:
            sync.removeaspect(ak, everywhere=True)
        return True

    try:
        import xattr
    except ImportError:
        xattr = None
    if xattr:
        if sync.hasaspect("MetadataSynchronizationWithShadow", everywhere=True) or \
                    sync.hasaspect("MetadataSynchronization", everywhere=True):
            return [(10099, tr("Disable metadata storage"), _disable)]
        else:
            return [(10099, tr("Enable metadata storage"), _enable)]
