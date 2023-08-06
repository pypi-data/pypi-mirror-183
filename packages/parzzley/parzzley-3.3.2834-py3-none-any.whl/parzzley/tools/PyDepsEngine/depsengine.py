#!/usr/bin/python3

# Copyright (C) 2018-2021, Josef Hahn
#
# This file is part of PyDepsEngine.
#
# PyDepsEngine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyDepsEngine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyDepsEngine.  If not, see <http://www.gnu.org/licenses/>.

from typing import *


SymbolList = Union[str, List[str], Callable[[], str], Callable[[], List[str]], None]


class EngineError(Exception):
    """
    Exceptions for all kinds of errors happening inside PyDepsEngine. See subclasses.
    """

    def __call__(self, *args):
        return self.__class__(*(self.args + args))
    
    
class DependencyUnresolvedError(EngineError):
    """
    Exception for unresolvable dependencies in dependency resolution.
    """

    def __init__(self, o: Any, req: List[Any]):
        self.o = o
        self.req = req
        super().__init__(f"Could not resolve dependencies '{list(req)}' of object '{o}'.")
    
    
class CircularDependenciesError(EngineError):
    """
    Exception for circular dependencies in dependency resolution.
    """

    def __init__(self, remainings: List['Processor.Object']):
        self.remainings = remainings
        slrem = "->".join([str(x.o) for x in remainings])
        super().__init__(f"Could not resolve dependencies due to a circle in {slrem}.")


