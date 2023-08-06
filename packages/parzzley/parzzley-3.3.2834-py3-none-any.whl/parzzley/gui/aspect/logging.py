# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _setinterval():
        lc = [tr("No logging"), tr("Only problems"), tr("Problems & file changes")]
        ilc = parzzley.gui.apidef.userfeedback.choicedialog(tr("Please specify a log level."), lc)
        if ilc is not None:
            if ilc == 0:
                sync.removeaspect("Logging", everywhere=True)
            else:
                if not sync.hasaspect("Logging"):
                    sync.addaspect("Logging")
                p = sync.getaspects("Logging")[0].params
                if ilc == 1:
                    p["logcreate"] = p["logupdate"] = p["logremove"] = "0"
                    p["logproblem"] = "1"
                elif ilc == 2:
                    p["logcreate"] = p["logupdate"] = p["logremove"] = p["logproblem"] = "1"
            return True

    return [(10093, tr("Setup logging"), _setinterval)]
