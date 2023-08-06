# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import abc
import os
import re

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.config.config
import parzzley.gui.apidef
import parzzley.gui.app_main.runsyncdialog
import parzzley.gui.gtk
import parzzley.gui.helpers
import parzzley.runtime.datastorage


_mydir = os.path.dirname(__file__)


class ParamConfigNode(Gtk.Button):
    __gtype_name__ = "ParamConfigNode"

    def __init__(self, **kwargs):
        self.__lblkey = Gtk.Label(visible=True, wrap=True, xalign=0)
        self.__lblvalue = Gtk.Label(visible=True, wrap=True, xalign=0)
        super().__init__(**kwargs, halign=Gtk.Align.START)
        lblbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, parent=self)
        self.__lblkey.get_style_context().add_class("configparamkey")
        lblbox.add(self.__lblkey)
        lblbox.add(self.__lblvalue)
        self.__key_text = None

    @GObject.property(type=str)
    def key_label(self):
        return self.__key_text

    @key_label.setter
    def key_label(self, value):
        self.__key_text = value
        self.__lblkey.props.label = f"{value}: "

    @GObject.property(type=str)
    def value_label(self):
        return self.__lblvalue.props.label

    @value_label.setter
    def value_label(self, value):
        self.__lblvalue.props.label = value


class ObjectConfigNode(Gtk.Button):
    __gtype_name__ = "ObjectConfigNode"

    def __init__(self, **kwargs):
        self.__lbl = Gtk.Label(visible=True, wrap=True, xalign=0)
        super().__init__(**kwargs, halign=Gtk.Align.START)
        self.get_style_context().add_class("configblock")
        self.add(self.__lbl)

    @GObject.property(type=str)
    def label(self):
        return self.__lbl.props.label

    @label.setter
    def label(self, value):
        self.__lbl.props.label = value


class ConfigItemListener:

    def reload(self):
        pass

    def add_item(self, config, aligntowidget):
        pass


@Gtk.Template.from_file(f"{_mydir}/configitem.ui")
class ConfigItem(Gtk.Box):
    __gtype_name__ = "ConfigItem"

    lblhead = Gtk.Template.Child()
    toolbar = Gtk.Template.Child()
    pnlbody = Gtk.Template.Child()
    pnlconfigbody = Gtk.Template.Child()
    pnlbodyouter = Gtk.Template.Child()

    def __init__(self, handler: 'ConfigItemHandler', **kwargs):
        super().__init__(**kwargs)
        self.__listeners = []
        self.__handler = handler
        self.set_css_name("configitem")
        parzzley.gui.gtk.load_css(f"{_mydir}/configitem.css")
        self.get_style_context().add_class(self.__handler.get_css_classname())
        self.body_visible = False
        self.refresh()

    @property
    def configobject(self):
        return self.__handler.configobject

    @property
    def body_visible(self):
        return self.pnlbodyouter.props.visible

    @body_visible.setter
    def body_visible(self, v):
        self.pnlbodyouter.props.visible = v

    def add_listener(self, listener):
        self.__listeners.append(listener)

    def _set_showbody_button(self, btn):
        def clickhandler(*_):
            self.body_visible = not self.body_visible
            btn.props.active = self.body_visible
        btn.connect("clicked", clickhandler)

    def _trigger_reload(self):
        for listener in self.__listeners:
            listener.reload()

    def _trigger_add_item(self, config, aligntowidget):
        for listener in self.__listeners:
            listener.add_item(config, aligntowidget)

    def _cleanup(self, toolbar=True, configbody=True, body=True):
        for panel, flag in [(self.toolbar, toolbar), (self.pnlconfigbody, configbody), (self.pnlbody, body)]:
            if flag:
                for oldchild in panel.get_children():
                    panel.remove(oldchild)

    def refresh(self):
        self.lblhead.props.label = self.__handler.get_header_text()
        self.__handler.init_ui(self)


