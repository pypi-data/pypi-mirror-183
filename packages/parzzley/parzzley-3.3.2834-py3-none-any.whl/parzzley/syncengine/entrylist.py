# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Internal in-memory list of entries for one filesystem with (de-)serialization features.
"""

import datetime
import pickle
import typing as t


class EntryList:

    def __init__(self):
        self.d = {}

    def foundfile(self, path: str, ftype: str, size: int, mtime: datetime.datetime, param: t.Optional[str],
                  last_synced_mtime: t.Optional[datetime.datetime] = None) -> None:
        self.d[path] = (path, ftype, size, mtime, param, [], last_synced_mtime)

    def updatefile(self, path: str, ftype: str, size: int, mtime: datetime.datetime, param: t.Optional[str]) -> None:
        self.foundfile(path, ftype, size, mtime, param)

    def removefile(self, path: str) -> None:
        self.d.pop(path, None)

    def notfoundfile(self, path: str) -> None:
        self.removefile(path)

    def save(self) -> bytes:
        return pickle.dumps(list(self.d.values()))

    def read(self, cnt: bytes) -> None:
        self.d = {}
        if cnt:
            _oldlst = pickle.loads(cnt)
            for v in _oldlst:
                self.d[v[0]] = v

    def exists(self, path: str) -> bool:
        return path in self.d

    def getftype(self, path: str) -> str:
        return self.d[path][1] if (path in self.d) else None

    def getsize(self, path: str) -> int:
        return self.d[path][2] if (path in self.d) else None

    def getmtime(self, path: str) -> datetime.datetime:
        return self.d[path][3] if (path in self.d) else None

    def getparam(self, path: str) -> t.Optional[str]:
        return self.d[path][4] if (path in self.d) else None

    def getlastsyncedmtime(self, path: str) -> t.Optional[datetime.datetime]:
        return self.d[path][6] if (path in self.d) else None

    def setlastsyncedmtime(self, path: str, mtime: datetime.datetime) -> None:
        self.d[path][6] = mtime

    def addtag(self, path: str, tag: str) -> None:
        if path in self.d:
            self.d[path][5].append(tag)

    def gettags(self, path: str) -> t.List[str]:
        if path in self.d:
            return list(self.d[path][5])


class CombinedEntryList:

    def __init__(self, first: EntryList, second: EntryList):
        self.first = first
        self.second = second

    def foundfile(self, path, ftype, size, mtime, param, last_synced_mtime=None):
        self.first.foundfile(path, ftype, size, mtime, param, last_synced_mtime=last_synced_mtime)

    def updatefile(self, path, ftype, size, mtime, param):
        self.first.updatefile(path, ftype, size, mtime, param)
        self.second.updatefile(path, ftype, size, mtime, param)

    def removefile(self, path):
        self.first.removefile(path)
        self.second.removefile(path)

    def notfoundfile(self, path):
        self.first.removefile(path)

    def exists(self, path):
        return self.first.exists(path)

    def getftype(self, path):
        return self.first.getftype(path)

    def getsize(self, path):
        return self.first.getsize(path)

    def getmtime(self, path):
        return self.first.getmtime(path)

    def getparam(self, path):
        return self.first.getparam(path)

    def getlastsyncedmtime(self, path):
        return self.first.getlastsyncedmtime(path)

    def setlastsyncedmtime(self, path, mtime):
        self.first.setlastsyncedmtime(path, mtime)
        self.second.setlastsyncedmtime(path, mtime)

    def addtag(self, path, tag):
        self.first.addtag(path, tag)
        self.second.addtag(path, tag)

    def gettags(self, path):
        return self.first.gettags(path)
