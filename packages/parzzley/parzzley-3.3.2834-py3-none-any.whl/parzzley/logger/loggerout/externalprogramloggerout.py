# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import parzzley.config.configpiece
import parzzley.logger.loggerout.abstractloggerout
import parzzley.tools.common


class ExternalProgramLoggerout(parzzley.logger.loggerout.abstractloggerout.Loggerout):

    def __init__(self, **kwa):
        super().__init__()
        self.cmdline = parzzley.config.configpiece.getlist(kwa, "cmdline")
        self.cont = ""

    def log(self, content):
        self.cont += content

    def flush(self, wasused):
        if wasused:
            cmdline = []
            for x in self.cmdline:
                if x.endswith("{}"):
                    t = None
                    i = 0
                    while t is None or os.path.exists(t):
                        t = f"/tmp/parzzley.{i}"
                        i += 1
                    with open(t, "w") as f:
                        f.write(self.cont)
                    cmdline.append(x[:-2] + t)
                elif x.endswith("[]"):
                    cmdline.append(x[:-2] + self.cont)
                else:
                    cmdline.append(x)
            parzzley.tools.common.call(cmdline)