class ConfigItemHandler:

    def __init__(self, configobject):
        self.__configobject = configobject
        self.__configitem = None
        self._rootconfig_cfgfile = None
        self._rootconfig_datadir = None

    def reload(self):
        self.__configitem._trigger_reload()

    @property
    def configobject(self):
        return self.__configobject

    @property
    def configitem(self):
        return self.__configitem

    @abc.abstractmethod
    def get_header_text(self) -> str:
        pass

    @abc.abstractmethod
    def get_css_classname(self) -> str:
        pass

    def _set_root_config(self, cfgfile, datadir):
        self._rootconfig_cfgfile = cfgfile
        self._rootconfig_datadir = datadir

    def init_ui(self, configitem: ConfigItem) -> None:
        self.__configitem = configitem

    @property
    def _toplevel_window(self):
        return self.__configitem.get_toplevel()

    def _ask_and_remove(self, lst, obj):
        confirmdlg = Gtk.MessageDialog(text=tr("Do you really want to remove this item?"),
                                       buttons=Gtk.ButtonsType.YES_NO, modal=True,
                                       parent=self.__configitem.get_toplevel())
        if confirmdlg.run() == Gtk.ResponseType.YES:
            lst.remove(obj)
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()
        confirmdlg.destroy()

    def _edit_param(self, obj, paramkey, paramvalue):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(
            question=tr("Please enter the new parameter value."), defaultanswer=paramvalue)
        if answer is not None:
            obj.params[paramkey] = answer
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()

    def _remove_param(self, obj, paramkey):
        answer = parzzley.gui.apidef.userfeedback.messagedialog(
            message=tr("Do you really want to remove the '{0}' parameter?").format(paramkey),
            buttons=[tr("Yes"), tr("No")])
        if answer == 0:
            obj.params.pop(paramkey)
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()

    def _add_param(self, obj):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(question=tr("Please enter the new parameter name."))
        if answer and (answer not in obj.params):
            obj.params[answer] = ""
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()

    def _change_type(self, obj):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(question=tr("Please enter the new object type name."),
                                                             defaultanswer=obj.otype)
        if answer:
            obj.otype = answer
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()

    def _edit_attr(self, obj, attrname, question):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(question=question,
                                                             defaultanswer=getattr(obj, attrname, ""))
        if answer is not None:
            if answer == "":
                answer = None
            setattr(obj, attrname, answer or None)
            parzzley.gui.helpers.saveconfig(obj.cfg)
            self.reload()

    def _edit_boolattr(self, obj, attrname):
        setattr(obj, attrname, not getattr(obj, attrname, False))
        parzzley.gui.helpers.saveconfig(obj.cfg)
        self.reload()


