# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
# noinspection PyPep8Naming
import xml.etree.cElementTree as ET

import parzzley.aspect.abstractaspect
import parzzley.exceptions
import parzzley.logger
import parzzley.runtime.datastorage
import parzzley.syncengine.common


class SyncMetadataAspectError(parzzley.exceptions.ParzzleyError):
    pass


# noinspection PyProtectedMember
class _Metadata:

    def __str__(self):
        return f"[v:{self.version} data:{self._data}]"

    def __init__(self, version=0):
        self.version = version
        self._data = {}

    def putdata(self, k, v):
        self._data[k] = v

    def getdata(self, k, d=None):
        return self._data.get(k, d)

    def getkeys(self):
        return list(self._data.keys())

    @staticmethod
    def get_metadata_from_file(filesystem, path, ignore_removed=False):
        if filesystem.exists(path):
            xakeys = filesystem.listxattrkeys(path)
            version = -1
            if "user.parzzley__version" in xakeys:
                version = int(filesystem.getxattrvalue(path, "user.parzzley__version"))
            result = _Metadata(version)
            for xakey in xakeys:
                if xakey.startswith("user."):
                    key = xakey[5:]
                    if key != "parzzley__version":
                        value = filesystem.getxattrvalue(path, xakey)
                        result.putdata(key, value)
        else:
            if ignore_removed:
                result = _Metadata(-1)
            else:
                raise SyncMetadataAspectError(f"file {path} does not exist on {filesystem.name}")
        return result

    @staticmethod
    def set_metadata_to_file(filesystem, path, md, ignore_removed=False):
        if filesystem.exists(path):
            xakeys = filesystem.listxattrkeys(path)
            for key in md._data.keys():
                xakey = f"user.{key}"
                filesystem.setxattrvalue(path, xakey, md._data[key])
                if xakey in xakeys:
                    xakeys.remove(xakey)
            for xakey in xakeys:
                if xakey.startswith("user.") and xakey != "user.parzzley__version":
                    filesystem.unsetxattrvalue(path, xakey)
            _Metadata.set_metadataversion_to_file(filesystem, path, md, ignore_removed)
        else:
            if not ignore_removed:
                raise SyncMetadataAspectError(f"file {path} does not exist on {filesystem.name}")

    @staticmethod
    def set_metadataversion_to_file(filesystem, path, md, ignore_removed=False):
        if filesystem.exists(path):
            filesystem.setxattrvalue(path, "user.parzzley__version", str(md.version))
        else:
            if not ignore_removed:
                raise SyncMetadataAspectError(f"file {path} does not exist on {filesystem.name}")

    @staticmethod
    def get_metadata_from_shadow(filesystem, shadowfilesystem, path):
        isdir = filesystem.getftype(path) == parzzley.syncengine.common.EntryType.Directory
        xmlpath = path + ("/##parzzley.directory.metadata##" if isdir else "")
        if shadowfilesystem.getftype(xmlpath) == parzzley.syncengine.common.EntryType.File:
            root = ET.fromstring(shadowfilesystem.readfromfile(xmlpath))
            res = _Metadata(version=int(root.attrib["version"]))
            for xmlchild in root:
                res.putdata(xmlchild.attrib["key"], xmlchild.attrib["value"])
        else:
            res = _Metadata(version=-1)
        return res

    @staticmethod
    def set_metadata_to_shadow(filesystem, shadowfilesystem, path, md):
        isdir = filesystem.getftype(path) == parzzley.syncengine.common.EntryType.Directory
        root = ET.Element("parzzley_metadata")  # TODO patch in /data/storage
        root.set("version", str(md.version))
        for kkey in md.getkeys():
            ent = ET.SubElement(root, "item")
            ent.set("key", kkey)
            ent.set("value", md.getdata(kkey, ""))
        dstfile = f"/{path}{'/##parzzley.directory.metadata##' if isdir else ''}"
        destdir = os.path.dirname(dstfile)
        shadowfilesystem.createdirs(destdir)
        shadowfilesystem.writetofile(dstfile, ET.tostring(root, encoding="utf-8"))

    @staticmethod
    def remove_shadow(shadowfilesystem, path, isdir):
        dstfile = f"{path}{'/##parzzley.directory.metadata##' if isdir else ''}"
        if isdir:
            destdir = os.path.dirname(dstfile)
            if shadowfilesystem.exists(destdir):
                shadowfilesystem.removedir(destdir, recursive=True)
        else:
            if shadowfilesystem.exists(dstfile):
                shadowfilesystem.removefile(dstfile)

    @staticmethod
    def metadata_differs(md1, md2):
        return md1.version != md2.version or md1._data != md2._data


