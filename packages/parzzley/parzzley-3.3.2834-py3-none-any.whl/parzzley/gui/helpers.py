# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import abc
import gettext
import locale
import os
import subprocess
import sys
import threading
import typing as t

import parzzley.config.config
import parzzley.logger.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.core


mydir = os.path.dirname(__file__)
parzzleyrootdir = os.path.dirname(os.path.dirname(mydir))


locale.setlocale(locale.LC_ALL, None)  # common boilerplate thingy for usage of the 'locale' module


# noinspection PyUnresolvedReferences
def _translator() -> t.Callable[[str], str]:
    gettext.textdomain("parzzley")
    locale.textdomain("parzzley")
    for localedir in [None, f"{parzzleyrootdir}/locale"]:
        if gettext.find("parzzley", localedir):
            locale.bindtextdomain("parzzley", localedir)
            gettext.bindtextdomain("parzzley", localedir)
            break
    return gettext.gettext


tr = _translator()


class ParzzleyRunThreadListener:

    @abc.abstractmethod
    def output(self, txt: str) -> None:
        pass

    @abc.abstractmethod
    def ended(self, returnvalue: int) -> None:
        pass


class ParzzleyRunThread(threading.Thread):

    def __init__(self, listener: ParzzleyRunThreadListener, datadir: str, configfile: str, syncname: str):
        if not syncname:
            raise ValueError("syncname must not be empty")
        super().__init__()
        self.listener = listener
        self.outputnuggets = []
        self._nextoutputnuggetid = 0
        self.datadir = datadir
        self.configfile = configfile
        self.syncname = syncname
        self.retval = None
        self.process = None
        ocmdlist = ["--sync", self.syncname]
        if self.configfile != parzzley.syncengine.core.CmdLine([]).configfile_or_default():
            ocmdlist += ["--configfile", self.configfile]
        if self.datadir != parzzley.syncengine.core.CmdLine([]).datadir_or_default():
            ocmdlist += ["--datadir", self.datadir]
        self.cmdlist = parzzley.gui.helpers.parzzley_cmdline(*ocmdlist)

    def cancel(self) -> None:
        if self.process:
            self.process.terminate()

    def run(self):
        p = subprocess.Popen(self.cmdlist, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.process = p
        while True:
            line = p.stdout.readline()
            if not line:
                break
            self.listener.output(line.decode())
        self.listener.ended(p.wait())


def parzzley_cmdline(*params: str, toolname: str = "parzzley") -> t.List[str]:
    parzzleycmd = f"{parzzleyrootdir}/{toolname}.py"
    if not os.path.isfile(parzzleycmd):
        parzzleycmd = toolname
    cmdline = [parzzleycmd, *params]
    if sys.platform == "win32":
        cmdline = [sys.executable, *cmdline]
    return cmdline


def get_volume_paths_for_sync(syncname: str, *, datadir: str) -> t.List[str]:
    result = []
    if not syncname:
        raise ValueError("syncname must not be empty")
    d = f"{datadir}/volume_path_breadcrumb/{syncname}"
    if os.path.exists(d):
        for f in os.listdir(d):
            ff = f"{d}/{f}/{parzzley.runtime.datastorage.StorageDepartment.VALUE_FILENAME}"
            if os.path.exists(ff):
                with open(ff, "r") as fff:
                    breadcrumb = fff.read()
                if breadcrumb and os.path.exists(f"{breadcrumb}/.parzzley.control"):
                    result.append(breadcrumb)
    return result


def call_parzzley_tool(toolname: str, *, syncname: str, datadir: str) -> None:
    volpath = get_volume_paths_for_sync(syncname, datadir=datadir)[0]
    threading.Thread(target=lambda: subprocess.call(parzzley_cmdline(volpath, toolname=toolname))).start()


def find_volume_rootpath(path: str) -> t.Optional[str]:
    realpath = os.path.abspath(path)
    while (realpath is not None) and not os.path.isdir(f"{realpath}/.parzzley.control"):  # TODO noh finish renaming
        orealpath = realpath
        realpath = os.path.dirname(realpath)
        if realpath == orealpath:
            realpath = None
    return realpath


def openconfig(cfgfile: str) -> t.Optional[parzzley.config.config.ParzzleyConfiguration]:
    def _loadincludes(cfg, _cfgfile):
        for inc in cfg.includes:
            ipath = inc.get_absolute_path(f"{_cfgfile}/..")
            try:
                with open(ipath, "r") as fpi:
                    cnt = fpi.read()
                inc.innercfg = parzzley.config.config.ParzzleyConfiguration.fromxml(cnt)
                inc.innercfg.filename = ipath
                _loadincludes(inc.innercfg, ipath)
                inc.loaderror = None
            except Exception as ex:
                inc.innercfg = None
                inc.loaderror = str(ex)
    if cfgfile:
        with open(cfgfile, "r") as f:
            scfg = "".join(f.readlines())
        result = parzzley.config.config.ParzzleyConfiguration.fromxml(scfg)
        result.filename = cfgfile
        _loadincludes(result, cfgfile)
        return result


def saveconfig(cfg: parzzley.config.config.ParzzleyConfiguration) -> None:
    xml = cfg.toxml()
    # noinspection PyUnresolvedReferences
    with open(cfg.filename, "w") as f:
        f.write(xml)
