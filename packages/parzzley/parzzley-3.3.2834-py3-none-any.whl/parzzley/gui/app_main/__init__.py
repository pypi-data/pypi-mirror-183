# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
The Parzzley main user interface.
"""

import datetime
import os
import subprocess
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.config.config
import parzzley.gui.apidef
import parzzley.gui.aspect
import parzzley.gui.filesystem
import parzzley.gui.gtk
import parzzley.gui.gtk.userfeedback
import parzzley.gui.helpers
import parzzley.gui.app_main.configitem
import parzzley.runtime._project_infos
import parzzley.syncengine.core
import parzzley.tools.common


_mydir = os.path.dirname(__file__)


class App:

    def __init__(self):
        builder = parzzley.gui.gtk.ParzzleyGtkBuilder()
        builder.add_from_file(f"{_mydir}/main.ui")
        self.__win = builder.get_object("mainwindow")
        self.__btnopen = builder.get_object("btnopen")
        self.__btnhelp = builder.get_object("btnhelp")
        self.__btnabout = builder.get_object("btnabout")
        self.__lblconfigfile = builder.get_object("lblconfigfile")
        self.__pnlnotparzzleyconf = builder.get_object("pnlnotparzzleyconf")
        self.__pnlbody = builder.get_object("pnlbody")
        self.__pnlconfigitems = builder.get_object("pnlconfigitems")
        self.__newitemmenu = builder.get_object("newitemmenu")
        self.__btnnewsynctask = builder.get_object("btnnewsynctask")
        self.__btnnewlogger = builder.get_object("btnnewlogger")
        self.__btnnewcustomaspect = builder.get_object("btnnewcustomaspect")
        self.__btnnewfileinclude = builder.get_object("btnnewfileinclude")
        self.__btnnewpythonimport = builder.get_object("btnnewpythonimport")
        self.__btnopen.connect("clicked", self.__openfiledialog)
        self.__btnhelp.connect("clicked", self.__help)
        self.__btnabout.connect("clicked", self.__about)
        self.__btnnewsynctask.connect("clicked", self.__do_add_synctask)
        self.__btnnewlogger.connect("clicked", self.__do_add_logger)
        self.__btnnewcustomaspect.connect("clicked", self.__do_add_customaspect)
        self.__btnnewfileinclude.connect("clicked", self.__do_add_fileinclude)
        self.__btnnewpythonimport.connect("clicked", self.__do_add_pythonimport)
        parzzley.gui.gtk.load_common_css()
        parzzley.gui.gtk.load_css(f"{_mydir}/main.css")
        self.__config = None
        self.__configfile = None
        self.__datadir = None
        self.__newitemmenu_config = None

    def __help(self, *_):
        docfile = None
        for d in ["/usr/share/doc/parzzley", os.path.dirname(sys.argv[0])]:
            if os.path.exists(f"{d}/README.pdf"):
                docfile = f"{d}/README.pdf"
                break
        if not docfile:
            docfile = parzzley.runtime._project_infos.homepage_url
        try:
            if sys.platform == "win32":
                # noinspection PyUnresolvedReferences
                os.startfile(docfile)
            else:
                subprocess.call(("xdg-open", docfile))
        except IOError:
            pass

    def __about(self, *_):
        #TODO _project_infos.*
        dlg = Gtk.AboutDialog(transient_for=self.__win)
        buildtimetxt = datetime.datetime.fromisoformat(parzzley.runtime._project_infos.buildtimeutc).replace(
            tzinfo=datetime.timezone.utc).astimezone().strftime("%c")
        dlg.props.program_name = tr("Parzzley")
        dlg.props.version = parzzley.runtime._project_infos.version
        dlg.props.website = parzzley.runtime._project_infos.homepage_url
        dlg.props.license = parzzley.runtime._project_infos.license
        dlg.props.comments = tr("built: {0}\n\n{1}").format(buildtimetxt, parzzley.runtime._project_infos.summary)
        dlg.props.authors = ["Josef Hahn"]
        dlg.props.logo = self.__win.props.icon
        dlg.run()
        dlg.destroy()

    def __openfiledialog(self, *_):
        dialog = Gtk.FileChooserDialog(title=tr("Choose a configuration file"),
                                       parent=self.__win, action=Gtk.FileChooserAction.OPEN,
                                       buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                                Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        filefilter = Gtk.FileFilter()
        filefilter.set_name(tr("XML files"))
        filefilter.add_pattern("*.xml")
        dialog.add_filter(filefilter)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.__openfile(dialog.get_filename())
        dialog.destroy()

    def __openfile(self, filepath):
        self.__configfile = filepath
        try:
            self.__config = parzzley.gui.helpers.openconfig(filepath)
        except Exception as ex:
            self.__config = None
            print(f"Unable to load '{filepath}': {ex}")
        self._populate()

    def __do_add(self, config, aligntowidget):
        self.__newitemmenu.hide()
        self.__newitemmenu_config = config
        self.__newitemmenu.props.relative_to = aligntowidget
        self.__newitemmenu.popup()

    def __do_add_synctask(self, *_):
        config = self.__newitemmenu_config
        userfeedback = parzzley.gui.apidef.userfeedback
        defaultanswerprep = None
        i = 1
        while (defaultanswerprep is None) or (defaultanswerprep in [x.name for x in config.syncs]):
            defaultanswerprep = f"sync_{i}"
            i += 1
        lsfsh = []
        lfsh = []
        lfs = []
        for fs in parzzley.gui.apidef.getregisteredfilesystemhelpers():
            lsfsh.append(fs[1]().label)
            lfsh.append(fs[1])
            lfs.append(fs[0])
        cfgsync = parzzley.config.config.ParzzleyConfiguration.Sync(config, [], [], [])
        for i in range(2):
            ifs = userfeedback.choicedialog(tr("Please choose the type for the {0}. filesystem.").format(i+1), lsfsh)
            if ifs is not None:
                fs = lfs[ifs]
                fsh = lfsh[ifs]
                cfgfs = parzzley.config.config.ParzzleyConfiguration.Filesystem(config, fs.__name__, [])
                cfgfs.aspects.append(parzzley.config.config.ParzzleyConfiguration.Aspect(config, "TrashRemove"))
                cfgfs.name = parzzley.gui.apidef.getnumstring(i+1)
                if not fsh().configfs(cfgfs, cfgsync):
                    break
                cfgsync.filesystems.append(cfgfs)
            else:
                break
        if len(cfgsync.filesystems) == 2:  # not cancelled
            nname = userfeedback.inputdialog(tr("Please specify a name for this synchronization task."),
                                             defaultanswerprep)
            if nname is not None:
                cfgsync.name = nname
                cfgsync.aspects.append(parzzley.config.config.ParzzleyConfiguration.Aspect(config, "DefaultSync"))
                cfgsync.aspects.append(parzzley.config.config.ParzzleyConfiguration.Aspect(config, "Logging"))
                config.syncs.append(cfgsync)
                parzzley.gui.helpers.saveconfig(config)
        self._populate()

    def __do_add_logger(self, *_):
        config = self.__newitemmenu_config
        loggerout = parzzley.config.config.ParzzleyConfiguration.Loggerout(config, "FilestreamLoggerout")
        formatter = parzzley.config.config.ParzzleyConfiguration.LogFormatter(config, "PlaintextLogformat")
        cfglogger = parzzley.config.config.ParzzleyConfiguration.Logger(config, "info", None, loggerout, formatter, True)
        config.loggers.append(cfglogger)
        parzzley.gui.helpers.saveconfig(config)
        self._populate()

    def __do_add_customaspect(self, *_):
        config = self.__newitemmenu_config
        namedialog = parzzley.gui.gtk.EntryDialog(text=tr("Please specify a type name for the new custom aspect."),
                                                 entry_text="DoSomeStuff", modal=True, parent=self.__win)
        name = namedialog.run_and_get_entry_text()
        namedialog.destroy()
        if name:
            code = f"""
