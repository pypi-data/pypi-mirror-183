# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import parzzley.aspect.abstractaspect
import parzzley.config.configpiece
import parzzley.syncengine.common


class ApplyPathAcceptor(parzzley.aspect.abstractaspect.Aspect):
    """
    Filters out files/dirs that should be excluded from syncing.
    It works by providing a path acceptor function.
    """

    # noinspection PyShadowingBuiltins
    def __init__(self, function):
        """
        :param function: The acceptor function. it gets the path as parameter and must return `True` for accepting it.
                         Warning: This parameter is a string that will be evaluated as Python expression (so
                         usage from config files is easy)! The path argument is available as `path`. 
                         Example: `path[2]=='a'`. The filesystem is available as `fs`.
        """
        super().__init__()
        self.acceptor = parzzley.config.configpiece.getcallable(function, ["path", "fs"])

    @parzzley.aspect.hook("", "applypathacceptor", "collectinfo",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_BeforeElectMaster)
    @parzzley.aspect.execute_only_if_not_already_maximally_elected()
    def applypathacceptor_applypathacceptor(self, ctx, filesystem):
        """
        Skips this entry if it is rejected by the path acceptor.
        """
        if not self.acceptor(path=ctx.path, fs=filesystem):
            ctx.skip_master_filesystem_promotion()