# noinspection PyProtectedMember
class Processor:
    """
    A dependency processor manages a list of entity objects, based on top of an :py:class:`Engine`, but sorted according
    to their dependencies.
    
    Each processor potentially has its own view on dependencies for the entity objects 
    so two processors on top of the same engine can hold the entity objects in two different orders. Processors can also
    apply a filter and thereby returns just a subset of all entity objects.
    
    Either use processors directly (construct one with :py:meth:`Engine.add_processor`, then
    use :py:meth:`Processor.get_objects`) or use higher level constructs like compound objects
    (with :py:meth:`Engine.create_compound_object`).
    """

    class GraphNode:
        """
        A node in the (mostly internal) dependency graph.
        """

        def __init__(self, o: Optional['Processor.Object']):
            """
            :param o: The processor object to represent.
            """
            self.object = o
            self.after = list()

        def _add_dep(self, n2: str) -> None:
            """
            Adds a dependency.
            """
            if n2 not in self.after:
                self.after.append(n2)

        def _remove_dep(self, n2: str) -> None:
            """
            Removes a dependency.
            """
            self.after.remove(n2)

        def find_route_to(self, nto: 'Processor.GraphNode', *, _seen=None) -> List['Processor.GraphNode']:
            """
            Returns a route to another node.
            Raises a :py:class:`CircularDependenciesError` if a circle was found.

            .. note::
               This is just plain graph routing, not dependency resolution!

            :param nto: The destination graph node, or :samp:`None` if no route exists.
            :param _seen: Internal.
            """
            _seen = _seen or set()
            res = None
            for naft in nto.after:
                if naft == self:
                    res = [self, nto]
                else:
                    sroute = self.find_route_to(naft, _seen=_seen)
                    if sroute:
                        res = sroute + [nto]
                if res:
                    if self == nto:
                        raise CircularDependenciesError([n.object for n in res])
                    return res

        def dump_plain(self, *, _ind=0, _seen=None) -> str:
            """
            Returns a graph representation as plaintext.
            """
            _seen = _seen or set()
            r = " " * _ind + (str(self.object.o) if self.object else "+") + "\n"
            if self not in _seen:
                _seen.add(self)
                for aoo in self.after:
                    r += aoo.dump_plain(_ind=_ind + 4, _seen=_seen)
            return r

        def dump_pygraphviz(self, path: str, *, labelfct: Optional[Callable[['Processor.Object'], str]] = None,
                            colorfct: Optional[Callable[['Processor.GraphNode'], str]] = None,
                            txtcolorfct: Optional[Callable[['Processor.GraphNode'], str]] = None,
                            bkgcolor: str = "#ffffff") -> None:
            """
            Creates a graph representation as png image via pygraphviz (must be installed).

            :param path: The image destination path.
            :param labelfct: Function for creating a label from a processor object.
            :param colorfct: Function for creating a node color tuple from a graph node.
            :param txtcolorfct: Function for creating a node text color tuple from a graph node.
            :param bkgcolor: The image background color.
            """
            import pygraphviz
            import hashlib
            import html
            import random
            if not labelfct:
                def _defaultlabelfct(o):
                    s = str(o.o)
                    if len(s) > 120:
                        s = s[:58] + " ⋯ " + s[-59:]
                    ls = []
                    while s:
                        ss, s = s[:40], s[40:]
                        ls.append(ss)
                    return html.escape("↩\n".join(ls))
                labelfct = _defaultlabelfct
            if not colorfct:
                def _defaultcolorfct(n):
                    lbl = labelfct(n.object)
                    rnd = random.Random(int.from_bytes(hashlib.md5(lbl.encode()).digest()[-5:], "big"))
                    return rnd.randint(150, 255), rnd.randint(150, 255), rnd.randint(150, 255)
                colorfct = _defaultcolorfct
            if not txtcolorfct:
                def txtcolorfct(_):
                    return None
            g = pygraphviz.AGraph(directed=True, bgcolor=bkgcolor)
            def ggn(nn):
                snn = str(id(nn))
                if nn.object:
                    lbl = labelfct(nn.object)
                    cr, cg, cb = colorfct(nn)
                    # noinspection PyNoneFunctionAssignment
                    tt = txtcolorfct(nn)
                    tr, tg, tb = tt if tt else (0, 0, 0)
                    tr, tg, tb = min(255, max(0, int(tr))), min(255, max(0, int(tg))), min(255, max(0, int(tb)))
                    tcol = f"#{tr:02x}{tg:02x}{tb:02x}"
                else:
                    lbl = "root"
                    cr = cg = cb = 0
                    tcol = "#ffffff"
                cr, cg, cb = min(255, max(0, int(cr))), min(255, max(0, int(cg))), min(255, max(0, int(cb)))
                g.add_node(snn, label=lbl, fillcolor=f"#{cr:02x}{cg:02x}{cb:02x}", style="filled", fontcolor=tcol)
                return snn, cr, cg, cb
            seen = set()
            def dive(nn):
                if nn in seen:
                    return
                seen.add(nn)
                for a in nn.after:
                    dive(a)
                    usnn, ucr, ucg, ucb = ggn(nn)
                    vsnn, vcr, vcg, vcb = ggn(a)
                    er = int(vcr / 1.5)
                    eg = int(vcg / 1.5)
                    eb = int(vcb / 1.5)
                    g.add_edge(vsnn, usnn, color=f"#{er:02x}{eg:02x}{eb:02x}", penwidth=4)
            dive(self)
            g.layout("dot")
            g.draw(path)

    class Object:
        """
        A processor object holds an entity object together with dependency details.
        Instantiated by the :py:class:`Processor` infrastructure.
        """

        def __str__(self):
            return f"<depsengine.Processor.Object {self.o}>"

        def __init__(self, o, processor: 'Processor', own: SymbolList,
                     afterrequired: SymbolList, beforerequired: SymbolList,
                     afteroptional: SymbolList, beforeoptional: SymbolList, cacheable: bool):
            """
            See :py:meth:`Engine.add_object` for details about the parameters.

            :param cacheable: If the dependencies are cacheable (just a hint; internal code may restrict cacheability
                              further).
            """
            self.o = o
            self.processor = processor
            self.own = None
            self.afterrequired = None
            self.beforerequired = None
            self.afteroptional = None
            self.beforeoptional = None
            self.after = None
            self.before = None
            self.required = None
            self.cacheable = cacheable and not (callable(own) or callable(afterrequired) or
                                                callable(beforerequired) or callable(afteroptional) or
                                                callable(beforeoptional))
            self.update(own, afterrequired, beforerequired, afteroptional, beforeoptional)
        
        def update(self, own: SymbolList, afterrequired: SymbolList, beforerequired: SymbolList,
                   afteroptional: SymbolList, beforeoptional: SymbolList) -> None:
            """
            Updates the dependency details for this processor object.
            See Engine.add_object for details about the parameters.
            """
            self.own = Processor.Object._getlist(own)
            self.afterrequired = Processor.Object._getlist(afterrequired)
            self.beforerequired = Processor.Object._getlist(beforerequired)
            self.afteroptional = Processor.Object._getlist(afteroptional)
            self.beforeoptional = Processor.Object._getlist(beforeoptional)
            engine = self.processor.engine
            if engine.stagesymbol_PRE in self.own:
                self.beforeoptional.append(engine.stagesymbol_DEFAULT)
                self.own = [x for x in self.own if x not in [engine.stagesymbol_DEFAULT, engine.stagesymbol_POST]]
            elif engine.stagesymbol_POST in self.own:
                self.afteroptional.append(engine.stagesymbol_DEFAULT)
                self.own = [x for x in self.own if x not in [engine.stagesymbol_DEFAULT, engine.stagesymbol_PRE]]
            else:
                self.own.append(engine.stagesymbol_DEFAULT)
                self.own = [x for x in self.own if x not in [engine.stagesymbol_POST, engine.stagesymbol_PRE]]
            self.after = self.afterrequired + self.afteroptional
            self.before = self.beforerequired + self.beforeoptional
            self.required = self.beforerequired + self.afterrequired
        
        @staticmethod
        def _getlist(ll: SymbolList) -> List[str]:
            """
            Sanitizes :samp:`ll` to an actual list.
            If input is a string, it gets split. If input is a function, it gets called.

            :param ll: The list (or some other stuff - see above) to sanitize.
            """
            if ll is None:
                return []
            elif callable(ll):
                return Processor.Object._getlist(ll())
            elif isinstance(ll, str):
                ll = ll.replace(";", ",").replace(" ", ",").replace("\n", ",").split(",")
            return [y for y in [str(x).strip() for x in ll] if y]
    
    def __init__(self, filter_by_owns: Optional[List[str]] = None,
                 presort_keyfct: Optional[Callable[[Any], Any]] = None):
        """
        :param filter_by_owns: The list of :samp:`own` symbols to let the filter pass.
        :param presort_keyfct: Optionally pre-sorts the list so it always has the same order regardless of the object
                               insertion order.
        """
        self._all_objects_raw = []
        self._objects = []
        self._filter_by_owns = filter_by_owns
        self._presort_keyfct = presort_keyfct
        self._graphed_sorted_filtered = True
        self._graph_root = Processor.GraphNode(None)
        self.engine = None

    def initialize(self, engine: 'Engine') -> None:
        self.engine = engine

    def set_filter_by_owns(self, owns: Optional[List[str]] = None) -> None:
        """
        Filters this processor so it returns only entity objects that list at least one of :samp:`owns` in its
        :samp:`own`.

        :param owns: The list of :samp:`own` symbols to let the filter pass.
        """
        self._filter_by_owns = owns
        self._graphed_sorted_filtered = False

    def _ensure_filtering_sorting_valid(self) -> None:
        """
        Ensures the dependency graph to be up to date and the objects to be sorted correctly according to their
        current dependencies.
        """
        if not self._graphed_sorted_filtered:
            cacheable = True
            remainings = list(self._all_objects_raw)
            if self._presort_keyfct:
                remainings.sort(key=self._presort_keyfct)
            for oa in self._all_objects_raw:
                self._update_object_deps(oa)
                cacheable = cacheable and oa.cacheable
            remainings = self._filter_objects(remainings)
            nnodes = {ro: Processor.GraphNode(ro) for ro in remainings}
            nanodes = list(nnodes.values())
            subrootnodes = list(nanodes)
            for oa in remainings:
                onod = nnodes[oa]
                for onaa in oa.after:
                    found = False
                    for onoda in [n for n in nnodes.values() if onaa in n.object.own]:
                        onod._add_dep(onoda)
                        found = True
                    if not found and (onaa in oa.required):
                        raise DependencyUnresolvedError(oa.o, [onaa])
                for onab in oa.before:
                    found = False
                    for onodb in [n for n in nnodes.values() if onab in n.object.own]:
                        onodb._add_dep(onod)
                        found = True
                    if not found and (onab in oa.required):
                        raise DependencyUnresolvedError(oa.o, [onab])
            for ry in nanodes:
                for rx in list(ry.after):
                    if rx in subrootnodes:
                        subrootnodes.remove(rx)
                    largerexists = False
                    pol = list(ry.after)
                    seen = set()
                    while pol and not largerexists:
                        fpol = pol.pop()
                        if fpol == ry:
                            ry.find_route_to(ry)  # will raise a DependencyUnresolvedError
                        seen.add(fpol)
                        for z in fpol.after:
                            if z not in seen:
                                pol.append(z)
                            if z == rx:
                                largerexists = True
                                break
                    if largerexists:
                        ry._remove_dep(rx)
            rnode = Processor.GraphNode(None)
            for subrootnode in subrootnodes:
                rnode._add_dep(subrootnode)
            self._graph_root = rnode
            newlist = []
            seen = set()
            def dive(na):
                for cna in na.after:
                    if cna not in seen:
                        seen.add(cna)
                        dive(cna)
                        newlist.append(cna.object)
            dive(rnode)
            self._objects = newlist
            if cacheable:
                self._graphed_sorted_filtered = True

    def _filter_objects(self, l: List['Processor.Object']) -> List['Processor.Object']:
        """
        Filters the list of all objects and returns the subset that is to be actually processed.

        :param l: A list of processor objects.
        """
        result = l
        if self._filter_by_owns is not None:
            result = [x for x in result if len([y for y in x.own if y in self._filter_by_owns]) > 0]
        return self._complete_list_by_requirements(result)

    def _complete_list_by_requirements(self, l: List['Processor.Object']) -> List['Processor.Object']:
        """
        Returns a new list of processor objects, containing all from the input list, but extended by their required 
        dependencies. 
        This is to be used internally. It is not sorted and not checked to be valid!

        :param l: A list of processor objects to complete.
        """
        r = list(l)
        n = list([x for x in self._all_objects_raw if (x not in r)])
        madeprogress = True
        while madeprogress:
            madeprogress = False
            reqs = set()
            for oro in r:
                for oror in oro.afterrequired:
                    reqs.add(oror)
                for oror in oro.beforerequired:
                    reqs.add(oror)
            for iono, ono in reversed(list(enumerate(n))):
                for onoo in ono.own:
                    if onoo in reqs:
                        r.append(n.pop(iono))
                        madeprogress = True
                        break  # continue with next ono
        return r

    def _update_object_deps(self, pobj: 'Processor.Object') -> None:
        """
        Computes dependencies for an object and calls :py:meth:`Processor.Object.update` in order to update dependency
        infos. Subclasses may override it with custom behavior.
        See :py:meth:`Engine.add_object` for more details about the parts of a dependency tuple.

        :param pobj: The processor object.
        """
        def aundo(a, n):
            r = list(a)
            if ("_pydepsengine_"+n) in dir(pobj.o):
                flo = getattr(pobj.o, "_pydepsengine_"+n)
                lo = Processor.Object._getlist(flo(pobj.o, self))
                for olo in lo:
                    if olo not in r:
                        r.append(olo)
            return r
        own = aundo(pobj.own, "own")
        afterrequired = aundo(pobj.afterrequired, "afterrequired")
        beforerequired = aundo(pobj.beforerequired, "beforerequired")
        afteroptional = aundo(pobj.afteroptional, "afteroptional")
        beforeoptional = aundo(pobj.beforeoptional, "beforeoptional")
        pobj.update(own, afterrequired, beforerequired, afteroptional, beforeoptional)
    
    def _add_object(self, o: Optional[Any], own: SymbolList = None,
                    afterrequired: SymbolList = None, beforerequired: SymbolList = None,
                    afteroptional: SymbolList = None, beforeoptional: SymbolList = None) -> None:
        """
        Adds an object to this processor.
        |infrastructure|
        """
        # noinspection PyUnresolvedReferences
        cacheable = (self._update_object_deps.__func__ ==
                     Processor._update_object_deps)  # other code applies further conditions
        self._all_objects_raw.append(Processor.Object(o, self, own, afterrequired, beforerequired, afteroptional,
                                                      beforeoptional, cacheable))
        self._graphed_sorted_filtered = False

    def _remove_object(self, o: Optional[Any]) -> None:
        """
        Removes an object from this processor.
        |infrastructure|
        """
        for ipo, po in reversed(list(enumerate(self._all_objects_raw))):
            if po.o == o:
                self._all_objects_raw.pop(ipo)
        self._graphed_sorted_filtered = False

    def get_objects(self) -> List[Optional[Any]]:
        """
        Returns the list of entity objects, correctly sorted according their dependencies.
        """
        return [x.o for x in self.get_processor_objects()]

    def get_processor_objects(self) -> List['Processor.Object']:
        """
        Returns the list of processor objects, correctly sorted according their dependencies.
        Each contains one entity object and its dependency details.
        Typically one should use :py:meth:`Processor.get_objects` instead, which returns just the plain entity objects
        as inserted.
        """
        self._ensure_filtering_sorting_valid()
        return list(self._objects)

    def get_depgraph(self) -> 'Processor.GraphNode':
        """
        Returns the (mostly internal) dependency graph (the root node that depends on all).
        """
        self._ensure_filtering_sorting_valid()
        return self._graph_root


