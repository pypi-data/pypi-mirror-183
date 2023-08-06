# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import grp
import os
import pwd
import stat

import parzzley.aspect.abstractaspect
import parzzley.syncengine.common


class ApplyPermissions(parzzley.aspect.abstractaspect.Aspect):
    """
    Applies the specified file system permissions to all entries processed by Parzzley.
    Warning: Do not use this feature in security relevant contexts. It's not guaranteed that all aspects follow this.
    """

    def __init__(self, user, group, fileaddperms="", filesubtractperms="", diraddperms="", dirsubtractperms=""):
        """
        :param user: Either "#uid" or user name of the new owner user.
        :param group: Either "#gid" or group name of the new owner group.
        :param fileaddperms: Numerical mask of permissions that will be added to each synchronized file.
        :param filesubtractperms: Numerical mask of permissions that will be subtracted from each synchronized file.
        :param diraddperms: Numerical mask of permissions that will be added to each synchronized directory.
        :param dirsubtractperms: Numerical mask of permissions that will be subtracted from each synchronized
                                 directory.
        """
        super().__init__()
        self.user = user
        self.group = group
        if user.startswith("#"):
            self.user = int(user[1:])
        else:
            self.user = pwd.getpwnam(user).pw_uid
        if group.startswith("#"):
            self.group = int(group[1:])
        else:
            self.group = grp.getgrnam(group).gr_gid
        fileaddperms = int(fileaddperms) if (fileaddperms != "") else None
        filesubtractperms = int(filesubtractperms) if (filesubtractperms != "") else None
        diraddperms = int(diraddperms) if (diraddperms != "") else None
        dirsubtractperms = int(dirsubtractperms) if (dirsubtractperms != "") else None
        self.fileaddperms = fileaddperms or (stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)
        self.diraddperms = diraddperms or (stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP)
        self.filesubtractperms = filesubtractperms or (stat.S_IRWXO | stat.S_IWGRP)
        self.dirsubtractperms = dirsubtractperms or (stat.S_IRWXO | stat.S_IWGRP)

    @staticmethod
    def _setperms(path, uid, gid, addperms, subtractperms):
        perms = os.stat(path).st_mode
        perms = (perms & ~subtractperms) | addperms
        os.chmod(path, perms)
        os.chown(path, uid, gid)

    @parzzley.aspect.hook("*defaultupdate", "", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster)
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.File)
    def applypermissions_setfileperms(self, ctx, filesystem):
        """
        Sets the file permissions of a file entry to what is configured in the aspect.
        """
        if not ctx.is_update_set_skipped():
            ApplyPermissions._setperms(filesystem.getfulllocalpath(ctx.path), self.user, self.group,
                                       self.fileaddperms, self.filesubtractperms)

    @parzzley.aspect.hook("", "", "", event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def applypermissions_setdirperms(self, ctx, filesystem):
        """
        Sets the file permissions of a dir entry to what is configured in the aspect.
        """
        if ctx.getinfo_current_ftype(filesystem, ctx.path) == parzzley.syncengine.common.EntryType.Directory:
            ApplyPermissions._setperms(filesystem.getfulllocalpath(ctx.path), self.user, self.group,
                                       self.diraddperms, self.dirsubtractperms)
