# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Helper class for user feedback dialogs.
"""

import datetime
import typing as t

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.gui.gtk


class UserFeedbackController:

    def __init__(self, owner):
        self.__owner = owner

    def messagedialog(self, message: str, buttons: t.Optional[t.List[str]] = None) -> int:
        """
        Shows a message dialog to the user and returns the index of the selected button.

        :param message: The message text to show.
        :param buttons: The buttons to offer.
        """
        if buttons is None:
            buttons = [tr("OK")]
        dlg = Gtk.MessageDialog(text=message, deletable=False, parent=self.__owner)
        buttonbox = Gtk.ButtonBox(layout_style=Gtk.ButtonBoxStyle.EXPAND, margin=8)
        def get_button_handler(i):
            def handler(*_):
                dlg.response(i)
            return handler
        for ibuttonlbl, buttonlbl in reversed(list(enumerate(buttons))):
            btn = Gtk.Button(label=buttonlbl, parent=buttonbox)
            btn.connect("clicked", get_button_handler(ibuttonlbl))
        dlg.get_content_area().add(buttonbox)
        buttonbox.show_all()
        answer = dlg.run()
        dlg.destroy()
        return answer

    def inputdialog(self, question: str, defaultanswer: str = "") -> t.Optional[str]:
        """
        Shows an input dialog to the user and returns the entered text (or :samp:`None` when cancelled).

        :param question: The question text to show.
        :param defaultanswer: The default answer text that is written to the text field when showing.
        """
        dlg = parzzley.gui.gtk.EntryDialog(text=question, entry_text=defaultanswer, parent=self.__owner)
        answer = dlg.run_and_get_entry_text()
        dlg.destroy()
        return answer

    def choicedialog(self, question: str, choices: t.List[str]) -> t.Optional[int]:
        """
        Shows a choice dialog to the user and returns the selected item (or :samp:`None` when cancelled).

        :param question: The question text to show.
        :param choices: The list of choices the user has to select from.
        """
        dlg = Gtk.MessageDialog(text=question, deletable=False, buttons=Gtk.ButtonsType.CANCEL, parent=self.__owner)
        buttonbox = Gtk.ButtonBox(orientation=Gtk.Orientation.VERTICAL)
        def get_button_handler(i):
            def handler(*_):
                dlg.response(i)
            return handler
        for ichoice, choice in enumerate(choices):
            btn = Gtk.Button(label=choice, parent=buttonbox)
            btn.connect("clicked", get_button_handler(ichoice))
        dlg.get_content_area().add(buttonbox)
        buttonbox.show_all()
        answer = dlg.run()
        dlg.destroy()
        if answer != Gtk.ResponseType.CANCEL:
            return answer

    def multilineinputdialog(self, question: str, defaultanswer: str = "") -> t.Optional[str]:
        """
        Like :py:meth:`inputdialog` but multi-line capable.

        :param question: The question text to show.
        :param defaultanswer: The default answer text that is written to the text field when showing.
        """
        dlg = parzzley.gui.gtk.EntryDialog(text=question, entry_text=defaultanswer, is_multiline=True,
                                          parent=self.__owner)
        answer = dlg.run_and_get_entry_text()
        dlg.destroy()
        return answer

    def filesystemdialog(self, fstype: str = "file", question: str = "",
                         startpath: t.Optional[str] = None) -> t.Optional[str]:
        """
        Shows a file/directory selection dialog to the user and returns the path to the selected item
        (or :samp:`None`).

        :param fstype: The type of filesystem items to select.
        :param question: The question text to show.
        :param startpath: The directory path to start in.
        """
        action = Gtk.FileChooserAction.SELECT_FOLDER if (fstype == "directory") else Gtk.FileChooserAction.OPEN
        dlg = Gtk.FileChooserDialog(title=question, parent=self.__owner, action=action,
                                    buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        if startpath:
            dlg.set_current_folder(startpath)
        response = dlg.run()
        result = dlg.get_filename()
        dlg.destroy()
        if response == Gtk.ResponseType.OK:
            return result
