# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _disable():
        sync.removeaspect("RevisionTracking", everywhere=True)
        return True

    def _enable():
        sync.addaspect("RevisionTracking")
        return True

    if not sync.hasaspect("DefaultSync"):
        return
    if sync.hasaspect("RevisionTracking", everywhere=True):
        return [(10023, tr("Disable revision tracking"), _disable)]
    else:
        return [(10023, tr("Enable revision tracking"), _enable)]
