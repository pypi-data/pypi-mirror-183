# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Abstract base class for a logger output.
"""


class Loggerout:
    """
    Abstract base class for log message sinks.
    For existing implementations, see parzzley.logger.loggerout.
    """

    def __init__(self):
        pass

    def log(self, content: str) -> None:
        """
        Writes the rendered content to the logger (can be log messages, html header or footer, ...).
        """
        pass

    def flush(self, wasused: bool) -> None:
        """
        Commits the log content to the sink and closes the logger.

        :param wasused: If there was any useful logged message (instead of just headers and footers).
        """
        pass
