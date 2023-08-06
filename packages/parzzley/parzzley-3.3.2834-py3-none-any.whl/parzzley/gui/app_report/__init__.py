# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
The Parzzley reporting gui.
"""

import os

from parzzley.gui.helpers import tr
import parzzley.gui.app_report.logpanel
import parzzley.gui.app_report.performancepanel
import parzzley.gui.app_report.timelinepanel
import parzzley.gui.gtk.volumeapp
import parzzley.tools.common


_mydir = os.path.dirname(__file__)


class App(parzzley.gui.gtk.volumeapp.AbstractVolumeApp):

    def __init__(self):
        super().__init__()
        builder = parzzley.gui.gtk.ParzzleyGtkBuilder()
        builder.add_from_file(f"{_mydir}/main.ui")
        self.__pnllog = builder.get_object("pnllog")
        self.__pnltimeline = builder.get_object("pnltimeline")
        self.__pnlperformance = builder.get_object("pnlperformance")
        self.__btnrefresh = builder.get_object("btnrefresh")
        self.__wlog = parzzley.gui.app_report.logpanel.LogPanel()
        self.__wtimeline = parzzley.gui.app_report.timelinepanel.TimelinePanel()
        self.__wperformance = parzzley.gui.app_report.performancepanel.PerformancePanel()
        self.__pnllog.add(self.__wlog)
        self.__pnltimeline.add(self.__wtimeline)
        self.__pnlperformance.add(self.__wperformance)
        self._set_body(builder.get_object("mainbody"))
        self._set_application_title(tr("Parzzley Report Viewer"))
        self._set_welcome_text(tr("At first, go to the Parzzley sync directory you want to see reports for."))
        self._add_action_button(self.__btnrefresh)
        self.__btnrefresh.connect("clicked", lambda *_: self._populate())

    def _has_unsaved_changes(self):
        return False

    def _populate(self):
        super()._populate()
        self.__btnrefresh.props.visible = self._dir_is_valid
        self.__wlog._populate(self._dir)
        self.__wtimeline._populate(self._dir)
        self.__wperformance._populate(self._dir)


def run():
    App().show()
