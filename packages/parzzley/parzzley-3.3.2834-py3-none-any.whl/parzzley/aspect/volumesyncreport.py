# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import time
import traceback
# noinspection PyPep8Naming
import xml.etree.cElementTree as ET

import parzzley.aspect.abstractaspect
import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.common


# noinspection PyProtectedMember
class VolumeSyncReport(parzzley.aspect.abstractaspect.Aspect):
    """
    Writes some report data to the volume.
    """

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.CloseSync)
    def syncvolumereport_write(self, ctx, filesystem):
        """
        Writes the report.
        """
        log_storage = parzzley.runtime.datastorage.get_storage_department(
            ctx, "log", location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
            scope=parzzley.runtime.datastorage.StorageScope.PER_SYNC)
        xroot = ET.Element("parzzley_log")
        xroot.set("version", "1")
        xroot.set("syncrun", ctx.runname)
        xroot.set("begin", str(ctx.benchmark._begintime))
        xroot.set("end", str(time.time()))
        for ltime, name, subject, verb, comment, severity, symbol in ctx._logmessages:
            if name == ctx.sync.name:
                xmsg = ET.SubElement(xroot, "message")
                xmsg.set("time", str(ltime))
                xmsg.set("symbol", str(symbol))
                xmsg.set("subject", str(subject))
                xmsg.set("severity", str(severity))
                xmsg.set("verb", str(verb))
                xmsg.set("comment", str(comment))
        errortext = getattr(ctx, "errortext", "")
        if errortext:
            xmsg = ET.SubElement(xroot, "message")
            xmsg.set("time", str(time.time()))
            xmsg.set("symbol", "E")
            xmsg.set("subject", "")
            xmsg.set("severity", "6")
            xmsg.set("verb", "unhandled error")
            xmsg.set("comment", errortext)
            xroot.set("crashed", "1")
        # argh; just for prettifying...
        import xml.dom.minidom
        bcontent = xml.dom.minidom.parseString(ET.tostring(xroot)).toprettyxml(indent="    ").encode()
        name = ctx.runname
        logfs = log_storage.get_filesystem(filesystem=filesystem)
        try:
            logfs.writetofile(name, bcontent)
            for f in logfs.listdir(""):
                if (datetime.datetime.now()-logfs.getmtime(f)) > datetime.timedelta(days=30):
                    logfs.removefile(f)
        except OSError:
            ctx.log(subject=logfs.name, verb="Errors while writing log", comment=traceback.format_exc(), symbol="E",
                    severity=parzzley.logger.Severity.DEBUG)