class _MetadataStruct:

    def __init__(self):
        self.latestmd = None
        self.latestmd_origversion = -1
        self.aborted = False
        self.forpath = None


# noinspection PyProtectedMember
class MetadataSynchronization(parzzley.aspect.abstractaspect.Aspect):
    """
    Synchronizes metadata without a shadow storage (typical for the workstations).
    """

    @parzzley.aspect.hook("metadata_findhighestshadow", "metadata", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_Prepare)
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.File,
                                                       parzzley.syncengine.common.EntryType.Directory)
    def metadata_checkagainstshadow(self, ctx, filesystem):
        """
        Checks if this entry has a metadata update against the shadow storage. If so, it updates the version numbers
        (in the in-memory data structure).
        """
        if not hasattr(ctx, "metadata_struct"):
            raise parzzley.syncengine.common.SyncConfigurationError("At least one metadata synchronization with "
                                                                   "shadow must exist.")
        td = ctx.metadata_struct
        if td.aborted:
            return
        minemd = _Metadata.get_metadata_from_file(filesystem, ctx.path, ignore_removed=True)
        if minemd.version >= td.latestmd.version:
            if _Metadata.metadata_differs(minemd, td.latestmd):
                if minemd.version == td.latestmd.version or td.latestmd_origversion == -1:
                    if minemd.version == td.latestmd_origversion:
                        minemd.version += 1
                        td.latestmd = minemd
                    elif td.latestmd_origversion == -1:
                        td.latestmd = minemd
                        td.latestmd_origversion = minemd.version
                    else:
                        td.aborted = True
                        ctx.logproblem(filesystem, ctx.path, verb="has metadata conflict")

    @parzzley.aspect.hook("", "metadata", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_AfterUpdate)
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.File,
                                                       parzzley.syncengine.common.EntryType.Directory)
    def metadata_propagatetofilesystem_file(self, ctx, filesystem):
        """
        Checks if metadata of the entry differ from the filesystem information and, if so, updates the
        entry metadata in the filesystem (with exactly what it is now stored in-memory).
        """
        td = getattr(ctx, "metadata_struct", None)
        if td is None or td.aborted or td.latestmd.version < 0:
            return
        if _Metadata.metadata_differs(td.latestmd, _Metadata.get_metadata_from_file(filesystem, ctx.path,
                                                                                    ignore_removed=True)):
            if ctx.getinfo_current_exists(filesystem, ctx.path):
                _Metadata.set_metadata_to_file(filesystem, ctx.path, td.latestmd)
                ctx.logupdate(filesystem, "metadata of " + ctx.path, comment="on "+filesystem.name)
                ctx.syncglobaldata.changed_flag = True
            else:
                ctx.logproblem(filesystem, ctx.path, verb="gone during metadata update",
                               severity=parzzley.logger.Severity.DEBUG)