class SyncTaskConfigItemHandler(ConfigItemHandler):

    def __init__(self, synctask: parzzley.config.config.ParzzleyConfiguration.Sync, **kwargs):
        super().__init__(synctask, **kwargs)

    def get_header_text(self):
        return tr("Sync Task '{0}'").format(self.configobject.name) if self.configobject.name else tr("Sync Task")

    def get_css_classname(self):
        return "synctask"

    def init_ui(self, configitem):
        super().init_ui(configitem)
        self.configitem._cleanup()
        if self.configobject.name:
            btnrun = Gtk.ToolButton(label=tr("Run"), icon_widget=Gtk.Image(stock="gtk-media-play"),
                                    parent=configitem.toolbar)
            btnrun.connect("clicked", self.__do_run)
        btnconfig = Gtk.ToolButton(label=tr("Configure"), icon_widget=Gtk.Image(stock="gtk-preferences"),
                                   parent=configitem.toolbar)
        btnconfig.connect("clicked", self.__do_config)
        btnprefs = Gtk.ToggleToolButton(label=tr("Properties"), icon_widget=Gtk.Image(stock="gtk-index"),
                                        parent=configitem.toolbar)
        configitem._set_showbody_button(btnprefs)
        btnremove = Gtk.ToolButton(label=tr("Remove"), icon_widget=Gtk.Image(stock="gtk-delete"),
                                   parent=configitem.toolbar)
        btnremove.connect("clicked", self.__do_remove)
        if self.configobject.name and len(parzzley.gui.helpers.get_volume_paths_for_sync(
                self.configobject.name, datadir=self._rootconfig_datadir)) > 0:
            btnconflicts = Gtk.ToolButton(label=tr("Resolve conflicts"), icon_widget=Gtk.Image(stock="gtk-clear"),
                                          parent=configitem.toolbar)
            btnconflicts.connect("clicked", self.__do_conflicts)
            btnreport = Gtk.ToolButton(label=tr("Reports"), icon_widget=Gtk.Image(stock="gtk-find"),
                                       parent=configitem.toolbar)
            btnreport.connect("clicked", self.__do_report)
        configitem.toolbar.show_all()
        Gtk.Label(label=tr("Click on one of the nodes below in order to configure it.\n"
                           "Warning: Changes might break your configuration!"), parent=configitem.pnlbody,
                  margin_bottom=10)
        configitem.pnlbody.show_all()
        lblgeneral = ObjectConfigNode(label=tr("General"), parent=configitem.pnlconfigbody)
        lblgeneral.connect("clicked", self.__gethandler_edit_general())
        for paramkey, paramvalue in self.configobject.params.items():
            lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue, parent=configitem.pnlconfigbody,
                                       margin_left=20)
            lblparam.connect("clicked", self.__gethandler_edit_param(paramkey, paramvalue))
        for preparation in self.configobject.preparations:
            lblpreparation = ObjectConfigNode(label=tr("Preparation '{0}'").format(preparation.otype),
                                              parent=configitem.pnlconfigbody)
            lblpreparation.connect("clicked", self.__gethandler_edit_preparation(preparation))
            for paramkey, paramvalue in preparation.params.items():
                lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue, parent=configitem.pnlconfigbody,
                                           margin_left=20)
                lblparam.connect("clicked", self.__gethandler_edit_preparation_param(preparation, paramkey, paramvalue))
        for filesystem in self.configobject.filesystems:
            fsnamequot = tr("Filesystem '{0}' ({1})").format(filesystem.name, filesystem.otype) if filesystem.name \
                else tr("Filesystem ({0})").format(filesystem.otype)
            lblfilesystem = ObjectConfigNode(label=fsnamequot, parent=configitem.pnlconfigbody)
            lblfilesystem.connect("clicked", self.__gethandler_edit_filesystem(filesystem))
            for paramkey, paramvalue in filesystem.params.items():
                lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue, parent=configitem.pnlconfigbody,
                                           margin_left=20)
                lblparam.connect("clicked", self.__gethandler_edit_filesystem_param(filesystem, paramkey, paramvalue))
            for aspect in filesystem.aspects:
                lblaspect = ObjectConfigNode(label=tr("Aspect '{0}'").format(aspect.otype),
                                             parent=configitem.pnlconfigbody, margin_left=20)
                lblaspect.connect("clicked", self.__gethandler_edit_filesystem_aspect(filesystem, aspect))
                for paramkey, paramvalue in aspect.params.items():
                    lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue,
                                               parent=configitem.pnlconfigbody, margin_left=40)
                    lblparam.connect("clicked", self.__gethandler_edit_filesystem_aspect_param(aspect, paramkey,
                                                                                               paramvalue))
        for aspect in self.configobject.aspects:
            lblaspect = ObjectConfigNode(label=tr("Aspect '{0}'").format(aspect.otype), parent=configitem.pnlconfigbody)
            lblaspect.connect("clicked", self.__gethandler_edit_aspect(aspect))
            for paramkey, paramvalue in aspect.params.items():
                lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue, parent=configitem.pnlconfigbody,
                                           margin_left=20)
                lblparam.connect("clicked", self.__gethandler_edit_aspect_param(aspect, paramkey, paramvalue))
        configitem.pnlconfigbody.show_all()

    def __gethandler_edit_general(self):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"), lambda *_: self._add_param(self.configobject)),
                                          (tr("Add aspect"), lambda *_: self._add_aspect(self.configobject.aspects)),
                                          (tr("Add preparation"), lambda *_: self._add_preparation())], btn)
        return handler

    def __gethandler_edit_param(self, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_: self._edit_param(self.configobject, paramkey, paramvalue)),
                                          (tr("Remove"), lambda *_: self._remove_param(self.configobject, paramkey))],
                                         btn)
        return handler

    def __gethandler_edit_preparation(self, preparation):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"), lambda *_: self._add_param(preparation)),
                                          (tr("Change type"), lambda *_: self._change_type(preparation)),
                                          (tr("Remove"), lambda *_: self._remove_preparation(preparation))], btn)
        return handler

    def __gethandler_edit_preparation_param(self, preparation, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_: self._edit_param(preparation, paramkey, paramvalue)),
                                          (tr("Remove"), lambda *_: self._remove_param(preparation, paramkey))], btn)
        return handler

    def __gethandler_edit_filesystem(self, filesystem):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"), lambda *_: self._add_param(filesystem)),
                                          (tr("Change type"), lambda *_: self._change_type(filesystem)),
                                          (tr("Add aspect"), lambda *_: self._add_aspect(filesystem.aspects))], btn)
        return handler

    def __gethandler_edit_filesystem_param(self, filesystem, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_: self._edit_param(filesystem, paramkey, paramvalue)),
                                          (tr("Remove"), lambda *_: self._remove_param(filesystem, paramkey))], btn)
        return handler

    def __gethandler_edit_filesystem_aspect(self, filesystem, aspect):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"), lambda *_: self._add_param(aspect)),
                                          (tr("Change type"), lambda *_: self._change_type(aspect)),
                                          (tr("Remove"), lambda *_: self._remove_aspect(filesystem.aspects, aspect))],
                                         btn)
        return handler

    def __gethandler_edit_filesystem_aspect_param(self, aspect, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_: self._edit_param(aspect, paramkey, paramvalue)),
                                          (tr("Remove"), lambda *_: self._remove_param(aspect, paramkey))], btn)
        return handler

    def __gethandler_edit_aspect(self, aspect):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"), lambda *_: self._add_param(aspect)),
                                          (tr("Change type"), lambda *_: self._change_type(aspect)),
                                          (tr("Remove"),
                                           lambda *_: self._remove_aspect(self.configobject.aspects, aspect))],
                                         btn)
        return handler

    def __gethandler_edit_aspect_param(self, aspect, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_: self._edit_param(aspect, paramkey, paramvalue)),
                                          (tr("Remove"), lambda *_: self._remove_param(aspect, paramkey))], btn)
        return handler

    def _remove_preparation(self, preparation):
        answer = parzzley.gui.apidef.userfeedback.messagedialog(
            message=tr("Do you really want to remove the '{0}' preparation?").format(preparation.otype),
            buttons=[tr("Yes"), tr("No")])
        if answer == 0:
            self.configobject.preparations.remove(preparation)
            parzzley.gui.helpers.saveconfig(self.configobject.cfg)
            self.reload()

    def _remove_aspect(self, parentlist, aspect):
        answer = parzzley.gui.apidef.userfeedback.messagedialog(
            message=tr("Do you really want to remove the '{0}' aspect?").format(aspect.otype),
            buttons=[tr("Yes"), tr("No")])
        if answer == 0:
            parentlist.remove(aspect)
            parzzley.gui.helpers.saveconfig(self.configobject.cfg)
            self.reload()

    def _add_preparation(self):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(question=tr("Please enter the new preparation type name."))
        if answer:
            self.configobject.preparations.append(parzzley.config.config.ParzzleyConfiguration.Preparation(
                self.configobject.cfg, answer))
            parzzley.gui.helpers.saveconfig(self.configobject.cfg)
            self.reload()

    def _add_aspect(self, parentlist):
        answer = parzzley.gui.apidef.userfeedback.inputdialog(question=tr("Please enter the new aspect type name."))
        if answer:
            parentlist.append(parzzley.config.config.ParzzleyConfiguration.Aspect(self.configobject.cfg, answer))
            parzzley.gui.helpers.saveconfig(self.configobject.cfg)
            self.reload()

    def __do_config(self, btn, *_):
        def gethandler(changeguideo):
            def handler():
                if changeguideo():
                    parzzley.gui.helpers.saveconfig(self.configobject.cfg)
                self.reload()
            return handler
        lcg = []
        for f in parzzley.gui.apidef.getregisteredchangeguides():
            for changeguide in f[0](self.configobject.cfg, self.configobject) or []:
                lcg.append((changeguide[0], changeguide[1], gethandler(changeguide[2])))
        lcg.sort(key=lambda x: x[0])
        parzzley.gui.gtk.popover_menu([tup[1:] for tup in lcg], btn)

    def __do_run(self, *_):
        answer = parzzley.gui.apidef.userfeedback.messagedialog(
            message=tr("Do you really want to run this synchronization task now?"), buttons=[tr("Yes"), tr("No")])
        if answer == 0:
            syncdlg = parzzley.gui.app_main.runsyncdialog.RunSyncDialog(modal=True, parent=self._toplevel_window)
            # noinspection PyMethodParameters
            class MyParzzleyRunThreadListener(parzzley.gui.helpers.ParzzleyRunThreadListener):
                def output(self_, txt):
                    GLib.idle_add(syncdlg.append_output, txt)
                def ended(self_, returnvalue):
                    def endedfct():
                        if returnvalue == 0:
                            syncdlg.sync_succeeded = True
                        else:
                            syncdlg.sync_failed = True
                        self.reload()
                    GLib.idle_add(endedfct)
            parzzleyrun = parzzley.gui.helpers.ParzzleyRunThread(MyParzzleyRunThreadListener(), self._rootconfig_datadir,
                                                                self._rootconfig_cfgfile, self.configobject.name)
            parzzleyrun.start()
            syncdlg.connect("destroy", lambda *_: parzzleyrun.cancel())
            syncdlg.show()

    def __do_remove(self, *_):
        self._ask_and_remove(self.configobject.cfg.syncs, self.configobject)

    def __do_conflicts(self, *_):
        self.__call_parzzley_tool("parzzley_infssync_manageconflicts_gui")

    def __do_report(self, *_):
        self.__call_parzzley_tool("parzzley_report_gui")

    def __call_parzzley_tool(self, toolname: str):
        parzzley.gui.helpers.call_parzzley_tool(toolname, syncname=self.configobject.name,
                                                datadir=self._rootconfig_datadir)


