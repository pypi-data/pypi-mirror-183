# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Parzzley.

Very roughly, Parlsey consists of

- A synchronization task execution engine in :py:mod:`parzzley.syncengine` (and :py:mod:`parzzley.runtime`)
- Lots of program pieces that bring the actual synchronization behavior in parzzley.aspect
- Filesystem implementations in :py:mod:`parzzley.filesystem`
- Some helping hands at different places like :py:mod:`parzzley.logger`, :py:mod:`parzzley.preparation`
  or :py:mod:`parzzley.tools`
- Graphical user interfaces in :py:mod:`parzzley.gui`
"""
