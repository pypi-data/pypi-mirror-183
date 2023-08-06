# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Default implementation for path acceptors as e.g. used in
:py:class:`parzzley.aspect.applypathacceptor.ApplyPathAcceptor`.
"""

import os
import typing as t

import parzzley.tools.common

if t.TYPE_CHECKING:
    import parzzley.filesystem.abstractfilesystem


# noinspection PyUnusedLocal
def defaultpathacceptor(path: str, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem') -> bool:
    """
    A path acceptor that skips file names with some known 'backup pattern', like ending with `~`.
    """
    bn = os.path.basename(path)
    if bn.endswith("~"):
        return False
    if bn.endswith(".kate-swp"):
        return False
    if bn.startswith(".#"):
        return False
    if bn == "__pycache__":
        return False
    return True


def builtinpathacceptor(path: str, fs: 'parzzley.filesystem.abstractfilesystem.Filesystem') -> bool:
    """
    A path acceptor that skips Parzzley control stuff. It is always used.
    """
    if fs.control_directory.startswith("./"):
        return parzzley.tools.common.abspath("///" + path) != parzzley.tools.common.abspath("///" + fs.control_directory)
    else:
        return True
