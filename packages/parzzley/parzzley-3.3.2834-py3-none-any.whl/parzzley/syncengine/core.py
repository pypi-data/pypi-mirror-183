# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
The engine which abstractly executes arbitrary synchronization tasks.
"""

import datetime
import os
import socket
import sys
import time
import typing as t

import parzzley.config.config
import parzzley.exceptions
import parzzley.logger
import parzzley.runtime.commonimports
import parzzley.runtime.returnvalue
import parzzley.runtime.runtime
import parzzley.runtime.datastorage
import parzzley.tools.common

if t.TYPE_CHECKING:
    import parzzley.syncengine.sync


class Core:
    """
    The Parzzley engine. It is the lowest (or higest, if you want) layer, which coordinates all the synchronization
    work.
    """

    class _Myclass:
        
        def __init__(self):
            self.changed_flag = False
                
    class CoreRuntime:

        def __init__(self, sync: 'parzzley.syncengine.sync.Sync'):
            self.sync = sync
            self.runname = "{},{},{},{}".format(socket.gethostname(), os.getpid(), sync.name,
                                                datetime.datetime.now().timestamp())
            # noinspection PyProtectedMember
            self.syncglobaldata = Core._Myclass()

    @staticmethod
    def execute(syncs: t.List['parzzley.syncengine.sync.Sync'], datadir: str, syncname: t.Optional[str] = None,
                logging: t.Optional[t.List['parzzley.logger.Logger']] = None, throwexceptions: bool = False) -> int:
        """
        Executes the selected synchronization tasks.

        :param syncs: a list of synchronization tasks existing in your configuration.
        :param datadir: which directory to use for persistent control data (file lists, ...).
        :param syncname: which sync task shall be executed (None: all).
        :param logging: list of loggers of logging output.
        :param throwexceptions: If exceptions should be raised in error case.
        """
        if logging is None:
            logging = []
        runtime = parzzley.runtime.runtime.RuntimeData(datadir, logging, syncs)
        try:
            with runtime:
                if syncname:
                    syncstack = [[s, True] for s in syncs if s.name == syncname]
                else:
                    syncstack = [[x, False] for x in syncs]
                for sync, force in syncstack:
                    sruntime = runtime.clone(merge_also_from=Core.CoreRuntime(sync))
                    try:
                        sync.execute(sruntime, force)
                    except Exception:
                        runtime.set_retval(parzzley.runtime.returnvalue.ReturnValue.ERROR)
                        if throwexceptions:
                            raise
        finally:
            runtime.log(verb="Finished task executions", severity=parzzley.logger.Severity.DEBUGVERBOSE)
        with open(runtime.datadir + "/heartbeat", "w"):
            pass
        return runtime.get_retval()


class CmdLine:
    """
    Parser for command line arguments.
    """

    def __init__(self, args: t.List[str]):
        c = 1
        self.forcesyncs = None
        self.lockpid = None
        self.sync = None
        def _next():
            nonlocal c, args
            v = args[c] if c < len(args) else None
            c += 1
            return v
        values = {}
        _p = _next()
        forcesyncs = []
        values["forcesyncs"] = forcesyncs
        while _p is not None:
            if _p[0:2] != "--":
                raise Exception("parse error: " + _p)
            p = _p[2:]
            if p == "sync":
                values[p] = _next()
            elif p == "datadir":
                values[p] = _next()
            elif p == "configfile":
                values[p] = _next()
            elif p == "createconfig":
                values[p] = True
            elif p == "lock" or p == "unlock":
                values[p] = True
                if p == "lock":
                    values["lockpid"] = _next()
            elif p == "forcesync":
                forcesyncs += [_next()]
            elif p == "listsyncs":
                values[p] = True
            else:
                raise parzzley.exceptions.InvalidCommandLineError("unknown parameter: '" + p + "'")
            _p = _next()
        self.cfgs = values.keys()
        for k in values:
            setattr(self, k, values[k])

    def datadir_or_default(self) -> str:
        return getattr(self, "datadir", os.path.expanduser("~/.parzzley"))

    def configfile_or_default(self) -> str:
        return getattr(self, "configfile", self.datadir_or_default() + "/parzzley.xml")


def _createemptyconfigifneeded(cmdline: CmdLine) -> None:
    configfile = cmdline.configfile_or_default()
    if not os.path.exists(configfile):
        cfgfiledir = os.path.dirname(configfile)
        if cfgfiledir and not os.path.exists(cfgfiledir):
            os.makedirs(cfgfiledir)
        with open(configfile, "w") as f:
            f.write("""<?xml version="1.0" ?>
