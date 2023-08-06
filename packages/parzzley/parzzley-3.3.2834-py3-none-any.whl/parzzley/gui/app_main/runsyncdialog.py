# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject
from gi.repository import Gtk

from parzzley.gui.helpers import tr


_mydir = os.path.dirname(__file__)


@Gtk.Template.from_file(f"{_mydir}/runsyncdialog.ui")
class RunSyncDialog(Gtk.Dialog):
    __gtype_name__ = "RunSyncDialog"

    bufferlog = Gtk.Template.Child()
    pnlsyncing = Gtk.Template.Child()
    pnlsyncsucceeded = Gtk.Template.Child()
    pnlsyncfailed = Gtk.Template.Child()
    btncancel = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__sync_succeeded = False
        self.__sync_failed = False
        self.__handle_dialogstate()
        self.btncancel.connect("clicked", lambda *_: self.destroy())

    @GObject.Property(type=bool, default=False)
    def sync_succeeded(self):
        return self.__sync_succeeded

    @sync_succeeded.setter
    def sync_succeeded(self, v):
        self.__sync_succeeded = v
        self.__handle_dialogstate()

    @GObject.Property(type=bool, default=False)
    def sync_failed(self):
        return self.__sync_failed

    @sync_failed.setter
    def sync_failed(self, v):
        self.__sync_failed = v
        self.__handle_dialogstate()

    def __handle_dialogstate(self):
        for w in [self.pnlsyncing, self.pnlsyncsucceeded, self.pnlsyncfailed]:
            w.hide()
        self.btncancel.props.label = tr("Close")
        if self.__sync_failed:
            self.pnlsyncfailed.show()
        elif self.__sync_succeeded:
            self.pnlsyncsucceeded.show()
        else:
            self.pnlsyncing.show()
            self.btncancel.props.label = tr("Cancel")

    def append_output(self, txt):
        self.bufferlog.insert(self.bufferlog.get_end_iter(), txt)
