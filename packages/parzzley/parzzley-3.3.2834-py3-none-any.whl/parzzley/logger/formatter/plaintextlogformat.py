# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import math

import parzzley.logger
import parzzley.logger.formatter.abstractlogformat


# noinspection PyProtectedMember
class PlaintextLogformat(parzzley.logger.formatter.abstractlogformat.Logformat):

    def __init__(self, maxlen=80, color=None):
        super().__init__()
        self.maxlen = maxlen
        self.color = color

    def header(self):
        return ""

    def log(self, logmessage):
        result = ""
        sevtxtlen = int(math.ceil(parzzley.logger.Severity._MAX_TYPICAL / 2.0))
        if logmessage.severity <= parzzley.logger.Severity._MAX_TYPICAL:
            sevstring = (("." * logmessage.severity).replace("..", ":") + " " * sevtxtlen)[0:sevtxtlen]
        else:
            sevstring = " " * sevtxtlen
        pr = datetime.datetime.now().strftime("%Y%m%d %H%M%S") + " " + sevstring + \
            " " + (logmessage.symbol + " ")[0] + " "
        fullmsg = str(logmessage.sync) + " " + str(logmessage.subject) + \
            ("" if (not logmessage.verb) else (" " + str(logmessage.verb))) + \
            ("" if (not logmessage.comment) else (" " + str(logmessage.comment)))
        for line in fullmsg.split("\n"):
            while len(line) > 0:
                il = self.maxlen - len(pr)
                if len(line) > il:
                    sp = line.rfind(" ", 0, il)
                    if sp > -1:
                        il = sp
                _line = line[0:il].strip()
                line = line[il:].strip()
                result += (pr if result == "" else " " * len(pr)) + _line + "\n"
        if self.color:
            result = f"\033[9{self.color}m{result}\033[0m"
        return result

    def footer(self):
        return ""
