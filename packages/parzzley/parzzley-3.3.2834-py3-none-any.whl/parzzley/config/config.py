# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Parzzley configuration handling.
"""

import importlib
import sys
import threading
import typing as t
# noinspection PyPep8Naming
import xml.etree.ElementTree as ET

import parzzley.aspect.abstractaspect
import parzzley.exceptions
import parzzley.filesystem.abstractfilesystem
import parzzley.logger.formatter.abstractlogformat
import parzzley.logger.loggerout.abstractloggerout
import parzzley.preparation.abstractpreparation
import parzzley.syncengine.sync
import parzzley.tools.common

if t.TYPE_CHECKING:
    import parzzley.filesystem.abstractfilesystem


threadlocal = threading.local()
threadlocal.knowntypes = []


class ParzzleyConfiguration:
    """
    Representation of a Parzzley configuration. This class can parse a configuration from xml and can generate it.
    It also has some modification methods and internal methods for generating actual objects from the data.
    """

    def __init__(self, environment: t.Optional[t.Dict[str, str]] = None):
        self.__syncs = []
        self.__loggers = []
        self.__customaspects = []
        self.__includes = []
        self.__pythonimports = []
        self.__environment = environment or {}

    @property
    def syncs(self) -> t.List['ParzzleyConfiguration.Sync']:
        return self.__syncs

    @property
    def loggers(self) -> t.List['ParzzleyConfiguration.Logger']:
        return self.__loggers

    @property
    def customaspects(self) -> t.List['ParzzleyConfiguration.CustomAspect']:
        return self.__customaspects

    @property
    def includes(self) -> t.List['ParzzleyConfiguration.Include']:
        return self.__includes

    @property
    def pythonimports(self) -> t.List['ParzzleyConfiguration.PythonImport']:
        return self.__pythonimports

    @property
    def environment(self) -> t.Dict[str, str]:
        return self.__environment

    def parsestring(self, s: str) -> str:
        """"
        Interprets a string by replacing each `${FOO}` with the value of the os environmental variable `FOO`.
        """
        i = len(s) - 1
        state = 1
        ei = None
        while i >= 0:
            if state == 1:  # looking for an end
                if s[i:i+1] == "}":
                    ei = i
                    state = 2
            elif state == 2:  # looking for a begin or end
                if s[i:i+1] == "}":
                    ei = i
                elif s[i:i+2] == "${":
                    ins = s[i+2:ei]
                    ns = ""
                    if len(ins) > 0 and len([c for c in ins if
                                             (c.lower() not in "abcdefghijklmnopqrstuvwxyz01234567890_")]) == 0:
                        ns = self.environment.get(ins, None)
                        if ns is None:
                            raise parzzley.exceptions.ReadInvalidConfigurationError(f"environment variable"
                                                                                   f" not set: {ins}")
                    s = s[:i] + ns + s[ei+1:]
                    state = 1
            i -= 1
        return s

    def parseparams(self, d: t.Dict[str, str]) -> t.Dict[str, str]:
        """
        Interprets a complete dictionary by the same replacement as in ParzzleyConfiguration.parsestring.
        """
        return {k: self.parsestring(v) for k, v in d.items()}

    @staticmethod
    def fromxml(xmlstring: str, environment: t.Optional[t.Dict[str, str]] = None) -> 'ParzzleyConfiguration':
        """
        Generates a ParzzleyConfiguration from an xml string.
        """
        xdoc = ET.ElementTree(ET.fromstring(xmlstring))
        xroot = xdoc.getroot()
        cfg = ParzzleyConfiguration(environment)
        for xentry in xroot:
            if xentry.tag == "sync":
                cfg.syncs.append(ParzzleyConfiguration.Sync.fromxml(cfg, xentry))
            elif xentry.tag == "logger":
                cfg.loggers.append(ParzzleyConfiguration.Logger.fromxml(cfg, xentry))
            elif xentry.tag == "customaspect":
                cfg.customaspects.append(ParzzleyConfiguration.CustomAspect.fromxml(cfg, xentry))
            elif xentry.tag == "include":
                cfg.includes.append(ParzzleyConfiguration.Include.fromxml(cfg, xentry))
            elif xentry.tag == "pythonimport":
                cfg.pythonimports.append(ParzzleyConfiguration.PythonImport.fromxml(cfg, xentry))
            else:
                raise parzzley.exceptions.ReadInvalidConfigurationError(f"invalid tag: {xentry.tag}")
        return cfg

    def toxml(self) -> str:
        """
        Returns an xml representation for the current configuration.
        """
        xroot = ET.Element("parzzleyconfig")
        for sync in self.syncs:
            sync.toxml(xroot)
        for logger in self.loggers:
            logger.toxml(xroot)
        for customaspect in self.customaspects:
            customaspect.toxml(xroot)
        for include in self.includes:
            include.toxml(xroot)
        for pythonimport in self.pythonimports:
            pythonimport.toxml(xroot)
        # argh; just for prettifying...
        import xml.dom.minidom
        return xml.dom.minidom.parseString(ET.tostring(xroot)).toprettyxml(indent="    ")

    class Sync:
        """
        Represents configuration for one synchronization task.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', filesystems: t.List['ParzzleyConfiguration.Filesystem'],
                     aspects: t.List['ParzzleyConfiguration.Aspect'],
                     preparations: t.List['ParzzleyConfiguration.Preparation'], **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param filesystems: A list of ParzzleyConfiguration.Filesystem.
            :param aspects: A list of ParzzleyConfiguration.Aspect.
            :param preparations: A list of ParzzleyConfiguration.Preparation.
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.filesystems = filesystems
            self.aspects = aspects
            self.preparations = preparations
            self.params = params

        @property
        def name(self) -> t.Optional[str]:
            return self.params.get("name")

        @name.setter
        def name(self, v: t.Optional[str]):
            self.params["name"] = v

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("sync")
            for filesystem in self.filesystems:
                filesystem.toxml(xentry)
            for aspect in self.aspects:
                aspect.toxml(xentry)
            for preparation in self.preparations:
                preparation.toxml(xentry)
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Sync':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            filesystems = []
            aspects = []
            preparations = []
            for xcentry in xentry:
                if xcentry.tag == "fs":
                    filesystems.append(ParzzleyConfiguration.Filesystem.fromxml(cfg, xcentry))
                elif xcentry.tag == "aspect":
                    aspects.append(ParzzleyConfiguration.Aspect.fromxml(cfg, xcentry))
                elif xcentry.tag == "preparation":
                    preparations.append(ParzzleyConfiguration.Preparation.fromxml(cfg, xcentry))
                else:
                    raise parzzley.exceptions.ReadInvalidConfigurationError(f"invalid tag: {xcentry.tag}")
            return ParzzleyConfiguration.Sync(cfg, filesystems, aspects, preparations, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.syncengine.sync.Sync:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            filesystems = []
            aspects = []
            preparations = []
            for a in self.aspects:
                aspects.append(a.instantiate(knowntypes))
            for f in self.filesystems:
                filesystems.append(f.instantiate(knowntypes))
            for p in self.preparations:
                preparations.append(p.instantiate(knowntypes))
            return parzzley.syncengine.sync.Sync(*aspects, *filesystems, *preparations,
                                                **self.cfg.parseparams(self.params))

        def _aspectlist(self, fs: t.Optional[int] = None) -> t.List['ParzzleyConfiguration.Aspect']:
            """
            Returns either the aspect list for `fs`, or the global one if `fs=None`.
            """
            if fs is None:
                return self.aspects
            else:
                return self.filesystems[fs].aspects

        def hasaspect(self, otype: str, fs: t.Optional[int] = None, everywhere: bool = False) -> bool:
            """
            Checks if an aspect with otype name `otype` (i.e. the class name) exists.

            :param otype: The otype name.
            :param fs: Whose aspect list to consider, `None` for the global one.
            :param everywhere: If `True`, all aspect lists are considered; ignores `fs`.
            """
            if everywhere:
                for _fs in list(range(len(self.filesystems))) + [None]:
                    if self.hasaspect(otype, fs=_fs):
                        return True
                return False
            else:
                return len([x for x in self._aspectlist(fs) if x.otype == otype]) > 0

        def getaspects(self, otype: str, fs: t.Optional[int] = None,
                       everywhere: bool = False) -> t.List['ParzzleyConfiguration.Aspect']:
            """
            Returns all aspects with otype name `otype` (i.e. the class name).

            :param otype: The otype name.
            :param fs: Whose aspect list to consider, `None` for the global one.
            :param everywhere: If `True`, all aspect lists are considered; ignores `fs`.
            """
            result = []
            if everywhere:
                for _fs in list(range(len(self.filesystems))) + [None]:
                    for x in self.getaspects(otype, fs=_fs):
                        result.append(x)
            else:
                for x in self._aspectlist(fs):
                    if x.otype == otype:
                        result.append(x)
            return result

        def removeaspect(self, otype: str, fs: t.Optional[int] = None, everywhere: bool = False) -> None:
            """
            Removes all aspects with otype name `otype` (i.e. the class name).

            :param otype: The otype name.
            :param fs: Whose aspect list to consider, `None` for the global one.
            :param everywhere: If `True`, all aspect lists are considered; ignores `fs`.
            """
            if everywhere:
                for _fs in list(range(len(self.filesystems))) + [None]:
                    self.removeaspect(otype, fs=_fs)
            else:
                aspects = self._aspectlist(fs)
                for x in [x for x in aspects if x.otype == otype]:
                    aspects.remove(x)

        def addaspect(self, otype: str, fs: t.Optional[int] = None, **params) -> 'ParzzleyConfiguration.Aspect':
            """
            Adds a new aspect.

            :param otype: The otype name for the new aspect (i.e. the class name).
            :param fs: Adds to this filesystem's aspect list, `None` for global.
            :param params: Additional keyword args are stored as additional config values.
            """
            a = ParzzleyConfiguration.Aspect(self.cfg, otype, **params)
            self._aspectlist(fs).append(a)
            return a

    class Filesystem:
        """
        Represents configuration for one filesystem.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', otype: str, aspects: t.List['ParzzleyConfiguration.Aspect'],
                     **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param otype: The otype name for the new object (i.e. the class name).
            :param aspects: A list of ParzzleyConfiguration.Aspect.
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.otype = otype
            self.aspects = aspects
            self.params = params

        @property
        def name(self) -> t.Optional[str]:
            return self.params.get("name")

        @name.setter
        def name(self, v: t.Optional[str]):
            self.params["name"] = v

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("fs")
            for a in self.aspects:
                a.toxml(xentry)
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xentry.attrib["type"] = self.otype
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Filesystem':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            otype = params.pop("type")
            aspects = []
            for xcentry in xentry:
                if xcentry.tag == "aspect":
                    aspects.append(ParzzleyConfiguration.Aspect.fromxml(cfg, xcentry))
                else:
                    raise parzzley.exceptions.ReadInvalidConfigurationError(f"invalid tag: {xcentry.tag}")
            return ParzzleyConfiguration.Filesystem(cfg, otype, aspects, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> 'parzzley.filesystem.abstractfilesystem.Filesystem':
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            aspects = []
            for a in self.aspects:
                aspects.append(a.instantiate(knowntypes))
            return knowntypes[self.cfg.parsestring(self.otype)](
                *aspects, **self.cfg.parseparams(self.params))

    class Aspect:
        """
        Represents configuration for one aspect.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', otype: str, **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param otype: The otype name for the new object (i.e. the class name).
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.otype = otype
            self.params = params

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("aspect")
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xentry.attrib["type"] = self.otype
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Aspect':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            otype = params.pop("type")
            return ParzzleyConfiguration.Aspect(cfg, otype, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.aspect.abstractaspect.Aspect:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            return knowntypes[self.cfg.parsestring(self.otype)](**self.cfg.parseparams(self.params))

    class Preparation:
        """
        Represents configuration for one synchronization task preparation.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', otype, **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param otype: The otype name for the new object (i.e. the class name).
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.otype = otype
            self.params = params

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this configuration object.
            """
            xentry = ET.Element("preparation")
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xentry.attrib["type"] = self.otype
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Preparation':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            otype = params.pop("type")
            return ParzzleyConfiguration.Preparation(cfg, otype, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.preparation.abstractpreparation.Preparation:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            return knowntypes[self.cfg.parsestring(self.otype)](**self.cfg.parseparams(self.params))

    class Logger:
        """
        Represents configuration for one logger.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', minseverity: t.Optional[str], maxseverity: t.Optional[str],
                     loggerout: 'ParzzleyConfiguration.Loggerout', formatter: 'ParzzleyConfiguration.LogFormatter',
                     enabled: bool):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param minseverity: The minimum severity (as parzzley.logger.Severity symbol name).
            :param maxseverity: The maximum severity (as parzzley.logger.Severity symbol name).
            :param loggerout: A ParzzleyConfiguration.Loggerout.
            :param formatter: A ParzzleyConfiguration.LogFormatter.
            :param enabled: If to enable this logger.
            """
            self.cfg = cfg
            self.minseverity = minseverity
            self.maxseverity = maxseverity
            self.loggerout = loggerout
            self.formatter = formatter
            self.enabled = enabled

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("logger")
            self.formatter.toxml(xentry)
            self.loggerout.toxml(xentry)
            xentry.attrib["minseverity"] = self.minseverity
            if self.maxseverity:
                xentry.attrib["maxseverity"] = self.maxseverity
            if not self.enabled:
                xentry.attrib["enabled"] = "0"
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Logger':
            """
            Generates a new configuration object from an xml piece.
            """
            minseverity = xentry.attrib["minseverity"]
            maxseverity = xentry.attrib.get("maxseverity", None)
            enabled = xentry.attrib.get("enabled", "1") == "1"
            loggerout = formatter = None
            for xcentry in xentry:
                if xcentry.tag == "out":
                    loggerout = ParzzleyConfiguration.Loggerout.fromxml(cfg, xcentry)
                elif xcentry.tag == "formatter":
                    formatter = ParzzleyConfiguration.LogFormatter.fromxml(cfg, xcentry)
                else:
                    raise parzzley.exceptions.ReadInvalidConfigurationError(f"invalid tag: {xcentry.tag}")
            return ParzzleyConfiguration.Logger(cfg, minseverity, maxseverity, loggerout, formatter, enabled)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.logger.Logger:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            minseverity = getattr(parzzley.logger.Severity, self.cfg.parsestring(self.minseverity).upper())
            maxseverity = getattr(parzzley.logger.Severity, self.cfg.parsestring(self.maxseverity).upper()) \
                if self.maxseverity else None
            loggerout = self.loggerout.instantiate(knowntypes)
            formatter = self.formatter.instantiate(knowntypes)
            enabled = self.enabled
            return parzzley.logger.Logger(formatter=formatter, loggerout=loggerout,
                                         minseverity=minseverity, maxseverity=maxseverity, enabled=enabled)

    class Loggerout:
        """
        Represents configuration for one logger output.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', otype: str, **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param otype: The otype name for the new object (i.e. the class name).
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.otype = otype
            self.params = params

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("out")
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xentry.attrib["type"] = self.otype
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Loggerout':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            otype = params.pop("type")
            return ParzzleyConfiguration.Loggerout(cfg, otype, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.logger.loggerout.abstractloggerout.Loggerout:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            return knowntypes[self.cfg.parsestring(self.otype)](**self.cfg.parseparams(self.params))

    class LogFormatter:
        """
        Represents configuration for one log formatter.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', otype: str, **params):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param otype: The otype name for the new object (i.e. the class name).
            :param params: Additional keyword args are stored as additional config values.
            """
            self.cfg = cfg
            self.otype = otype
            self.params = params

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("formatter")
            for prm in self.params.keys():
                xentry.attrib[prm] = self.params[prm]
            xentry.attrib["type"] = self.otype
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.LogFormatter':
            """
            Generates a new configuration object from an xml piece.
            """
            params = dict(xentry.attrib)
            otype = params.pop("type")
            return ParzzleyConfiguration.LogFormatter(cfg, otype, **params)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]) -> parzzley.logger.formatter.abstractlogformat.Logformat:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            return knowntypes[self.cfg.parsestring(self.otype)](**self.cfg.parseparams(self.params))

    class CustomAspect:
        """
        Represents configuration for one custom aspect implementation.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', name: str, code: str):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param name: The new otype name (i.e. class name) for this aspect.
            :param code: The implementation source code.
            """
            self.cfg = cfg
            self.name = name
            self.code = code

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("customaspect")
            xentry.attrib["name"] = self.name
            xentry.text = "\n" + self.code.strip() + "\n"
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.CustomAspect':
            """
            Generates a new configuration object from an xml piece.
            """
            name = xentry.attrib["name"]
            code = xentry.text.strip()
            return ParzzleyConfiguration.CustomAspect(cfg, name, code)

        def instantiate(self, knowntypes: t.Dict[str, t.Type]):
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            g = dict(globals())
            for x in knowntypes:
                g[x] = knowntypes[x]
            exec(self.code, g, g)
            return g[self.name]

    class Include:
        """
        Represents configuration for one config file include.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', incpath: str):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param incpath: The path to the Parzzley configuration file for including.
            """
            self.cfg = cfg
            self.incpath = incpath

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("include")
            xentry.attrib["path"] = self.incpath
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.Include':
            """
            Generates a new configuration object from an xml piece.
            """
            path = xentry.attrib["path"]
            return ParzzleyConfiguration.Include(cfg, path)

        def get_absolute_path(self, basepath: str) -> str:
            """
            Returns the absolute path to the file to include.
            """
            def isrelativepath(s):
                if sys.platform != "win32":  # good os -> easy rules
                    return not s.startswith("/")
                else:  # no comment :)
                    return (not s.startswith("/")) and (not s.startswith("\\")) and (not (len(s) > 1 and s[1] == ":"))
            ipath = self.cfg.parsestring(self.incpath)
            if isrelativepath(ipath):
                ipath = parzzley.tools.common.abspath(f"{basepath}/{ipath}")
            return ipath

    class PythonImport:
        """
        Represents configuration for one python import.
        """

        def __init__(self, cfg: 'ParzzleyConfiguration', importfrom: str, to: str):
            """
            :param cfg: The ParzzleyConfiguration instance.
            :param importfrom: The full name of the class to import ('package.module.Class').
            :param to: The name this class shall have after importing (without dots).
            """
            self.cfg = cfg
            self.importfrom = importfrom
            self.to = to

        def toxml(self, xparent: ET.Element) -> None:
            """
            Generates an xml piece for this object.
            """
            xentry = ET.Element("pythonimport")
            xentry.attrib["importfrom"] = self.importfrom
            xentry.attrib["to"] = self.to
            xparent.append(xentry)

        @staticmethod
        def fromxml(cfg: 'ParzzleyConfiguration', xentry: ET.Element) -> 'ParzzleyConfiguration.PythonImport':
            """
            Generates a new configuration object from an xml piece.
            """
            importfrom = xentry.attrib["importfrom"]
            to = xentry.attrib["to"]
            return ParzzleyConfiguration.PythonImport(cfg, importfrom, to)

        def instantiate(self) -> t.Any:
            """
            Instantiates a new actual Parzzley object by this configuration object.
            """
            _importfrom = self.cfg.parsestring(self.importfrom)
            nnames = _importfrom.split(".")
            anames = []
            mmod = None
            while mmod is None:
                anames.append(nnames.pop(-1))
                if len(nnames) == 0:
                    break
                try:
                    mmod = importlib.import_module(".".join(nnames))
                except ImportError:
                    pass
            aobj = mmod
            if aobj is None:
                raise parzzley.exceptions.ReadInvalidConfigurationError(f"module not found for: {_importfrom}")
            while len(anames) > 0:
                aname = anames.pop(-1)
                aobj = getattr(aobj, aname, None)
                if aobj is None:
                    raise parzzley.exceptions.ReadInvalidConfigurationError(f"object not found: {_importfrom}")
            return aobj