class LoggerConfigItemHandler(ConfigItemHandler):

    def __init__(self, logger: parzzley.config.config.ParzzleyConfiguration.Logger, **kwargs):
        super().__init__(logger, **kwargs)

    def get_header_text(self):
        return tr("Logger")

    def get_css_classname(self):
        return "logger"

    def init_ui(self, configitem):
        super().init_ui(configitem)
        self.configitem._cleanup()
        btnprefs = Gtk.ToggleToolButton(label=tr("Properties"), icon_widget=Gtk.Image(stock="gtk-index"),
                                        parent=configitem.toolbar)
        configitem._set_showbody_button(btnprefs)
        btnremove = Gtk.ToolButton(label=tr("Remove"), icon_widget=Gtk.Image(stock="gtk-delete"),
                                   parent=configitem.toolbar)
        btnremove.connect("clicked", self.__do_remove)
        configitem.toolbar.show_all()
        Gtk.Label(label=tr("Click on one of the nodes below in order to configure it.\n"
                           "Warning: Changes might break your configuration!"), parent=configitem.pnlbody,
                  margin_bottom=10)
        configitem.pnlbody.show_all()
        for paramkey, question in [("minseverity", tr("Please enter the new minimum severity for this logger.")),
                                   ("maxseverity", tr("Please enter the new maximum severity for this logger."))]:
            lblparam = ParamConfigNode(key_label=paramkey, value_label=str(getattr(self.configobject, paramkey)),
                                       parent=configitem.pnlconfigbody)
            lblparam.connect("clicked", self.__gethandler_edit_attr(paramkey, question))
        for paramkey in ["enabled"]:
            lblparam = ParamConfigNode(key_label=paramkey, value_label=str(getattr(self.configobject, paramkey)),
                                       parent=configitem.pnlconfigbody)
            lblparam.connect("clicked", self.__gethandler_edit_boolattr(paramkey))
        lblformatter = ObjectConfigNode(label=tr("Formatter '{0}'").format(self.configobject.formatter.otype),
                                        parent=configitem.pnlconfigbody)
        lblformatter.connect("clicked", self.__gethandler_edit_formatter())
        for paramkey, paramvalue in self.configobject.formatter.params.items():
            lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue,
                                       parent=configitem.pnlconfigbody, margin_left=20)
            lblparam.connect("clicked", self.__gethandler_edit_formatter_param(paramkey, paramvalue))
        lblloggerout = ObjectConfigNode(label=tr("Loggerout '{0}'").format(self.configobject.loggerout.otype),
                                        parent=configitem.pnlconfigbody)
        lblloggerout.connect("clicked", self.__gethandler_edit_loggerout())
        for paramkey, paramvalue in self.configobject.loggerout.params.items():
            lblparam = ParamConfigNode(key_label=paramkey, value_label=paramvalue,
                                       parent=configitem.pnlconfigbody, margin_left=20)
            lblparam.connect("clicked", self.__gethandler_edit_loggerout_param(paramkey, paramvalue))
        configitem.pnlconfigbody.show_all()

    def __gethandler_edit_attr(self, paramkey, question):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change"),
                                           lambda *_: self._edit_attr(self.configobject, paramkey, question))], btn)
        return handler

    def __gethandler_edit_boolattr(self, paramkey):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change"), lambda *_: self._edit_boolattr(self.configobject, paramkey))],
                                         btn)
        return handler

    def __gethandler_edit_formatter_param(self, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"),
                                           lambda *_:
                                           self._edit_param(self.configobject.formatter, paramkey, paramvalue)),
                                          (tr("Remove"),
                                           lambda *_: self._remove_param(self.configobject.formatter, paramkey))], btn)
        return handler

    def __gethandler_edit_loggerout_param(self, paramkey, paramvalue):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change value"), lambda *_:
                                           self._edit_param(self.configobject.loggerout, paramkey, paramvalue)),
                                          (tr("Remove"),
                                           lambda *_: self._remove_param(self.configobject.loggerout, paramkey))], btn)
        return handler

    def __gethandler_edit_formatter(self):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"),
                                           lambda *_: self._add_param(self.configobject.formatter)),
                                          (tr("Change type"),
                                           lambda *_: self._change_type(self.configobject.formatter))], btn)
        return handler

    def __gethandler_edit_loggerout(self):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Add parameter"),
                                           lambda *_: self._add_param(self.configobject.loggerout)),
                                          (tr("Change type"),
                                           lambda *_: self._change_type(self.configobject.loggerout))], btn)
        return handler

    def __do_remove(self, *_):
        self._ask_and_remove(self.configobject.cfg.loggers, self.configobject)


