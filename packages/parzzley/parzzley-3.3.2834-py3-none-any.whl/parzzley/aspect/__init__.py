# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Aspects control the behavior of :py:class:`parzzley.syncengine.sync.Sync` configurations. Each feature should be
encapsulated as one subclass of :py:class:`parzzley.aspect.abstractaspect.Aspect` that hooks some event handlers into
the processing chain (so-called aspect hook methods).

This module also contains some function decorators for usage with aspect hook methods.
"""

from parzzley.aspect.abstractaspect import hook, execute_only_for_master_fs, execute_only_for_master_fs_filetype, \
    execute_only_for_non_master_fs, execute_only_for_slave_fs_filetype, execute_only_if_not_already_maximally_elected, \
    execute_only_if_not_update_set_skipped