class {name}(parzzley.aspect.abstractaspect.Aspect):

    def __init__(self):
        super().__init__()

    @parzzley.aspect.hook('', '', '', event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def mybeginstuff(self, ctx, filesystem):
        ctx.log(comment="Hello World!")

    @parzzley.aspect.hook('', '', '', event=parzzley.syncengine.common.SyncEvent.EndSync)
    def myclosingstuff(self, ctx, filesystem):
        ctx.log(comment="Goodbye!")
                    """.strip()
            cfgcustomaspect = parzzley.config.config.ParzzleyConfiguration.CustomAspect(config, name, code)
            config.customaspects.append(cfgcustomaspect)
            parzzley.gui.helpers.saveconfig(config)
        self._populate()

    def __do_add_fileinclude(self, *_):
        config = self.__newitemmenu_config
        namedialog = parzzley.gui.gtk.EntryDialog(text=tr("Please specify a file name (or relative path) to include.\n\n"
                                                         "If this file does not exist, it will be created."),
                                                 entry_text="foo.xml", modal=True, parent=self.__win)
        name = namedialog.run_and_get_entry_text()
        namedialog.destroy()
        if name:
            cfginclude = parzzley.config.config.ParzzleyConfiguration.Include(config, name)
            ffpath = cfginclude.get_absolute_path(f"{config.filename}/..")
            if not os.path.exists(ffpath):
                os.makedirs(os.path.dirname(ffpath), exist_ok=True)
                with open(ffpath, "w") as f:
                    f.write("""
<?xml version="1.0" ?>
<parzzleyconfig>
</parzzleyconfig>
                        """.strip())
            config.includes.append(cfginclude)
            parzzley.gui.helpers.saveconfig(config)
            self.__openfile(self.__configfile)
        self._populate()

    def __do_add_pythonimport(self, *_):
        config = self.__newitemmenu_config
        importfromdialog = parzzley.gui.gtk.EntryDialog(text=tr("Please enter the full name (dot-separated including"
                                                               " package and module names) of the Python object (class,"
                                                               " function, ...) you want to import."),
                                                       entry_text="my.mo.du.le.MyClass", modal=True,
                                                       parent=self.__win)
        importfrom = importfromdialog.run_and_get_entry_text()
        importfromdialog.destroy()
        if importfrom:
            todialog = parzzley.gui.gtk.EntryDialog(text=tr("Please enter the name (without dots) you want to make"
                                                           " this object available as."),
                                                   entry_text="MyClass", modal=True, parent=self.__win)
            to = todialog.run_and_get_entry_text()
            todialog.destroy()
            if to:
                pythonimport = parzzley.config.config.ParzzleyConfiguration.PythonImport(config, importfrom, to)
                config.pythonimports.append(pythonimport)
                parzzley.gui.helpers.saveconfig(config)
        self._populate()

    def _populate(self):
        apptitle = tr("Parzzley")
        self.__pnlnotparzzleyconf.hide()
        self.__pnlbody.hide()
        cleanupconfigitems = True
        if self.__configfile:
            self.__win.props.title = f"{self.__configfile} - {apptitle}"
            self.__lblconfigfile.props.label = self.__configfile
            if self.__config is not None:
                self.__pnlbody.show()
                parzzley.gui.app_main.configitem.configitems_for_config(self.__configfile, self.__datadir, self.__config,
                                                                       self._populate, self.__do_add,
                                                                       self.__pnlconfigitems)
                cleanupconfigitems = False
            else:
                self.__pnlnotparzzleyconf.show()
            self.__pnlbody.show()
        else:
            self.__win.props.title = apptitle
        if cleanupconfigitems:
            for oldchild in self.__pnlconfigitems.get_children():
                self.__pnlconfigitems.remove(oldchild)

    def show(self):
        parzzley.gui.apidef.userfeedback = parzzley.gui.gtk.userfeedback.UserFeedbackController(self.__win)
        self.__win.show_all()
        self.__win.connect("delete_event", Gtk.main_quit)
        self._populate()
        cmdline = parzzley.syncengine.core.CmdLine(sys.argv)
        cfgfile = cmdline.configfile_or_default()
        self.__datadir = cmdline.datadir_or_default()
        if not os.path.exists(cfgfile):
            parzzley.tools.common.call(*parzzley.gui.helpers.parzzley_cmdline("--createconfig", "--configfile", cfgfile))
            parzzley.gui.apidef.userfeedback.messagedialog(tr(
                "Welcome to Parzzley!\n\n"
                "At first you should add at least one sync task. You can then run it directly from here, but maybe"
                " should configure it for automated background syncing later.\n\n"
                "Be aware that you use Parzzley at your own risk. Misuse (and also software errors) could screw"
                " up your data."))
        self.__openfile(cfgfile)
        Gtk.main()


def run():
    App().show()
