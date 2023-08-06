# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
A gui for manually resolving filesystem sync conflicts.
"""

import abc
import os
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.gui.gtk
import parzzley.gui.helpers


_mydir = os.path.dirname(__file__)


class AbstractVolumeApp:

    def __init__(self):
        builder = parzzley.gui.gtk.ParzzleyGtkBuilder()
        builder.add_from_file(f"{_mydir}/main.ui")
        self.__win = builder.get_object("mainwindow")
        self.__pnlwelcome = builder.get_object("pnlwelcome")
        self.__pnlnotparzzley = builder.get_object("pnlnotparzzley")
        self.__pnlbody = builder.get_object("pnlbody")
        self.__btnopen = builder.get_object("btnopen")
        self.__pnlbuttons = builder.get_object("pnlbuttons")
        self.__lbldirectory = builder.get_object("lbldirectory")
        self.__lblwelcome = builder.get_object("lblwelcome")
        self.__lblwelcomehead = builder.get_object("lblwelcomehead")
        self.__lstentries = builder.get_object("lstentries")
        self.__win.connect("delete_event", self.__handleclose)
        self.__btnopen.connect("clicked", self.__opendirdialog)
        parzzley.gui.gtk.load_common_css()
        self._dir = None
        self._dir_is_valid = False
        self.__apptitle = ""
        self.__welcometext = ""

    def _set_body(self, widget):
        for oldchild in self.__pnlbody.get_children():
            self.__pnlbody.remove(oldchild)
        self.__pnlbody.add(widget)

    def __handleclose(self, *_):
        if not self.__confirm_drop_unsaved(Gtk.main_quit):
            return True

    def __opendirdialog(self, *_):
        def do():
            dialog = Gtk.FileChooserDialog(title=tr("Please find the directory you want to resolve conflicts in. It is"
                                                    " sufficient to find the root directory of your Parzzley volume."),
                                           parent=self.__win, action=Gtk.FileChooserAction.SELECT_FOLDER,
                                           buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                                    Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.__opendir(dialog.get_filename())
            dialog.destroy()
        self.__confirm_drop_unsaved(do)

    def __opendir(self, dirpath):
        self._dir_is_valid = False
        if os.path.isdir(dirpath):
            parzzleydir = parzzley.gui.helpers.find_volume_rootpath(dirpath)
            self._dir = parzzleydir or os.path.abspath(dirpath)
            self._dir_is_valid = bool(parzzleydir)
        else:
            self._dir = None
        self._populate()

    def __confirm_drop_unsaved(self, onconfirmed):
        if self._has_unsaved_changes():
            msgdialog = Gtk.MessageDialog(text=tr("Do you really want to drop the resolution decisions you made"
                                                  " so far?"),
                                          buttons=Gtk.ButtonsType.YES_NO, modal=True, parent=self.__win)
            def responsehandler(_, btn):
                if btn == Gtk.ResponseType.YES:
                    onconfirmed()
                msgdialog.destroy()
            msgdialog.connect("response", responsehandler)
            msgdialog.show()
        else:
            onconfirmed()
            return True

    @abc.abstractmethod
    def _has_unsaved_changes(self):
        pass

    def _set_application_title(self, title):
        self.__apptitle = title
        self._set_welcome_text(self.__welcometext)
        self._populate()

    def _set_welcome_text(self, text):
        self.__welcometext = text
        self.__lblwelcome.props.label = text
        self.__lblwelcomehead.props.label = tr("Welcome to {0}.").format(self.__apptitle)

    def _add_action_button(self, button):
        self.__pnlbuttons.pack_end(button)

    def _populate(self):
        self.__lbldirectory.hide()
        self.__pnlbody.hide()
        self.__pnlwelcome.hide()
        self.__pnlnotparzzley.hide()
        if self._dir:
            self.__win.props.title = f"{os.path.basename(self._dir)} - {self.__apptitle}"
            self.__lbldirectory.props.label = self._dir
            self.__lbldirectory.show()
            if self._dir_is_valid:
                self.__pnlbody.show()
            else:
                self.__pnlnotparzzley.show()
        else:
            self.__win.props.title = self.__apptitle
            self.__pnlwelcome.show()

    def show(self):
        self.__win.show_all()
        self._populate()
        if len(sys.argv) >= 2:
            self.__opendir(sys.argv[1])
        elif parzzley.gui.helpers.find_volume_rootpath(os.getcwd()):
            self.__opendir(os.getcwd())
        Gtk.main()
