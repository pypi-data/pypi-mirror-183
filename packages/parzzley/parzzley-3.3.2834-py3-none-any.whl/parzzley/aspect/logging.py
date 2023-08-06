# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.config.configpiece
import parzzley.syncengine.common


class Logging(parzzley.aspect.abstractaspect.Aspect):
    """
    Switchable logging by situation.
    """

    def __init__(self, *, logcreate="1", logremove="1", logupdate="1", logproblem="1"):
        super().__init__()
        self.logcreate = parzzley.config.configpiece.getbool(logcreate)
        self.logremove = parzzley.config.configpiece.getbool(logremove)
        self.logupdate = parzzley.config.configpiece.getbool(logupdate)
        self.logproblem = parzzley.config.configpiece.getbool(logproblem)

    @parzzley.aspect.hook("", "logging", "", event=parzzley.syncengine.common.SyncEvent.LogUpdate)
    def _logupdate(self, ctx, filesystem):
        """
        Logs an entry update (only hooked if this is activated in aspect configuration).
        """
        if self.logupdate and filesystem == ctx.logfs:
            ctx.log(subject=ctx.subject, verb=ctx.verb, comment=ctx.comment, symbol=ctx.symbol, severity=ctx.severity)

    @parzzley.aspect.hook("", "logging", "", event=parzzley.syncengine.common.SyncEvent.LogRemove)
    def _logremove(self, ctx, filesystem):
        """
        Logs an entry removal (only hooked if this is activated in aspect configuration).
        """
        if self.logremove and filesystem == ctx.logfs:
            ctx.log(subject=ctx.subject, verb=ctx.verb, comment=ctx.comment, symbol=ctx.symbol, severity=ctx.severity)

    @parzzley.aspect.hook("", "logging", "", event=parzzley.syncengine.common.SyncEvent.LogCreate)
    def _logcreate(self, ctx, filesystem):
        """
        Logs an entry creation (only hooked if this is activated in aspect configuration).
        """
        if self.logcreate and filesystem == ctx.logfs:
            ctx.log(subject=ctx.subject, verb=ctx.verb, comment=ctx.comment, symbol=ctx.symbol, severity=ctx.severity)

    @parzzley.aspect.hook("", "logging", "", event=parzzley.syncengine.common.SyncEvent.LogProblem)
    def _logproblem(self, ctx, filesystem):
        """
        Logs a problem (only hooked if this is activated in aspect configuration).
        """
        if self.logproblem and filesystem == ctx.logfs:
            ctx.log(subject=ctx.subject, verb=ctx.verb, comment=ctx.comment, symbol=ctx.symbol, severity=ctx.severity)
