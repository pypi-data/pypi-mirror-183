# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.exceptions
import parzzley.logger
import parzzley.syncengine.common


# noinspection PyProtectedMember
class HighLevelCustomization(parzzley.aspect.abstractaspect.Aspect):
    """
    Executes high level customization handlers. They are loaded directly from the sync tree, whenever a
    `.parzzley.custom.py` file exists.
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "highlevel", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def init(self, ctx, filesystem):
        if not hasattr(ctx.syncglobaldata, "highlevelscripts"):
            ctx.syncglobaldata.highlevelscripts = []
            ctx.syncglobaldata.highlevelscripts_loaded = [None, ]

    @parzzley.aspect.hook("", "highlevel", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_Prepare)
    def loadcustomizations(self, ctx, filesystem):
        if ctx.path not in ctx.syncglobaldata.highlevelscripts_loaded:
            p = ctx.path + "/.parzzley.custom.py"
            if filesystem.exists(p):
                script = {}
                try:
                    exec(filesystem.readfromfile(p).decode(), script)
                    script["scriptsource"] = ctx.path
                    ctx.syncglobaldata.highlevelscripts.append(script)
                    ctx.syncglobaldata.highlevelscripts_loaded.append(ctx.path)
                except Exception as e:
                    skiponerror = script.get("skiponerror", False)
                    if skiponerror:
                        ctx.log(verb="custom script skipped due to problems", comment=str(e),
                                severity=parzzley.logger.Severity.MOREIMPORTANT)
                    else:
                        raise

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "highlevel", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def unloadcustomizations(self, ctx, filesystem):
        if ctx.syncglobaldata.highlevelscripts_loaded[-1] == ctx.path:
            ctx.syncglobaldata.highlevelscripts.pop()
            ctx.syncglobaldata.highlevelscripts_loaded.pop()

    class BeforeUpdateEvent:

        CONTINUE_TOUCHED = "CONTINUE_TOUCHED"
        CONTINUE_UNTOUCHED = "CONTINUE_UNTOUCHED"

        def __init__(self, controller, isnew, isdeleted, ischanged, scriptsource):
            self.controller = controller
            self.runtime = controller.runtime
            self.continuewith = None
            self.isnew = isnew
            self.isdeleted = isdeleted
            self.ischanged = ischanged
            self.scriptsource = scriptsource

        def continue_touched(self):
            self.continuewith = HighLevelCustomization.BeforeUpdateEvent.CONTINUE_TOUCHED

        def continue_untouched(self):
            self.continuewith = HighLevelCustomization.BeforeUpdateEvent.CONTINUE_UNTOUCHED

    class BeforeUpdateHandlerTerminatedWithoutDecision(parzzley.exceptions.ParzzleyError):

        def __init__(self):
            super().__init__("A custom beforeupdate event exited without calling either event.continue_touched or"
                             " event.continue_untouched.")

    @parzzley.aspect.hook("", "highlevel", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_Prepare)
    @parzzley.aspect.execute_only_for_master_fs()
    def callonbeforeupdate(self, ctx, filesystem):
        for h in reversed(ctx.syncglobaldata.highlevelscripts):
            hf = h.get("beforeupdate", None)
            skiponerror = h.get("skiponerror", False)
            if hf:
                isnew = not ctx.getinfo_lastrun_exists(filesystem, ctx.path)
                isdeleted = not ctx.getinfo_current_exists(filesystem, ctx.path)
                ischanged = (not isnew) and (not isdeleted) and \
                    ctx.getinfo_lastrun_mtime(filesystem, ctx.path) != ctx.getinfo_current_mtime(filesystem, ctx.path)
                highevent = HighLevelCustomization.BeforeUpdateEvent(ctx.sync, isnew, isdeleted, ischanged,
                                                                     h["scriptsource"])
                try:
                    hf(filesystem, ctx.path, highevent)
                except Exception as e:
                    if skiponerror:
                        ctx.log(verb="custom beforeupdate event skipped due to problems", comment=str(e),
                                severity=parzzley.logger.Severity.MOREIMPORTANT)
                        highevent.continue_touched()
                    else:
                        raise
                continuewith = highevent.continuewith
                if continuewith is None:
                    raise HighLevelCustomization.BeforeUpdateHandlerTerminatedWithoutDecision()
                elif continuewith == HighLevelCustomization.BeforeUpdateEvent.CONTINUE_TOUCHED:
                    from parzzley.aspect.collectinformation import CollectInformation
                    # noinspection PyCallByClass,PyTypeChecker
                    CollectInformation.collectinformation_collectinfo(self, ctx, filesystem)
