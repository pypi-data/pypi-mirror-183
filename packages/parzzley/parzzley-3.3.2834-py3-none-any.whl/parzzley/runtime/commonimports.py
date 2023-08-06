# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Imports everything that is typically used by the end user in a Parzzley config file.
"""

from datetime import timedelta
from parzzley.tools.pathacceptors import defaultpathacceptor
from parzzley.syncengine.sync import Sync
from parzzley.filesystem.local import LocalFilesystem
from parzzley.filesystem.sshfs import SshfsFilesystem
from parzzley.preparation.mountpreparation import MountPreparation
from parzzley.preparation.sshfsmountpreparation import SshfsMountPreparation
from parzzley.logger import Logger
from parzzley.logger.loggerout.externalprogramloggerout import ExternalProgramLoggerout
from parzzley.logger.loggerout.filestreamloggerout import FilestreamLoggerout
from parzzley.logger.formatter.plaintextlogformat import PlaintextLogformat
from parzzley.logger.formatter.htmllogformat import HtmlLogformat
from parzzley.aspect.remove import TrashRemove, DefaultRemove
from parzzley.aspect.logging import Logging
from parzzley.aspect.defaults import DefaultSync, PullAndPurgeSyncSink, PullAndPurgeSyncSource
from parzzley.aspect.revisiontracking import RevisionTracking
from parzzley.aspect.applypathacceptor import ApplyPathAcceptor
from parzzley.aspect.highlevelcustomization import HighLevelCustomization
from parzzley.aspect.monitorfilechanges import MonitorFileChanges
from parzzley.tools.pathacceptors import builtinpathacceptor
from parzzley.aspect.metadata import MetadataSynchronization, MetadataSynchronizationWithShadow

try:
    import stat
    from parzzley.aspect.permissions import ApplyPermissions
except ImportError:
    pass