class CustomAspectConfigItemHandler(ConfigItemHandler):

    def __init__(self, customaspect: parzzley.config.config.ParzzleyConfiguration.CustomAspect, **kwargs):
        super().__init__(customaspect, **kwargs)

    def get_header_text(self):
        return tr("Custom Aspect '{0}'").format(self.configobject.name)

    def get_css_classname(self):
        return "customaspect"

    def init_ui(self, configitem):
        super().init_ui(configitem)
        self.configitem._cleanup()
        btneditcode = Gtk.ToolButton(label=tr("Edit code"), icon_widget=Gtk.Image(stock="gtk-justify-fill"),
                                     parent=configitem.toolbar)
        btneditcode.connect("clicked", self.__do_editcode)
        btnremove = Gtk.ToolButton(label=tr("Remove"), icon_widget=Gtk.Image(stock="gtk-delete"),
                                   parent=configitem.toolbar)
        btnremove.connect("clicked", self.__do_remove)
        configitem.toolbar.show_all()

    def __do_editcode(self, *_):
        answer = parzzley.gui.apidef.userfeedback.multilineinputdialog(
            question=tr("Please make your code changes here."), defaultanswer=self.configobject.code)
        if answer is not None:
            self.configobject.code = answer
            m = re.search(r"^class\s+([A-Za-z0-9_]+).*:", answer, flags=re.MULTILINE)
            if m:
                self.configobject.name = m.group(1).strip()
            parzzley.gui.helpers.saveconfig(self.configobject.cfg)
            self.reload()

    def __do_remove(self, *_):
        self._ask_and_remove(self.configobject.cfg.customaspects, self.configobject)


