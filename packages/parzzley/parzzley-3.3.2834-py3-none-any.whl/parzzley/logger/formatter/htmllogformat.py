# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.logger
import parzzley.logger.formatter.abstractlogformat


class HtmlLogformat(parzzley.logger.formatter.abstractlogformat.Logformat):

    def __init__(self):
        super().__init__()
        self.bgtoggle = True
        self.lastsync = object()

    def header(self):
        return """
        <html><head><style><!--
            td { padding: 2pt;}
            th { padding: 3pt; margin:0 3pt 0 0; font-size:1.2em; text-align:left; }
        --></style></head><body>
        <table style='border-collapse:collapse;border-width:0px;width:100%;'>
        """

    def log(self, logmessage):
        color = HtmlLogformat.get_htmlcolor_for_severity(logmessage.severity)
        self.bgtoggle = not self.bgtoggle
        backgroundcolor = "#EEEEEE" if self.bgtoggle else "#DDDDDD"
        if logmessage.sync != self.lastsync:
            header = f"<tr>\n<th colspan='4'>{logmessage.sync}</th></tr>"
            self.lastsync = logmessage.sync
        else:
            header = ""
        return (f"{header}<tr style='color:{color};background-color:{backgroundcolor};'><td>{logmessage.symbol}</td>"
                f" <td>{logmessage.subject}</td> <td style='font-weight:bold;'>{logmessage.verb}</td>"
                f" <td>{logmessage.comment}</td></tr>")

    def footer(self):
        return "</table></body></html>\n"

    # noinspection PyProtectedMember
    @staticmethod
    def get_htmlcolor_for_severity(severity):
        if severity <= parzzley.logger.Severity.DEBUG:
            return "#adcbc9"
        if severity == parzzley.logger.Severity.INFO:
            return "#222222"
        elif severity == parzzley.logger.Severity.IMPORTANT:
            return "#80651b"
        elif severity == parzzley.logger.Severity.MOREIMPORTANT:
            return "#9d1e1e"
        elif severity <= parzzley.logger.Severity._MAX_TYPICAL:
            return "#ff0000"
        else:
            return "#000000"
