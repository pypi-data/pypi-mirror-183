# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.gui.report


_mydir = os.path.dirname(__file__)


@Gtk.Template.from_file(f"{_mydir}/performancepanel.ui")
class PerformancePanel(Gtk.Box):
    __gtype_name__ = "PerformancePanel"

    edtsynctask = Gtk.Template.Child()
    edtsyncrun = Gtk.Template.Child()
    edteventhandler = Gtk.Template.Child()
    edtfilesystem = Gtk.Template.Child()
    edtpath = Gtk.Template.Child()
    edtaxish = Gtk.Template.Child()
    edtaxisv = Gtk.Template.Child()
    edtaggregation = Gtk.Template.Child()
    spinner = Gtk.Template.Child()
    tree = Gtk.Template.Child()
    scrollview = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        def mainlooped(fct):
            def mainloopedf(*args):
                GLib.idle_add(fct, *args)
            return mainloopedf
        self.__dir = None
        self.__ignore_loadresults = False
        self.__perfdataloader = parzzley.gui.report.PerformanceData.Loader()
        self.__perfdataloader.add_data_available_changed_handler(mainlooped(self.__fill_form))
        self.__perfdataloader.add_data_available_changed_handler(mainlooped(self.__handle_spinner))
        self.__perfdataloader.add_query_result_available_changed_handler(mainlooped(self.__handle_queryresult))
        self.__perfdataloader.add_query_result_available_changed_handler(mainlooped(self.__handle_spinner))
        self.edtsynctask.connect("changed", self.__loadresults)
        self.edtsyncrun.connect("changed", self.__loadresults)
        self.edteventhandler.connect("changed", self.__loadresults)
        self.edtfilesystem.connect("changed", self.__loadresults)
        self.edtpath.connect("changed", self.__loadresults)
        self.edtaxish.connect("changed", self.__loadresults)
        self.edtaxisv.connect("changed", self.__loadresults)
        self.edtaggregation.connect("changed", self.__loadresults)

    def __handle_queryresult(self, query_result_available):
        for oldcolumn in self.tree.get_columns():
            self.tree.remove_column(oldcolumn)
        self.tree.props.model = None
        if query_result_available:
            query_result = self.__perfdataloader.get_query_result()
            for oldcolumn in self.tree.get_columns():
                self.tree.remove_column(oldcolumn)
            storereport = Gtk.TreeStore(str, *[str for _ in query_result.column_names])
            self.tree.append_column(Gtk.TreeViewColumn(tr("[times in ms]"), Gtk.CellRendererText(), text=0))
            for icolumnname, columnname in enumerate(query_result.column_names):
                self.tree.append_column(
                    Gtk.TreeViewColumn(columnname, Gtk.CellRendererText(xalign=1), text=icolumnname + 1))
            for irow, row in enumerate(query_result.result):
                storereport.append(None, [query_result.row_names[irow], *[f"{v*1000:.3f}" for v in row]])
            self.tree.props.model = storereport

    def __handle_spinner(self, _):
        showspinner = not (self.__perfdataloader.data_available and self.__perfdataloader.query_result_available)
        (self.spinner if showspinner else self.scrollview).show()
        (self.scrollview if showspinner else self.spinner).hide()

    def __fill_form(self, perf_data_available):
        if perf_data_available:
            self.__ignore_loadresults = True
            perfdata = self.__perfdataloader.get_data()
            self.edtsynctask.props.model = storesynctasks = Gtk.TreeStore(str, str)
            storesynctasks.append(None, ["*", ""])
            for synctask in perfdata.synctasks:
                storesynctasks.append(None, [synctask, synctask])
            self.edtsynctask.props.active_id = ""
            self.edtsyncrun.props.model = storesyncruns = Gtk.TreeStore(str, str)
            storesyncruns.append(None, ["*", ""])
            for syncrun in perfdata.syncruns:
                storesyncruns.append(None, [syncrun, syncrun])
            self.edtsyncrun.props.active_id = ""
            self.edteventhandler.props.model = storeeventhandlers = Gtk.TreeStore(str, str)
            storeeventhandlers.append(None, ["*", ""])
            for eventhandler in perfdata.eventhandlers:
                storeeventhandlers.append(None, [eventhandler, eventhandler])
            self.edteventhandler.props.active_id = ""
            self.edtfilesystem.props.model = storefilesystems = Gtk.TreeStore(str, str)
            storefilesystems.append(None, ["*", ""])
            for filesystem in perfdata.filesystems:
                storefilesystems.append(None, [filesystem, filesystem])
            self.edtfilesystem.props.active_id = ""
            self.edtpath.props.text = ".*"
            self.edtaxish.props.model = self.edtaxisv.props.model = storeaxis = Gtk.TreeStore(str, str)
            storeaxis.append(None, [tr("Sync task"), "synctask"])
            storeaxis.append(None, [tr("Sync run"), "syncrun"])
            storeaxis.append(None, [tr("Event handler"), "eventhandler"])
            storeaxis.append(None, [tr("Filesystem"), "filesystem"])
            storeaxis.append(None, [tr("Path"), "path"])
            storeaxis.append(None, [tr("-"), ""])
            self.edtaxish.props.active_id = "filesystem"
            self.edtaxisv.props.active_id = "syncrun"
            self.edtaggregation.props.model = storeaggregation = Gtk.TreeStore(str, str)
            storeaggregation.append(None, [tr("Sum"), "sum"])
            storeaggregation.append(None, [tr("Average"), "average"])
            self.edtaggregation.props.active_id = "sum"
            self.__ignore_loadresults = False
            self.__loadresults()

    def __loadresults(self, *_):
        if self.__ignore_loadresults:
            return
        self.__perfdataloader.query(
            horizontally=self.edtaxish.props.active_id, vertically=self.edtaxisv.props.active_id,
            aggregation=self.edtaggregation.props.active_id, sync=self.edtsynctask.props.active_id,
            syncrun=self.edtsyncrun.props.active_id, eventhandler=self.edteventhandler.props.active_id,
            filesystem=self.edtfilesystem.props.active_id, path=self.edtpath.props.text)

    def _populate(self, dirpath):
        self.__dir = dirpath
        self.__perfdataloader.set_path(dirpath)