class FileIncludeConfigItemHandler(ConfigItemHandler):

    def __init__(self, fileinclude: parzzley.config.config.ParzzleyConfiguration.Include, **kwargs):
        super().__init__(fileinclude, **kwargs)

    def get_header_text(self):
        return tr("File Include '{0}'").format(self.configobject.incpath)

    def get_css_classname(self):
        return "fileinclude"

    def init_ui(self, configitem):
        super().init_ui(configitem)
        self.configitem._cleanup(body=False)
        btncontent = Gtk.ToggleToolButton(label=tr("Content"), icon_widget=Gtk.Image(stock="gtk-zoom-in"),
                                          parent=configitem.toolbar)
        configitem._set_showbody_button(btncontent)
        btnremove = Gtk.ToolButton(label=tr("Remove"), icon_widget=Gtk.Image(stock="gtk-delete"),
                                   parent=configitem.toolbar)
        btnremove.connect("clicked", self.__do_remove)
        configitem.toolbar.show_all()
        configitems_for_config(self._rootconfig_cfgfile, self._rootconfig_datadir, self.configobject.innercfg,
                               self.reload, self.__do_add, configitem.pnlbody)

    def __do_remove(self, *_):
        self._ask_and_remove(self.configobject.cfg.includes, self.configobject)

    def __do_add(self, cfg, aligntowidget):
        self.configitem._trigger_add_item(cfg, aligntowidget)


