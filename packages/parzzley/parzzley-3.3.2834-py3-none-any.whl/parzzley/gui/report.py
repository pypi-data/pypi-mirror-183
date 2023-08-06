# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import bz2
import datetime
import os
import pickle
import re
import threading
import typing as t
# noinspection PyPep8Naming
import xml.etree.ElementTree as ET

import parzzley.logger.logger


class PerformanceData:

    def __init__(self, syncruns: t.List[str], eventhandlers: t.List[str], filesystems: t.List[str],
                 timingdata: t.Dict[str, 'PerformanceData.Sync']):
        self.__syncruns = syncruns
        self.__eventhandlers = eventhandlers
        self.__filesystems = filesystems
        self.__timingdata = timingdata

    @property
    def syncruns(self) -> t.List[str]:
        return self.__syncruns

    @property
    def synctasks(self) -> t.List[str]:
        return list(self.timingdata.keys())

    @property
    def eventhandlers(self) -> t.List[str]:
        return self.__eventhandlers

    @property
    def filesystems(self) -> t.List[str]:
        return self.__filesystems

    @property
    def timingdata(self) -> t.Dict[str, 'PerformanceData.Sync']:
        return self.__timingdata

    class Sync:

        def __init__(self, name: str):
            self.name = name
            self.runs = {}

    class SyncRun:

        def __init__(self, name: str):
            self.name = name
            self.eventhandlers = {}

    class EventHandler:

        def __init__(self, name: str, eventname: str):
            self.name = name
            self.eventname = eventname
            self.filesystems = {}

    class Filesystem:

        def __init__(self, name: str):
            self.name = name
            self.paths = {}

    class Path:

        def __init__(self, path: str):
            self.name = path
            self.duration = 0

    class Table:

        def __init__(self):
            self.rows = {}
            self.cols = set()

        def add(self, rowname: str, colname: str, value: float) -> None:
            if rowname not in self.rows:
                self.rows[rowname] = {}
            _row = self.rows[rowname]
            if colname not in _row:
                _row[colname] = []
            col = _row[colname]
            col.append(value)
            self.cols.add(colname)

    class QueryResult:

        def __init__(self, row_names: t.List[str], column_names: t.List[str], result: t.List[t.List[float]]):
            self.row_names = row_names
            self.column_names = column_names
            self.result = result

    class Loader:

        @classmethod
        def __read_events(cls, _levents, _eventlist, _eventhandlerset, _filesystemset):
            def _duration(lnode):
                if lnode[3] is None:
                    return 0
                return float(lnode[3]) - float(lnode[2])
            for levent in _levents:
                path = levent[1] or "/"
                eventname = levent[0]
                for lhandler in levent[4]:
                    filesystem = lhandler[1]
                    handlername = lhandler[0]
                    duration = max(0, _duration(lhandler) - sum([_duration(x) for x in lhandler[4]]))
                    if handlername not in _eventlist:
                        _eventlist[handlername] = PerformanceData.EventHandler(handlername, eventname)
                        _eventhandlerset.add(handlername)
                    ohandler = _eventlist[handlername]
                    if filesystem not in ohandler.filesystems:
                        ohandler.filesystems[filesystem] = PerformanceData.Filesystem(filesystem)
                        _filesystemset.add(filesystem)
                    ofilesystem = ohandler.filesystems[filesystem]
                    if path not in ofilesystem.paths:
                        ofilesystem.paths[path] = PerformanceData.Path(path)
                    opath = ofilesystem.paths[path]
                    opath.duration += duration
                    cls.__read_events(lhandler[4], _eventlist, _eventhandlerset, _filesystemset)

        def __init__(self):
            self.__perfdata = None
            self.__queryresult = None
            self.__lock = threading.RLock()
            self.__setpath_reqtoken = None
            self.__queryresult_reqtoken = None
            self.__data_available_changed_handlers = []
            self.__query_result_available_changed_handlers = []

        def add_data_available_changed_handler(self, fct):
            self.__data_available_changed_handlers.append(fct)
            fct(self.data_available)

        def add_query_result_available_changed_handler(self, fct):
            self.__query_result_available_changed_handlers.append(fct)
            fct(self.query_result_available)

        @property
        def data_available(self) -> bool:
            with self.__lock:
                return self.__perfdata is not None

        @property
        def query_result_available(self) -> bool:
            with self.__lock:
                return self.__queryresult is not None

        def get_data(self) -> 'PerformanceData':
            with self.__lock:
                return self.__perfdata

        def get_query_result(self) -> 'PerformanceData.QueryResult':
            with self.__lock:
                return self.__queryresult

        def set_path(self, path: str) -> None:
            with self.__lock:
                self.__perfdata = None
                self.__queryresult = None
                for data_available_changed_handler in self.__data_available_changed_handlers:
                    data_available_changed_handler(False)
                for query_result_available_changed_handler in self.__query_result_available_changed_handlers:
                    query_result_available_changed_handler(False)
                self.__setpath_reqtoken = reqtoken = object()
            if path:
                def loadstuff():
                    benchmarkdir = f"{path}/.parzzley.control/sync_benchmark/"
                    timingdata = {}
                    syncrunset = set()
                    eventhandlerset = set()
                    filesystemset = set()
                    if os.path.exists(benchmarkdir):
                        for sname in os.listdir(benchmarkdir):
                            timingdata[sname] = osync = PerformanceData.Sync(sname)
                            fsp = f"{benchmarkdir}/{sname}"
                            for f in os.listdir(fsp):
                                if self.__setpath_reqtoken != reqtoken:
                                    return
                                ff = f"{fsp}/{f}"
                                with open(ff, "rb") as ffff:
                                    zxbnch = ffff.read()
                                sxbnch = bz2.decompress(zxbnch)
                                obnch = pickle.loads(sxbnch)
                                syncrun = obnch[2]
                                osyncrun = PerformanceData.SyncRun(syncrun)
                                osync.runs[syncrun] = osyncrun
                                syncrunset.add(syncrun)
                                self.__read_events(obnch[0], osyncrun.eventhandlers, eventhandlerset, filesystemset)
                    with self.__lock:
                        if self.__setpath_reqtoken == reqtoken:
                            self.__perfdata = PerformanceData(sorted(list(syncrunset)), sorted(list(eventhandlerset)),
                                                              sorted(list(filesystemset)), timingdata)
                            for data_available_changed_handler_ in self.__data_available_changed_handlers:
                                data_available_changed_handler_(True)
                threading.Thread(target=loadstuff, daemon=True).start()

        def query(self, *, horizontally: str, vertically: str, aggregation: str, sync: t.Optional[str] = None,
                  syncrun: t.Optional[str] = None, eventhandler: t.Optional[str] = None,
                  filesystem: t.Optional[str] = None, path: t.Optional[str] = None):
            with self.__lock:
                if not self.data_available:
                    return
                data = self.get_data()
                self.__queryresult = None
                for query_result_available_changed_handler in self.__query_result_available_changed_handlers:
                    query_result_available_changed_handler(False)
                self.__queryresult_reqtoken = reqtoken = object()
            def execquery():
                def average(lst):
                    return (sum(lst) / len(lst)) if len(lst) > 0 else 0
                tresult = PerformanceData.Table()
                aggreg = {"sum": sum, "average": average}[aggregation]
                for nsync in data.timingdata:
                    bsync = data.timingdata[nsync]
                    for nrun in bsync.runs:
                        srun = bsync.runs[nrun]
                        for neventhandler in srun.eventhandlers:
                            reventhandler = srun.eventhandlers[neventhandler]
                            for nfilesystem in reventhandler.filesystems:
                                hfilesystem = reventhandler.filesystems[nfilesystem]
                                for npath in hfilesystem.paths:
                                    if self.__queryresult_reqtoken != reqtoken:
                                        return
                                    ppath = hfilesystem.paths[npath]
                                    if sync and sync != bsync.name:
                                        continue
                                    if syncrun and syncrun != srun.name:
                                        continue
                                    if eventhandler and eventhandler != reventhandler.name:
                                        continue
                                    if filesystem and filesystem != hfilesystem.name:
                                        continue
                                    if not re.match(path, ppath.name):
                                        continue
                                    remo = {"synctask": bsync, "syncrun": srun, "eventhandler": reventhandler,
                                            "filesystem": hfilesystem, "path": ppath}
                                    nullobj = PerformanceData.SyncRun("-")
                                    rowname = remo.get(vertically, nullobj).name
                                    colname = remo.get(horizontally, nullobj).name
                                    tresult.add(rowname, colname, ppath.duration)
                result = []
                colnames = sorted(tresult.cols)
                rownames = sorted(tresult.rows.keys())
                for trow in rownames:
                    row = []
                    result.append(row)
                    for colname in colnames:
                        vals = tresult.rows[trow].get(colname, [])
                        row.append(aggreg(vals))
                with self.__lock:
                    if self.__queryresult_reqtoken == reqtoken:
                        self.__queryresult = PerformanceData.QueryResult(rownames, colnames, result)
                        for query_result_available_changed_handler_ in self.__query_result_available_changed_handlers:
                            query_result_available_changed_handler_(True)
            threading.Thread(target=execquery, daemon=True).start()