# noinspection PyProtectedMember
class MetadataSynchronizationWithShadow(MetadataSynchronization):
    """
    Synchronizes metadata with a shadow storage (typical for the file server).
    """

    # noinspection PyUnusedLocal
    @parzzley.aspect.hook("", "metadata", "", event=parzzley.syncengine.common.SyncEvent.BeginSync)
    def metadata_init(self, ctx, filesystem):
        """
        Some initialization.
        """
        if not hasattr(ctx.syncglobaldata, "_content_metadata_storage"):
            ctx.syncglobaldata._content_metadata_storage = parzzley.runtime.datastorage.get_storage_department(
                ctx, "content_metadata", location=parzzley.runtime.datastorage.StorageLocation.SYNC_VOLUME,
                scope=parzzley.runtime.datastorage.StorageScope.SHARED)

    @parzzley.aspect.hook("", "metadata", "", event=parzzley.syncengine.common.SyncEvent.UpdateItem_Update_Prepare)
    def metadata_findhighestshadow(self, ctx, filesystem):
        """
        Updates `latestmd` as stored in ctx if this filesystem has a higher version in shadow.
        """
        ctx.metadata_struct = getattr(ctx, "metadata_struct", None)
        if ctx.metadata_struct is None:
            td = ctx.metadata_struct = _MetadataStruct()
            td.latestmd = _Metadata(-1)
        else:
            td = ctx.metadata_struct
        if td.aborted:
            return
        shadowfilesystem = ctx.syncglobaldata._content_metadata_storage.get_filesystem(filesystem=filesystem)
        minemd = _Metadata.get_metadata_from_shadow(filesystem, shadowfilesystem, ctx.path)
        if minemd.version > td.latestmd.version:
            td.latestmd = minemd
            td.latestmd_origversion = minemd.version
        elif minemd.version == td.latestmd.version and \
                _Metadata.metadata_differs(minemd, td.latestmd):
            ctx.logproblem(filesystem, ctx.path, verb="has metadata conflict with shadow")
            td.aborted = True

    @parzzley.aspect.hook("", "metadata", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateItem_AfterUpdate)
    @parzzley.aspect.execute_only_for_slave_fs_filetype(parzzley.syncengine.common.EntryType.File,
                                                       parzzley.syncengine.common.EntryType.Directory)
    def metadata_propagatetoshadow_file(self, ctx, filesystem):
        """
        Checks if metadata of the entry differ from the shadow storage information and, if so, updates the
        entry metadata in the shadow storage (with exactly what it is now stored in-memory).
        """
        td = getattr(ctx, "metadata_struct", None)
        if td is None or td.aborted or td.latestmd.version < 0:
            return
        shadowfilesystem = ctx.syncglobaldata._content_metadata_storage.get_filesystem(filesystem=filesystem)
        if _Metadata.metadata_differs(td.latestmd, _Metadata.get_metadata_from_shadow(filesystem, shadowfilesystem,
                                                                                      ctx.path)):
            _Metadata.set_metadata_to_shadow(filesystem, shadowfilesystem, ctx.path, td.latestmd)
            ctx.logupdate(filesystem, "shadow metadata of " + ctx.path, comment="on "+filesystem.name)
            ctx.syncglobaldata.changed_flag = True

    @parzzley.aspect.hook("*remove_orphaned_dirs", "", "",
                         event=parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate)
    def cleanup_shadow(self, ctx, filesystem):
        """
        Cleans up orphaned files in shadow metadata storage.
        """
        shadowfilesystem = ctx.syncglobaldata._content_metadata_storage.get_filesystem(filesystem=filesystem)
        if shadowfilesystem.getftype(ctx.path) == parzzley.syncengine.common.EntryType.Directory:
            for x in shadowfilesystem.listdir(ctx.path):
                if x == "##parzzley.directory.metadata##":
                    xx = ctx.path
                    isdir = True
                else:
                    xx = ctx.path + "/" + x
                    isdir = shadowfilesystem.getftype(xx) == parzzley.syncengine.common.EntryType.Directory
                if not filesystem.exists(xx):
                    _Metadata.remove_shadow(shadowfilesystem, xx, isdir)
                    td = getattr(ctx, "metadata_struct", None)
                    if td is not None:
                        td.aborted = True
