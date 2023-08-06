# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Aspects control the behavior of :py:class:`parzzley.syncengine.sync.Sync` configurations.
"""

import functools
import sys
import typing as t


class Aspect:
    """
    Abstract base class for aspect implementations that build the actual behavior of a
    parzzley.syncengine.sync.Sync synchronization implementation.
    
    For implementing custom synchronization behavior, implement a subclass of this class and write some aspect hook 
    methods. An aspect hook method is just a method that follows a certain signature and is registered by means
    of `parzzley.aspect.hook` (hook()). A minimalist aspect looks like this:
    
    @verbatim
    class DoSomething(parzzley.aspect.abstractaspect.Aspect):
    
        def __init__(self):
            parzzley.aspect.abstractaspect.Aspect.__init__(self)
    
        @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_Prepare)
        def sleepwhilebeginupdatedir(self, ctx, filesystem):  # this signature must be followed!
            do_something()
    @endverbatim
    
    A sync configuration can be enhanced by this functionality by adding this aspect to one or more filesystems or
    globally (which enhances all filesystems).
    
    A hook method is called on top of a certain filesystem whenever a certain event occurs or a certain state in the
    sync controller is reached. These are actually two different things, even if it sounds similar. It essentially means
    different modes of the parzzley.aspect.hook function (read there for more).
    
    Each call to an aspect hook method gets this parameters:

    - `ctx`: a parzzley.syncengine.syncruntime.SyncEventRuntime, which holds many flow control information and
      intermediate data for the execution of one event. It also has some control flow methods.
    - `filesystem`: the parzzley.filesystem.abstractfilesystem.Filesystem the method is executed on top (it should
      execute whatever needs to be done for particul filesystem).
    
    Find some function decorators in this module for usage with aspect hook methods, e.g. for some control flow.
    """

    def __init__(self):
        pass


def hook(after: str, provides: str, before: str, event: str) -> t.Callable:
    """
    Used for registering a function as parzzley.syncengine.sync.Sync hook for implementating parts of Parzzley
    synchronization behavior (those are sometimes called 'aspect hook methods').
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.
    
    The parameters control the alignment (i.e. the ordering of all aspect hook methods) and to which event to assign
    the method.
    
    `after`, `provides` and `before` control the alignment. Please read parzzley.syncengine.sync.Sync
    for details about ordering.
    
    `event` specifies the event for which this method is to be hooked.
    
    See parzzley.syncengine.common.SyncEvent for all events. Read parzzley.syncengine.sync.Sync about how all the
    hook methods are actually executed. Read the user manual about how to directly add custom code into your Parzzley
    configuration files.
    """

    # noinspection PyProtectedMember
    def _x(fct):
        _provides = provides + "," + fct.__name__
        fct._hookinfo = getattr(fct, "_hookinfo", [])
        fct._hookinfo.append((after, _provides, before, event))
        return fct
    return _x


def execute_only_for_non_master_fs() -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only for non-master filesystems.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.
    """
    def _x(fct):
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if filesystem != ctx.masterfs else None
        return _y
    return _x


def execute_only_for_master_fs() -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only for the master filesystem.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.
    """
    def _x(fct):
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if filesystem == ctx.masterfs else None
        return _y
    return _x


def execute_only_for_master_fs_filetype(*types: str) -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only if the file has certain types in the master
    filesystem.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.

    :param types: All arguments are parzzley.syncengine.common.EntryType.
    """
    def _x(fct):
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if ctx.getinfo_current_ftype(ctx.masterfs, ctx.path) in types else None
        return _y
    return _x


def execute_only_for_slave_fs_filetype(*types: str) -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only if the file has certain types in the argument
    filesystem.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.

    :param types: All arguments are parzzley.syncengine.common.EntryType.
    """
    def _x(fct):
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if ctx.getinfo_current_ftype(filesystem, ctx.path) in types else None
        return _y
    return _x


def execute_only_if_not_already_maximally_elected() -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only if there is not already an election with
    maximum key.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.
    """
    def _x(fct):
        # noinspection PyProtectedMember
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if ctx._masterfs_key != sys.maxsize else None
        return _y
    return _x


def execute_only_if_not_update_set_skipped() -> t.Callable:
    """
    Used on aspect hook methods for executing the function body only if the update is not marked as skipped.
    
    Creates a function decorator for usage with methods of parzzley.aspect.abstractaspect.Aspect subclasses.
    """
    def _x(fct):
        @functools.wraps(fct)
        def _y(self, ctx, filesystem):
            return fct(self, ctx, filesystem) if (not ctx.is_update_set_skipped()) else None
        return _y
    return _x