<parzzleyconfig>
    <logger minseverity="info" maxseverity="error">
        <out type="FilestreamLoggerout" />
        <formatter type="PlaintextLogformat"/>
    </logger>
</parzzleyconfig>
""")
        print("Created new config file: " + configfile)


def main(cmdline: t.Optional[t.List[str]] = None, callexit: bool = True,
         environment: t.Optional[t.Dict[str, str]] = None) -> int:
    """
    Main method for execution from command line.
    """
    environment = dict(environment or os.environ)
    retval = 0
    cmdline = CmdLine(cmdline or sys.argv)
    datadir = cmdline.datadir_or_default()
    configfile = cmdline.configfile_or_default()
    if not os.path.exists(datadir):
        os.makedirs(datadir)
    for forcesync in cmdline.forcesyncs:
        fn = f"{datadir}/sync_success/{forcesync}/{parzzley.runtime.datastorage.StorageDepartment.VALUE_FILENAME}"
        if os.path.exists(fn):
            fn = os.path.abspath(fn)
            with open(fn, "r") as f:
                c = f.readlines()
            if c is not None:
                if len(c) > 0:
                    c[0] = " " + c[0]
                    with open(fn, "w") as f:
                        for cl in c:
                            f.write(cl)
    if "sync" in cmdline.cfgs:
        _createemptyconfigifneeded(cmdline)
        if parzzley.tools.common.lock(f"{datadir}/lock"):
            knowntypes = None
            try:
                csyncs = []
                cloggers = []
                knowntypes = dict(parzzley.runtime.commonimports.__dict__)
                try:
                    parzzley.config.config.threadlocal.knowntypes.append(knowntypes)
                except AttributeError:
                    parzzley.config.config.threadlocal.knowntypes = [knowntypes]
                configfiles = [configfile]
                while len(configfiles) > 0:
                    cfgfile = configfiles.pop()
                    with open(cfgfile, "r") as f:
                        cfg = "".join(f.readlines())
                    cfgfiledir = os.path.dirname(cfgfile)
                    if cfgfiledir not in sys.path:
                        sys.path.append(cfgfiledir)
                    parzzleycfg = parzzley.config.config.ParzzleyConfiguration.fromxml(cfg, environment)
                    for sync in parzzleycfg.syncs:
                        csyncs.append(sync)
                    for logger in parzzleycfg.loggers:
                        cloggers.append(logger)
                    for customaspect in parzzleycfg.customaspects:
                        knowntypes[customaspect.name] = customaspect.instantiate(knowntypes)
                    for include in parzzleycfg.includes:
                        configfiles.append(include.get_absolute_path(f"{cfgfile}/.."))
                    for pythonimport in parzzleycfg.pythonimports:
                        knowntypes[pythonimport.to] = pythonimport.instantiate()
                syncs = [x.instantiate(knowntypes) for x in csyncs]
                loggers = [x.instantiate(knowntypes) for x in cloggers]
                syncname = cmdline.sync if cmdline.sync != "ALL" else None
                retval = Core.execute(syncs, datadir, syncname, loggers)
            except KeyboardInterrupt:
                pass
            finally:
                if knowntypes:
                    parzzley.config.config.threadlocal.knowntypes.pop()
                parzzley.tools.common.unlock(f"{datadir}/lock")
        else:
            sys.stderr.write("Skipped because the datadir is locked (maybe a sync is currently running?).\n")
    elif "lock" in cmdline.cfgs:
        lprms = {}
        if cmdline.lockpid:
            lprms["lockpid"] = int(cmdline.lockpid)
        else:
            lprms["pidless"] = True
        i = 0
        while not parzzley.tools.common.lock(f"{datadir}/lock", **lprms):
            if i % 20 == 0:
                print("Waiting for other instance...")
            i += 1
            time.sleep(1)
    elif "unlock" in cmdline.cfgs:
        parzzley.tools.common.unlock(f"{datadir}/lock")
    elif "createconfig" in cmdline.cfgs:
        _createemptyconfigifneeded(cmdline)
    elif "listsyncs" in cmdline.cfgs:
        _createemptyconfigifneeded(cmdline)
        configfiles = [configfile]
        while len(configfiles) > 0:
            cfgfile = configfiles.pop()
            with open(cfgfile, "r") as f:
                cfg = "".join(f.readlines())
                parzzleycfg = parzzley.config.config.ParzzleyConfiguration.fromxml(cfg)
                for sync in parzzleycfg.syncs:
                    print(sync.name)
                for i in parzzleycfg.includes:
                    configfiles.append(i.get_absolute_path(f"{cfgfile}/.."))
    if callexit:
        sys.exit(retval)
    else:
        return retval
