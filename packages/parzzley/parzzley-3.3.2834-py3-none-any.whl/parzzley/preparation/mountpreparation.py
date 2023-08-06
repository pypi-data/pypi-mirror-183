# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os

import parzzley.config.configpiece
import parzzley.exceptions
import parzzley.preparation.abstractpreparation
import parzzley.tools.common


class MountPreparationError(parzzley.exceptions.ParzzleyError):
    pass


class MountpointNotEmptyError(MountPreparationError):

    def __init__(self, mountpoint: str):
        super().__init__(f"The mountpoint {mountpoint} is not empty before mounting.")


class UnableToMountError(MountPreparationError):

    def __init__(self, mountpoint: str, msg: str):
        super().__init__(f"Unable to mount {mountpoint}: {msg}.")


class UnableToUnmountError(MountPreparationError):

    def __init__(self, mountpoint: str, msg: str):
        super().__init__(f"Unable to unmount {mountpoint}: {msg}.")


class UnableToGetMountListError(MountPreparationError):

    def __init__(self, msg: str):
        super().__init__(f"Unable to get list of mountpoints: {msg}")


class MountPreparation(parzzley.preparation.abstractpreparation.Preparation):
    """
    Mounts filesystems to a mountpoint.
    """

    def __init__(self, *, src: str, tgt: str, **kwargs):
        self.options = parzzley.config.configpiece.getlist(kwargs, "options")
        super().__init__()
        self.src = src
        self.tgt = os.path.abspath(tgt)

    def __str__(self):
        return f"[{type(self).__name__},{self.src}]"

    @staticmethod
    def _checkmountpointempty(tgt):
        if len(os.listdir(tgt)) > 0:
            raise MountpointNotEmptyError(tgt)

    def enable(self, runtime):
        if not os.path.exists(self.tgt):
            os.makedirs(self.tgt)
        MountPreparation._checkmountpointempty(self.tgt)
        (ret, r) = parzzley.tools.common.call("sudo", "-A", "mount", self.src, self.tgt, *self.options)
        if ret != 0:
            raise UnableToMountError(self.src, r)

    def disable(self, runtime):
        parzzley.tools.common.call("sync")
        parzzley.tools.common.call("sync")
        (ret, r) = parzzley.tools.common.call("sudo", "-A", "umount", self.tgt)
        if ret != 0:
            raise UnableToUnmountError(self.src, r)

    def getstate(self, runtime):
        (ret, r) = parzzley.tools.common.call(["mount"])
        if ret != 0:
            raise UnableToGetMountListError(r)
        return r.find(f" {self.tgt} ") > -1