class PythonImportConfigItemHandler(ConfigItemHandler):

    def __init__(self, pythonimport: parzzley.config.config.ParzzleyConfiguration.PythonImport, **kwargs):
        super().__init__(pythonimport, **kwargs)

    def get_header_text(self):
        return tr("Python Import '{0}'").format(self.configobject.to)

    def get_css_classname(self):
        return "pythonimport"

    def init_ui(self, configitem):
        super().init_ui(configitem)
        self.configitem._cleanup()
        btnprefs = Gtk.ToggleToolButton(label=tr("Properties"), icon_widget=Gtk.Image(stock="gtk-index"),
                                        parent=configitem.toolbar)
        configitem._set_showbody_button(btnprefs)
        btnremove = Gtk.ToolButton(label=tr("Remove"), icon_widget=Gtk.Image(stock="gtk-delete"),
                                   parent=configitem.toolbar)
        btnremove.connect("clicked", self.__do_remove)
        configitem.toolbar.show_all()
        for paramkey, question in [("importfrom", tr("Please enter the new full name of the Python object you want to"
                                                     " import.")),
                                   ("to", tr("Please enter the new name you want to make this object available as."))]:
            lblparam = ParamConfigNode(key_label=paramkey, value_label=str(getattr(self.configobject, paramkey)),
                                       parent=configitem.pnlconfigbody)
            lblparam.connect("clicked", self.__gethandler_edit_attr(paramkey, question))
        configitem.pnlconfigbody.show_all()

    def __gethandler_edit_attr(self, paramkey, question):
        def handler(btn, *_):
            parzzley.gui.gtk.popover_menu([(tr("Change"),
                                           lambda *_: self._edit_attr(self.configobject, paramkey, question))], btn)
        return handler

    def __do_remove(self, *_):
        self._ask_and_remove(self.configobject.cfg.pythonimports, self.configobject)


def configitems_for_config(rootconfig_cfgfile, rootconfig_datadir, config, reloadfct, additemfct, container):
    class MyConfigItemListener(ConfigItemListener):
        def reload(self):
            reloadfct()
        def add_item(self, config2, aligntowidget):
            additemfct(config2, aligntowidget)
    oldconfigitems = {}
    for oldconfigitem in container.get_children():
        configobject = getattr(oldconfigitem, "configobject", None)
        if configobject:
            oldconfigitems[configobject] = oldconfigitem
        else:
            container.remove(oldconfigitem)
    for configobjects, handlerclass in [
            (config.syncs, parzzley.gui.app_main.configitem.SyncTaskConfigItemHandler),
            (config.loggers, parzzley.gui.app_main.configitem.LoggerConfigItemHandler),
            (config.customaspects, parzzley.gui.app_main.configitem.CustomAspectConfigItemHandler),
            (config.includes, parzzley.gui.app_main.configitem.FileIncludeConfigItemHandler),
            (config.pythonimports, parzzley.gui.app_main.configitem.PythonImportConfigItemHandler)]:
        for configobject in configobjects:
            oldconfigitem = oldconfigitems.get(configobject)
            if oldconfigitem:
                oldconfigitems.pop(configobject)
                oldconfigitem.refresh()
            else:
                handler = handlerclass(configobject)
                handler._set_root_config(rootconfig_cfgfile, rootconfig_datadir)
                configitem = parzzley.gui.app_main.configitem.ConfigItem(handler, visible=True)
                configitem.add_listener(MyConfigItemListener())
                container.add(configitem)
    for oldconfigitem in oldconfigitems.values():
        container.remove(oldconfigitem)
    btnadd = Gtk.Button(label=tr("Add item"), image=Gtk.Image(stock="gtk-add"), visible=True)
    btnadd.get_style_context().add_class("btnaddconfigitem")
    btnadd.connect("clicked", lambda *_: additemfct(config, btnadd))
    container.add(btnadd)


# we must call that once, otherwise the css does not get applies to the first element, for some reason (gtk bug?!)
class _DummyConfigItemHandler(ConfigItemHandler):

    def get_header_text(self):
        return ""

    def get_css_classname(self):
        return ""


ConfigItem(_DummyConfigItemHandler(None))
