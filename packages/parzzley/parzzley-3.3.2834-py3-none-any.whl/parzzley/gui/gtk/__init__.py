# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import typing as t

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gtk


mydir = os.path.dirname(__file__)


class EntryDialog(Gtk.MessageDialog):

    def __init__(self, is_multiline=False, **kwargs):
        if is_multiline:
            widget = Gtk.ScrolledWindow(width_request=450, height_request=400)
            textview = Gtk.TextView(parent=widget)
            self.__entry = textview.props.buffer = Gtk.TextBuffer()
        else:
            widget = self.__entry = Gtk.Entry(width_request=250)
        super().__init__(**kwargs, buttons=Gtk.ButtonsType.OK_CANCEL)
        widget.show_all()
        self.get_content_area().add(widget)

    @GObject.Property(type=str)
    def entry_text(self):
        return self.__entry.props.text

    @entry_text.setter
    def entry_text(self, text):
        self.__entry.props.text = text

    def run_and_get_entry_text(self):
        if self.run() == Gtk.ResponseType.OK:
            return self.entry_text


def popover_menu(actions: t.List[t.Tuple[str, t.Callable[[], None]]], align_to: 'Gtk.Widget') -> None:
    def wrapx(fct):
        def efct(*_):
            return fct()
        return efct
    popover = Gtk.PopoverMenu()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, parent=popover)
    for actionlbl, actionfct in actions:
        btn = Gtk.ModelButton(text=actionlbl, parent=box)
        btn.connect("clicked", wrapx(actionfct))
    box.show_all()
    popover.props.relative_to = align_to
    popover.popup()


_loaded_css = set()


def load_css(path: str) -> None:
    path = os.path.abspath(path)
    if path not in _loaded_css:
        _loaded_css.add(path)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(path)
        context = Gtk.StyleContext()
        context.add_provider_for_screen(Gdk.Screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


def load_common_css() -> None:
    load_css(f"{mydir}/gtkgui.css")


class ParzzleyGtkBuilder(Gtk.Builder):

    def __init__(self):
        super().__init__(translation_domain="parzzley")
