# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

from parzzley.gui.helpers import tr
import parzzley.gui
import parzzley.gui.apidef


# noinspection PyUnusedLocal
@parzzley.gui.apidef.registerchangeguide()
def changeguides(cfg, sync):

    def _addacceptor():
        t = parzzley.gui.apidef.userfeedback.inputdialog(tr("Please specify a path acceptor filter as Python expression."
                                                           " The parameter 'path' holds the path, 'fs' the"
                                                           " filesystem."),
                                                        "not (path.endswith('.spam') or path.endswith('.crap'))")
        if t is not None:
            a = sync.addaspect("ApplyPathAcceptor")
            a.params["function"] = t
            return True

    return [(10143, tr("Add path acceptor filter"), _addacceptor)]
