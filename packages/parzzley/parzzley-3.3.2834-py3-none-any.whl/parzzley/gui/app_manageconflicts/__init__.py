# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
A gui for manually resolving filesystem sync conflicts.
"""

import os
import sys
import typing as t

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.gui.gtk.volumeapp
import parzzley.tools.common


_mydir = os.path.dirname(__file__)


class App(parzzley.gui.gtk.volumeapp.AbstractVolumeApp):

    def __init__(self):
        super().__init__()
        builder = parzzley.gui.gtk.ParzzleyGtkBuilder()
        builder.add_from_file(f"{_mydir}/main.ui")
        self.__allfsnames = []
        self.__store = None
        self._set_body(builder.get_object("mainbody"))
        self.__pnllist = builder.get_object("pnllist")
        self.__pnlnoconflicts = builder.get_object("pnlnoconflicts")
        self.__btnapplydecisions = builder.get_object("btnapplydecisions")
        self.__lstentries = builder.get_object("lstentries")
        self.__btnapplydecisions.connect("clicked", self.__applydecisions)
        self._set_application_title(tr("Parzzley Sync Conflict Manager"))
        self._set_welcome_text(tr("Resolve Parzzley sync conflicts here."
                                  " At first, go to the sync directory you got conflicts in."))
        self._add_action_button(self.__btnapplydecisions)

    class Conflict:

        def __init__(self, path: str, task: str, choices: t.List[str]):
            self.path = path
            self.task = task
            self.choices = choices

    @classmethod
    def __callmanageconflicts(cls, workdir: str, params: t.List[str]) -> t.List[str]:
        os.chdir(workdir)
        r, o = parzzley.tools.common.call(sys.executable,
                                          os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
                                          + "/parzzley_infssync_manageconflicts.py", *params)
        if r != 0:
            print("(just) debug output: " + o)
            return []
        else:
            return [x for x in [y.strip() for y in o.split("\n")] if x != ""]

    @classmethod
    def __listconflicts(cls, workdir) -> t.List['App.Conflict']:
        result = []
        for path in cls.__callmanageconflicts(workdir, ["list"]):
            for task in cls.__callmanageconflicts(workdir, ["gettasks", path]):
                result.append(cls.Conflict(path, task, cls.__callmanageconflicts(workdir, ["getfsnames", task, path])))
        return result

    @classmethod
    def __resolveconflict(cls, workdir, path, task, fsname):
        cls.__callmanageconflicts(workdir, ["resolve", path, task, fsname])

    def __getdecisions(self):
        result = []
        for row in self.__store:
            for ifsname, fsname in enumerate(self.__allfsnames):
                if row[ifsname+3]:
                    result.append((self._dir, row[0], row[1], fsname))
        return result

    def __applydecisions(self, *_):
        for decision in self.__getdecisions():
            self.__resolveconflict(*decision)
        self._populate()

    def _has_unsaved_changes(self):
        return len(self.__getdecisions()) > 0

    def _populate(self):
        super()._populate()
        self.__pnllist.hide()
        self.__pnlnoconflicts.hide()
        self.__btnapplydecisions.hide()
        conflicts = self.__listconflicts(self._dir) if self._dir else []
        self.__allfsnames = []
        for conflict in conflicts:
            for choice in conflict.choices:
                if choice not in self.__allfsnames:
                    self.__allfsnames.append(choice)
        self.__store = Gtk.TreeStore(str, str, bool, *[bool for _ in self.__allfsnames])
        def gettogglehandler(ifsname):
            def ontoggle(_, path):
                for i in range(len(self.__allfsnames) + 1):
                    self.__store[path][i + 2] = False
                self.__store[path][ifsname + 3] = True
            return ontoggle
        self.__lstentries.props.model = self.__store
        for oldcolumn in self.__lstentries.get_columns():
            self.__lstentries.remove_column(oldcolumn)
        self.__lstentries.append_column(Gtk.TreeViewColumn(tr("Path"), Gtk.CellRendererText(), text=0))
        self.__lstentries.append_column(Gtk.TreeViewColumn(tr("Task"), Gtk.CellRendererText(), text=1))
        nulltoggle = Gtk.CellRendererToggle(radio=True)
        nulltoggle.connect("toggled", gettogglehandler(-1))
        self.__lstentries.append_column(Gtk.TreeViewColumn("-", nulltoggle, active=2))
        for iactive, fsname in enumerate(self.__allfsnames):
            fstoggle = Gtk.CellRendererToggle(radio=True)
            fstoggle.connect("toggled", gettogglehandler(iactive))
            self.__lstentries.append_column(Gtk.TreeViewColumn(fsname, fstoggle, active=iactive+3))
        if conflicts:
            self.__pnllist.show()
            self.__btnapplydecisions.show()
            for conflict in conflicts:
                self.__store.append(None,
                                    [conflict.path, conflict.task, True] + [False for _ in self.__allfsnames])
        else:
            self.__pnlnoconflicts.show()


def run():
    App().show()