# noinspection PyProtectedMember
class Engine:
    """
    A dependency engine manages a list of entity objects.
    
    Depending on how it's configured (or subclassed), it holds a list of entity objects populated
    by :py:meth:`Engine.add_object`.
    
    On top of that, methods like :py:meth:`Engine.get_objects`, :py:meth:`Engine.add_processor`
    and :py:meth:`Engine.create_compound_object` help getting a list sorted according to their dependencies.
    """

    # noinspection PyPep8Naming
    def __init__(self, defaultprocessorclass: Type[Processor] = Processor,
                 defaultprocessorcfg: Optional[Dict[str, Optional[Any]]] = None,
                 stagesymbol_PRE: str = "PRE", stagesymbol_DEFAULT: str = "DEFAULT", stagesymbol_POST: str = "POST"):
        """
        :param defaultprocessorclass: The processor class to be used per default.
        :param defaultprocessorcfg: The configuration applied per default to new processors (in their constructors).
        :param stagesymbol_PRE: The name of the special symbol for earlier-than-the-rest objects.
                                This is one of some special symbols for usage in the :samp:`own` info (see
                                :py:meth:`Engine.add_object`).
                                Each represent one stage of execution. You should only need them in exotic situations.
        :param stagesymbol_DEFAULT: The name of the special symbol for the default staged objects (see above).
        :param stagesymbol_POST: The name of the special symbol for later-than-the-rest objects (see above).
        """
        self._objects = []
        self._processors = []
        self._defaultprocessorclass = defaultprocessorclass
        self._defaultprocessorcfg = defaultprocessorcfg or {}
        self.stagesymbol_PRE = stagesymbol_PRE
        self.stagesymbol_DEFAULT = stagesymbol_DEFAULT
        self.stagesymbol_POST = stagesymbol_POST
        
    def add_object(self, o: Optional[Any], own: SymbolList = None,
                   afterrequired: SymbolList = None, beforerequired: SymbolList = None,
                   afteroptional: SymbolList = None, beforeoptional: SymbolList = None) -> None:
        """
        Adds an entity object to the engine.
        All parameters marked with "Dependency info" are part of the dependency details of this entity object.
        Each is a list of symbols; either as an actual list of strings, or a comma-separated string (some other 
        delimiters exist), or a function returning such objects.
        Note: Dependency processors are free to add and remove any parts in their internal view.

        :param o: The entity object.
        :param own: Dependency info. List of symbols this entity object provides. Other entity objects can depend on
                    those symbols somehow (see the other parameters). The list may contain a 'stage symbol' for some 
                    exotic placements (see :py:class:`Engine`).
        :param afterrequired: Dependency info. List of symbols this entity object depends on. Each object providing one
                              of those symbols must be ordered before :samp:`o`. For each symbol there must exist at
                              least one object providing it.
        :param beforerequired: Dependency info. List of symbols this entity object reversely depends on. Each object
                               providing one of those symbols must be ordered after :samp:`o`. For each symbol there
                               must exist at least one object providing it.
        :param afteroptional: Dependency info. List of symbols this entity object optionally depends on. Each object
                              providing one of those symbols must be ordered before :samp:`o`. However, it is not an
                              error if some of those symbol are not provided by any object.
        :param beforeoptional: Dependency info. List of symbols this entity object optionally reversely depends on. Each
                               object providing one of those symbols must be ordered after :samp:`o`. However, it is not
                               an error if some of those symbol are not provided by any object.
        """
        ot = (o, own, afterrequired, beforerequired, afteroptional, beforeoptional)
        self._objects.append(ot)
        for p in self._processors:
            p._add_object(*ot)

    def remove_object(self, o: Optional[Any]) -> None:
        """
        Removes an entity object from the engine (all occurrences).

        :param o: The entity object.
        """
        for iot, ot in reversed(list(enumerate(self._objects))):
            if ot[0] == o:
                self._objects.pop(iot)
        for p in self._processors:
            p._remove_object(o)

    def add_processor(self, processorclass: Optional[Type[Processor]] = None, **cfg) -> Processor:
        """
        Creates and adds a processor to the engine, which in turn can return a list of entity objects processed
        regarding their dependencies.

        :param processorclass: The processor subclass to use (otherwise a default is used).
        :param cfg: Additional configuration (passed to the constructor).
        """
        processorclass = processorclass or self._defaultprocessorclass
        p = processorclass(**cfg)
        p.initialize(self)
        self._processors.append(p)
        for ot in self._objects:
            p._add_object(*ot)
        return p
    
    def get_objects(self, processorclass: Optional[Type[Processor]] = None, **cfg) -> List[Optional[Any]]:
        """
        Returns the list of entity objects processed by the default dependencies processor.

        :param processorclass: The processor subclass to use (otherwise a default is used).
        :param cfg: Additional configuration (passed to the constructor).
        """
        gcfg = dict(self._defaultprocessorcfg)
        gcfg.update(cfg)
        p = self.add_processor(processorclass, **gcfg)
        return p.get_objects()
