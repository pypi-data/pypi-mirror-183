# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import parzzley.gui.report


_mydir = os.path.dirname(__file__)


@Gtk.Template.from_file(f"{_mydir}/logpanel.ui")
class LogPanel(Gtk.Box):
    __gtype_name__ = "LogPanel"

    pnllog = Gtk.Template.Child()

    def _populate(self, dirpath):
        for oldchild in self.pnllog.get_children():
            self.pnllog.remove(oldchild)
        if dirpath:
            for session in parzzley.gui.report.try_load_log_from_syncdir(dirpath):
                if len(session.messages) > 0:
                    self.pnllog.add(Gtk.Label(label=session.syncrun))
                    lstmsgs = Gtk.TreeView(headers_visible=False, parent=self.pnllog)
                    lstmsgs.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererText(), text=1, foreground=0))
                    lstmsgs.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererText(), text=2, foreground=0))
                    lstmsgs.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererText(), text=3, foreground=0))
                    lstmsgs.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererText(), text=4, foreground=0))
                    lstmsgs.append_column(Gtk.TreeViewColumn("", Gtk.CellRendererText(), text=5, foreground=0))
                    msgstore = Gtk.TreeStore(str, str, str, str, str, str)
                    for message in session.messages:
                        if message.logmessage.severity <= 2:
                            textcolor = "#adcbc9"
                        elif message.logmessage.severity == 3:
                            textcolor = "#222222"
                        elif message.logmessage.severity == 4:
                            textcolor = "#80651b"
                        elif message.logmessage.severity == 5:
                            textcolor = "#9d1e1e"
                        else:
                            textcolor = "#ff0000"
                        msgstore.append(None, [textcolor, message.time.strftime("%c"), message.logmessage.symbol,
                                               message.logmessage.subject, message.logmessage.verb,
                                               message.logmessage.comment])
                    lstmsgs.props.model = msgstore
                    lstmsgs.get_selection().set_mode(Gtk.SelectionMode.NONE)
            self.pnllog.show_all()