class LogMessageWithTime:

    def __init__(self, logmessage: 'parzzley.logger.logger.LogMessage', time: datetime.datetime):
        self.logmessage = logmessage
        self.time = time


class SyncRunLog:

    def __init__(self, sync: str, syncrun: str, messages: t.List[LogMessageWithTime],
                 begintime: datetime.datetime, endtime: datetime.datetime, crashed: bool):
        self.sync = sync
        self.syncrun = syncrun
        self.messages = messages
        self.begintime = begintime
        self.endtime = endtime
        self.crashed = crashed


def try_load_log_from_syncdir(path: str, sync: str = "?") -> t.List[SyncRunLog]:
    result = []
    logdir = f"{path}/.parzzley.control/log"
    if os.path.exists(logdir):
        for sn in os.listdir(logdir):
            fsn = f"{logdir}/{sn}"
            for srn in os.listdir(fsn):
                fsrn = f"{fsn}/{srn}"
                with open(fsrn, "r") as f:
                    content = f.read()
                    xroot = ET.fromstring(content)
                    messages = []
                    for xmsg in xroot:
                        subject = xmsg.attrib["subject"]
                        verb = xmsg.attrib["verb"]
                        comment = xmsg.attrib["comment"]
                        severity = int(xmsg.attrib["severity"])
                        symbol = xmsg.attrib["symbol"]
                        time = datetime.datetime.fromtimestamp(int(float(xmsg.attrib["time"])))
                        messages.append(LogMessageWithTime(parzzley.logger.logger.LogMessage(
                            sync, subject, verb, comment, severity, symbol), time))
                    begintime = datetime.datetime.fromtimestamp(float(xroot.attrib["begin"]))
                    endtime = datetime.datetime.fromtimestamp(float(xroot.attrib["end"]))
                    crashed = xroot.attrib.get("crashed", "") == "1"
                result.append(SyncRunLog(sn, srn, messages, begintime, endtime, crashed))
    result.sort(key=lambda x: x.begintime, reverse=True)
    return result
