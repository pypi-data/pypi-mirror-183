# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Abstract base class for log formatters.
"""

import typing as t

if t.TYPE_CHECKING:
    import parzzley.logger.logger


class Logformat:
    """
    Abstract base class for log message formatters (html, plain, ...).
    For existing implementations, see parzzley.logger.formatter.
    """

    def __init__(self):
        pass

    def header(self) -> str:
        """
        Returns a header string for the log output (like an html header).
        """
        return ""

    # noinspection PyUnusedLocal
    def log(self, logmessage: 'parzzley.logger.logger.LogMessage') -> str:
        """
        Renders the information for one log message into a formatted string (plaintext, html, ...).

        :param logmessage: The parzzley.logger.logger.LogMessage log message.
        """
        return ""

    def footer(self) -> str:
        """
        Returns a footer string for the log output (like an html footer).
        """
        return ""
