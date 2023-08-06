# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _disable():
        sync.removeaspect("HighLevelCustomization", everywhere=True)
        return True

    def _enable():
        sync.addaspect("HighLevelCustomization")
        parzzley.gui.apidef.userfeedback.messagedialog(tr("This option allows you to customize the synchronization"
                                                          " behavior by placing '.parzzley.custom.py' script pieces"
                                                          " somewhere in the sync tree. See the documentation for more"
                                                          " details.\n\nFind a sample script in"
                                                          " '_meta/parzzley.custom.py.example' inside the Parzzley"
                                                          " package."))
        return True

    if sync.hasaspect("HighLevelCustomization", everywhere=True):
        return [(10062, tr("Disable high level customization support"), _disable)]
    else:
        return [(10062, tr("Enable high level customization support"), _enable)]
