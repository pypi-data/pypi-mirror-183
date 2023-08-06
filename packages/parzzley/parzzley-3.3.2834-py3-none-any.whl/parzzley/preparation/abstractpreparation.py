# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Implement custom preparations by subclassing :py:class:`Preparation`.
"""

import typing as t

if t.TYPE_CHECKING:
    import parzzley.runtime.runtime


class Preparation:
    """
    Abstract base class for all logic that does preparation work for the actual synchronization run
    in advance or afterwards (like mounting filesystems, cleaning up stuff).
    """

    def __str__(self):
        return f"[{type(self).__name__}]"

    def enable(self, runtime: 'parzzley.runtime.runtime.RuntimeData') -> None:
        """
        Runs the preparation work.
        """
        pass

    def disable(self, runtime: 'parzzley.runtime.runtime.RuntimeData') -> None:
        """
        Undo the preparation after the synchronization (like unmounting).
        """
        pass

    def getstate(self, runtime: 'parzzley.runtime.runtime.RuntimeData') -> bool:
        """
        Checks if the preparation is successfully done or not.
        The Parzzley engine will check the state with this method at certain times and decide what to do
        depending on the state and the return values of ensuredisabledbefore, ensuredisabledafter and
        ensureenabled.
        """
        pass

    def ensuredisabledbefore(self) -> bool:
        """
        Defines if this preparation is required to be disabled before the synchronization begins.
        For example, it is an error situation if a certain mountpoint is already mounted before this preparation
        has mounted it.
        """
        return True

    def ensuredisabledafter(self) -> bool:
        """
        Defines if this preparation is required to be disabled after the synchronization ended.
        For example, it is an error situation if a certain mountpoint is mounted even after this preparation
        has unmounted it.
        """
        return True

    def ensureenabled(self) -> bool:
        """
        Defines if this preparation is required to be successful for the ongoing process of synchronization.
        For example, a preparation that just does some uncritical cleanup, should not stop the complete
        synchronization if it fails.
        """
        return True
