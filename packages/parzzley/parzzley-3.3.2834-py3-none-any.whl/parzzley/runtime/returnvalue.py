# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Parzzley engine return values.
"""


class ReturnValue:
    """
    Flags that roughly describe the success of a synchronization run.
    The return value you get on command line is composed from this flags.
    """

    #: Everything went perfectly okay.
    SUCCESS = 0

    #: An error occurred.
    ERROR = 1

    #: An error occurred in the initialization of the synchronization itself.
    ERROR_INITIALIZATION = 2 | ERROR

    #: An error occurred while enabling one of the specified parzzley.preparation.abstractpreparation.Preparation before
    #: execution.
    ERROR_PREPARATION = 4 | ERROR

    #: An error occurred while executing the synchronization itself (excluding preparations, ...).
    ERROR_EXECUTION = 8 | ERROR

    #: An error occurred while disabling one of the specified parzzley.preparation.abstractpreparation.Preparation after
    #: execution.
    ERROR_UNPREPARATION = 16 | ERROR

    #: Something remained dirty and needs a new synchronization run soon.
    DIRTY = 32
