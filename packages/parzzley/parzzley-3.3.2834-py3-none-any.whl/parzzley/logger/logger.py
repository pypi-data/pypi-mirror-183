# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Logging messages.
"""

import typing as t

if t.TYPE_CHECKING:
    import parzzley.logger.formatter.abstractlogformat
    import parzzley.logger.loggerout.abstractloggerout


class Severity:
    """
    Enumeration for the severity of log messages.
    """

    DEBUGVERBOSE = 1
    DEBUG = 2
    INFO = 3
    IMPORTANT = 4
    MOREIMPORTANT = 5
    ERROR = 6

    #: This is the maximum severity value for typical log messages. Everything above is for special
    #: purpose categories.
    _MAX_TYPICAL = ERROR


class LogMessage:
    """
    A single log message.
    
    This is used in the logging backend. You do not need this class just for logging.
    """

    def __init__(self, sync: str, subject: str, verb: str, comment: str, severity: int, symbol: str):
        self.sync = sync
        self.subject = subject
        self.verb = verb
        self.comment = comment
        self.severity = severity
        self.symbol = symbol


class Logger:
    """
    Used by higher layers for logging messages.
    Contains a parzzley.logger.formatter.abstractlogformat.Logformat and 
    a parzzley.logger.loggerout.abstractloggerout.Loggerout and defines which severity
    span should actually be logged.
    """

    # noinspection PyProtectedMember
    def __init__(self, formatter: 'parzzley.logger.formatter.abstractlogformat.Logformat',
                 loggerout: 'parzzley.logger.loggerout.abstractloggerout.Loggerout',
                 minseverity: t.Optional[int] = Severity.INFO, maxseverity: t.Optional[int] = None,
                 enabled: bool = True):
        if maxseverity is None:
            if minseverity <= Severity._MAX_TYPICAL:
                maxseverity = Severity._MAX_TYPICAL
            else:
                maxseverity = minseverity
        self.loggerout = loggerout
        self.formatter = formatter
        self.minseverity = minseverity
        self.maxseverity = maxseverity
        self.enabled = enabled
        content = self.formatter.header()
        self.loggerout.log(content)
        self.used = False

    def log(self, sync: str, subject: str, verb: str, comment: str, severity: int, symbol: str) -> None:
        """
        Logs a message.

        :param sync: The name of the synchronization task that is presented as the source (arbitrary string).
        :param subject: The subject string.
        :param verb: The verb string.
        :param comment: The comment string.
        :param severity: The severity (parzzley.logger.logger.Severity).
        :param symbol: The event symbol string.
        """
        if self.enabled and self.minseverity <= severity <= self.maxseverity:
            logmessage = LogMessage(sync, subject, verb, comment, severity, symbol)
            content = self.formatter.log(logmessage)
            if content is not None:
                self.loggerout.log(content)
                self.used = True

    def flush(self) -> None:
        """
        Closes the logger and commits the content.
        """
        if self.enabled:
            content = self.formatter.footer()
            self.loggerout.log(content)
            self.loggerout.flush(self.used)
