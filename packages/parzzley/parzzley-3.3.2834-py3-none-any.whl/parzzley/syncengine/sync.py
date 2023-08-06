# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Find the synchronization implementation in :py:class:`Sync` and many other stuff in submodules.
"""

import bz2
import traceback
import typing as t

import parzzley.aspect.abstractaspect
import parzzley.aspect.baseinfrastructure
import parzzley.config.configpiece
import parzzley.exceptions
import parzzley.filesystem.abstractfilesystem
import parzzley.logger
import parzzley.preparation.abstractpreparation
import parzzley.preparation.preparator
import parzzley.runtime.datastorage
import parzzley.runtime.returnvalue
import parzzley.syncengine.common
import parzzley.syncengine.syncruntime
import parzzley.tools.PyDepsEngine.depsengine

if t.TYPE_CHECKING:
    import parzzley.runtime.runtime


# noinspection PyProtectedMember
class Sync:
    """
    The synchronization implementation.
    
    Parzzley configuration files typically create some instances of this class.
    
    The entire synchronization work takes place by all hook methods, hooked by all specified aspects.
    Read :py:meth:`Sync.executeevent` for more details.
    """

    class EventHandler:
        """
        A data structure that represents one hooked instance of a hook method (i.e. bound to a certain `funcargs`,
        including the filesystem).
        """

        def __init__(self, event: str, func: t.Callable, funcargs: t.Dict[str, t.Optional[t.Any]]):
            self.event = event
            self.func = func
            self.funcargs = funcargs

    def __init__(self, *objlist: t.Union[parzzley.filesystem.abstractfilesystem.Filesystem,
                                         parzzley.aspect.abstractaspect.Aspect,
                                         parzzley.preparation.abstractpreparation.Preparation], name: str,
                 interval: str = "0s", warn_after: str = "7d", warn_interval: str = "7d",
                 benchmark_data_size: int = 30):
        """
        :param name: The name for this synchronization.
        :param interval: The synchronization interval (the engine will skip this synchronization, if the last
                         successful run is not at least this interval ago.
        :param warn_after: The interval after which a warning is logged when no successful run took place.
        :param warn_interval: The interval for subsequent warnings when no successful run took place.
        :param benchmark_data_size: The maximum capacity used for collecting benchmark data (in MB).
        """
        self.name = name
        self.interval = parzzley.config.configpiece.gettimedelta(interval)
        self.warn_after = parzzley.config.configpiece.gettimedelta(warn_after)
        self.warn_interval = parzzley.config.configpiece.gettimedelta(warn_interval)
        self.benchmark_data_size = int(benchmark_data_size)
        self.filesystems = []
        self.preparations = []
        self.aspects = []
        for x in objlist:
            if isinstance(x, parzzley.filesystem.abstractfilesystem.Filesystem):
                if x.name == "":
                    raise parzzley.syncengine.common.SyncConfigurationError("name must not be empty")
                if len([y for y in self.filesystems if y.name == x.name]) > 0:
                    raise parzzley.syncengine.common.SyncConfigurationError("names must be unique")
                self.filesystems.append(x)
            elif isinstance(x, parzzley.aspect.abstractaspect.Aspect):
                self.aspects.append(x)
            elif isinstance(x, parzzley.preparation.abstractpreparation.Preparation):
                self.preparations.append(x)
            else:
                raise parzzley.syncengine.common.SyncConfigurationError(f"forbidden parameter: {x}")

    def _execute_helper(self, runtime: 'parzzley.runtime.runtime.RuntimeData',
                        preparations: t.List[parzzley.preparation.abstractpreparation.Preparation]) -> None:
        if len(preparations) == 0:
            try:
                runtime.log(verb="Start executing", severity=parzzley.logger.Severity.DEBUG)
                crashed = True
                self.runtime = runtime.clone(merge_also_from=parzzley.syncengine.syncruntime.SyncRuntime())
                self.runtime._syncruntime_init()
                runtime.successtracker.begincall(self)
                self.runtime.benchmark.beginsync()
                try:
                    self._handlers = {}
                    self._hook_aspect(parzzley.aspect.baseinfrastructure.BaseInfrastructure(), self.filesystems)
                    for aspect in self.aspects:
                        self._hook_aspect(aspect, self.filesystems)
                    for fs in self.filesystems:
                        for aspect in fs.aspects:
                            self._hook_aspect(aspect, [fs])
                        fs.initialize_late(self, runtime)
                        fs.checkalive()
                    self.runtime._verify_filelists_cookies()
                    try:
                        self.executeevent(parzzley.syncengine.common.SyncEvent.BeginSync, eventcontext=self.runtime)
                        self.sync_directory("")
                        self.executeevent(parzzley.syncengine.common.SyncEvent.EndSync, eventcontext=self.runtime)
                    except Exception as e:
                        self.executeevent(parzzley.syncengine.common.SyncEvent.CloseSync,
                                          eventcontext=self.runtime.clone(
                                              merge_also={"errortext": traceback.format_exc()}))
                        parzzley.preparation.preparator.Preparator._logandthrowexception(
                            runtime, parzzley.exceptions.ErrorExecutingExecutionError, e)
                    self.executeevent(parzzley.syncengine.common.SyncEvent.CloseSync, eventcontext=self.runtime.clone())
                    crashed = False
                    wasdirty = (runtime.get_retval() & parzzley.runtime.returnvalue.ReturnValue.DIRTY) > 0
                    wasdirtytxt = " (but skipped some items)" if wasdirty else ""
                    runtime.log(verb="Successfully executed" + wasdirtytxt, severity=parzzley.logger.Severity.DEBUG)
                    runtime.successtracker.successfulcall(self)
                    if wasdirty:
                        runtime.successtracker.forceexecution(self)
                finally:
                    self.runtime.benchmark.endsync()
                    benchmarkresult = bz2.compress(self.runtime.benchmark.get_report())
                    sync_benchmark_storage = parzzley.runtime.datastorage.get_storage_department(
                        self.runtime, "sync_benchmark",
                        location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
                        scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
                    for fs in self.filesystems:
                        try:
                            if fs._is_hot:
                                sync_benchmark_fs = sync_benchmark_storage.get_filesystem(filesystem=fs)
                                sync_benchmark_fs.writetofile(self.runtime.runname, benchmarkresult)
                                bfiles = [(x, sync_benchmark_fs.getmtime(x), sync_benchmark_fs.getsize(x))
                                          for x in sync_benchmark_fs.listdir("")]
                                bfiles.sort(key=lambda x: x[1], reverse=True)
                                while sum([x[2] for x in bfiles]) > self.benchmark_data_size * 1000000:
                                    sync_benchmark_fs.removefile(bfiles.pop()[0])
                        except Exception:
                            runtime.log(verb="Errors while writing benchmark data", subject=fs.name,
                                        severity=parzzley.logger.Severity.DEBUG, symbol="E",
                                        comment=traceback.format_exc())
                    try:
                        for fs in self.filesystems:
                            if fs._is_hot:
                                fs.shutdown(self, runtime)
                    finally:
                        for fs in self.filesystems:
                            if not crashed:
                                _y = self.runtime._filelists_curr[fs].first.save()
                            else:
                                _y = self.runtime._filelists_curr[fs].second.save()
                            self.runtime._filelists_storage.set_value(path=fs.name, value=_y)
            except Exception as e:
                runtime.set_retval(parzzley.runtime.returnvalue.ReturnValue.ERROR_EXECUTION)
                parzzley.preparation.preparator.Preparator._logandthrowexception(
                    runtime, parzzley.exceptions.ErrorExecutingExecutionError, e)
        else:
            with parzzley.preparation.preparator.Preparator(runtime, preparations[0]) as p:
                if p.enabled:
                    self._execute_helper(runtime, preparations[1:])

    def execute(self, runtime: 'parzzley.runtime.runtime.RuntimeData', force: bool = False) -> bool:
        """
        Used by the Parzzley engine for executing the sync run.
        """
        if (not force) and runtime.successtracker.shall_skip(self):
            runtime.log(verb="Task execution skipped", severity=parzzley.logger.Severity.DEBUGVERBOSE)
            return False
        try:
            for fs in self.filesystems:
                fs.initialize(self, runtime)
        except Exception as e:
            runtime.set_retval(parzzley.runtime.returnvalue.ReturnValue.ERROR_INITIALIZATION)
            parzzley.preparation.preparator.Preparator._logandthrowexception(
                runtime, parzzley.exceptions.ErrorInitializingExecutionError, e)
        self._execute_helper(runtime, self.preparations)
        return True

    def sync_directory(self, path: str) -> None:
        """
        Executes the sub workflow for synchronizing one directory.
        """
        ctx = self.runtime.clone()
        self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateDir_Prepare, eventcontext=ctx, path=path,
                          entrylist=set())
        self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateDir_ListDir, eventcontext=ctx, path=path)
        for f in ctx.entrylist:
            fullf = f"{ctx.path}/{f}"
            _ctx = ctx.clone(merge_also_from=parzzley.syncengine.syncruntime.SyncEventRuntime(fullf))
            self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_BeforeElectMaster, eventcontext=_ctx)
            self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster, eventcontext=_ctx)
            erroneous = False
            if _ctx.masterfs != parzzley.syncengine.common.SKIP:
                _ctx.log(subject=_ctx.path, comment=f"elected master: {_ctx.masterfs}",
                         severity=parzzley.logger.Severity.DEBUGVERBOSE)
                _ctx.existsonmaster = self.runtime.getinfo_current_exists(_ctx.masterfs, _ctx.path)
                for _fs in self.filesystems:
                    _fs.checkalive()
                self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_CheckConflicts, eventcontext=_ctx)
                if _ctx.get_conflicts():
                    self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_ResolveConflicts,
                                      eventcontext=_ctx)
                for _fs in self.filesystems:
                    _fs.checkalive()
                conflicts = _ctx.get_conflicts()
                if conflicts:
                    erroneous = True
                    for tup in conflicts:
                        if "temp" not in tup:
                            desc = ", ".join([s for s in tup if isinstance(s, str)])
                            conflictfs = [s for s in tup
                                          if isinstance(s, parzzley.filesystem.abstractfilesystem.Filesystem)][0]
                            _ctx.logproblem(conflictfs, _ctx.path, verb="has conflicts", comment=desc)
                    self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_SkippedDueConflicts,
                                      eventcontext=_ctx)
                else:
                    self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_Update_Prepare, eventcontext=_ctx)
                    _ctx.existsonmaster = self.runtime.getinfo_current_exists(_ctx.masterfs, _ctx.path)
                    if _ctx.existsonmaster:
                        self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster,
                                          eventcontext=_ctx)
                    else:
                        self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_Update_NotExistsInMaster,
                                          eventcontext=_ctx)
                self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateItem_AfterUpdate, eventcontext=_ctx)
            else:
                _ctx.log(subject=_ctx.path, comment=f"skipped by election: {_ctx.masterfs}",
                         severity=parzzley.logger.Severity.DEBUGVERBOSE)
            if not erroneous:
                mtag = "S~" if _ctx.is_update_marked_bad() else "S+"
                for _fs in self.filesystems:
                    _ctx.setinfo_current_addtag(_fs, fullf, mtag)
        self.executeevent(parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate, eventcontext=ctx, path=path)

    def executeevent(self, event: str, eventcontext: parzzley.syncengine.syncruntime.SyncEventRuntime,
                     **eventparams: str) -> None:
        """
        Executes an event by name. This means executing the aspect hooks and enforcing the ordering rules.
        
        The technical realization of the workflow bases on an event-based execution engine.
        The events (in parzzley.syncengine.common.SyncEvent) define the workflow stages of the engine.
        The engine essentially executes aspect hook methods (see parzzley.aspect.abstractaspect.Aspect) on filesystems
        (see parzzley.filesystem.abstractfilesystem.Filesystem) for each event.
        
        The entire synchronization behavior is implemented by a horde of builtin aspects and optionally also custom 
        ones.
        To be exact: The configuration for a synchronization task specifies the synchronization behavior by specifying
        a list of aspect instances. The list of aspects can be specified and configured for each filesystem
        individually and globally (which is equal to assigning it to each filesystem).
        
        Whenever an aspect is assigned to one filesystem by that means, it hooks some methods into some events for that
        filesystem.
        
        The order of the aspect hook executions is controlled by the symbol list `after`, `provides` and `before`.
        Each is a list of string symbols, e.g. `["foo", "bar", "baz"]` 
        (you can often also write one comma-separated string like `"foo,bar,baz"`). 
        The order of execution is chosen in a way it strictly follows this rules:
        
        - A hook method is never executed when it contains one symbol in `after` that also exists in a `provides` list
          of any hook that is not yet executed (use it for after-dependencies; the typical ones).
        - A hook method is never executed when it contains one symbol in `provides` that also exists in a `before` list
          of any hook that is not yet executed (use it for before-dependencies).
        
        Example: A hook with `after="",provides="foo",before=""` will be executed before a one with
        `after="foo",provides="bar",before=""` and after a one with `after="",provides="baz",before="foo"`.
        
        Specifying those three lists for each aspect hook method implies the execution order that must be used
        whenever certain hook methods depend on results or actions of other hook methods.
        
        @note For each hook, the function name itself is always implicitly added to `provides` by the engine.
        
        Read the manual for a high-level description of the workflow.
        
        For advanced usage in special situations:
        
        - A symbol in `after` and `before` can begin with a `*`. If so, it does not raise a validation error if this 
          symbol is not available at all.

        :param event: The event to execute. See parzzley.syncengine.common.SyncEvent.
        :param eventcontext: The parzzley.syncengine.syncruntime.SyncEventRuntime control interface for this execution.
        :param eventparams: Additional keyword parameters are added to `eventcontext` (convenience).
        """
        self.runtime.benchmark.beginsyncevent(event, getattr(eventcontext, "path", "") or eventparams.get("path"))
        try:
            handlers = self._get_eventhandlers(event)
            for k in eventparams.keys():
                setattr(eventcontext, k, eventparams[k])
            for handler in handlers:
                fs = handler.funcargs.get("filesystem", None)
                self.runtime.benchmark.beginsynceventhandler(handler, fs.name if fs else "")
                try:
                    handler.func(ctx=eventcontext, **handler.funcargs)
                finally:
                    self.runtime.benchmark.endsynceventhandler()
        finally:
            self.runtime.benchmark.endsyncevent()

    def _get_eventhandlers(self, event: str) -> t.List['Sync.EventHandler']:
        """
        Returns a list of event handlers for an event.
        """
        eh = self._handlers.get(event, None)
        if eh:
            return eh.processor.get_objects()
        else:
            return []

    def _hook_aspect(self, aspect: parzzley.aspect.abstractaspect.Aspect,
                     fss: t.List[parzzley.filesystem.abstractfilesystem.Filesystem]) -> None:
        """
        Request to hook program logic into certain events. Used internally. 
        See parzzley.aspect.abstractaspect.hook about how to hook custom synchronization logic.
        """
        hookinfos = []
        for d in dir(aspect):
            x = getattr(aspect, d)
            if hasattr(x, "_hookinfo"):
                for hi in x._hookinfo:
                    hookinfos.append((x,) + hi)
        glst = parzzley.tools.PyDepsEngine.depsengine.Processor.Object._getlist
        for fs in fss:
            for hi in hookinfos:
                func, afterrequired, provides, beforerequired, event = hi
                afteroptional = [x[1:] for x in glst(afterrequired) if x.startswith("*")]
                afterrequired = [x for x in glst(afterrequired) if not x.startswith("*")]
                beforeoptional = [x[1:] for x in glst(beforerequired) if x.startswith("*")]
                beforerequired = [x for x in glst(beforerequired) if not x.startswith("*")]
                hlist = self._handlers.get(event, None)
                if not hlist:
                    hlist = self._handlers[event] = parzzley.tools.PyDepsEngine.depsengine.Engine()
                    hlist.processor = hlist.add_processor(presort_keyfct=lambda xx: xx.o.func.__name__)
                hlist.add_object(Sync.EventHandler(event, func, {"filesystem": fs}),
                                 own=provides, afterrequired=afterrequired, beforerequired=beforerequired,
                                 afteroptional=afteroptional, beforeoptional=beforeoptional)
