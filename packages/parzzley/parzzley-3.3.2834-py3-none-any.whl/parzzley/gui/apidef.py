# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Interface for publishing api information to the gui and for querying that infos.
"""

import typing as t

if t.TYPE_CHECKING:
    import parzzley.config.config


class InvalidUserFeedbackController:
    pass


_filesystemhelpers = []
_changeguides = []
userfeedback = InvalidUserFeedbackController()


def registerfilesystemhelper(clss):
    """
    Returns a function that registers a filesystem implementation (together with gui helpers).
    This is mostly used for providing graphical aid in making a Parzzley configuration.
    """
    def x(createhelper):
        _filesystemhelpers.append((clss, createhelper))
        return createhelper
    return x


def getregisteredfilesystemhelpers():
    """
    Returns a list of all registered filesystem implementations (together with gui helpers).
    See registerfilesystem.
    """
    return list(_filesystemhelpers)


def registerchangeguide():
    """
    Returns a function that registers a graphical change guide.
    A change guide is a graphical dialog (mostly with messageboxes, inputboxes, choiceboxes)
    that helps the user to configure a certain part of Parzzley functionality.
    """
    def x(clss):
        _changeguides.append((clss,))
        return clss
    return x


def getregisteredchangeguides():
    """
    Returns a list of all registered graphical change guides.
    See registerchangeguide.
    """
    return list(_changeguides)


def getnumstring(i: int) -> str:
    """
    Returns a nice index representation, like '2nd' for 2.
    """
    return str(i) + {"1": "st", "2": "nd", "3": "rd"}.get(str(i)[-1], "th")


def getfsname(fs: 'parzzley.config.config.ParzzleyConfiguration.Filesystem', i: int) -> str:
    """
    Returns a name for a filesystem (even if no 'name' param is set).
    """
    return fs.name or getnumstring(i)
