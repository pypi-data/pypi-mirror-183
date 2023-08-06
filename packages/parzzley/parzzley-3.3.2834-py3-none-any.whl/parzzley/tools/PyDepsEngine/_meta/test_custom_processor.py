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


import os
import unittest
import sys

mydir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(mydir)
import depsengine


class MyObject:
    
    def __init__(self, s):
        self.s = s
        
    def up(self):
        return self.s.upper()
    
    def lo(self):
        return self.s.lower()


class MyProcessor(depsengine.Processor):
    
    def __init__(self, reverse):
        depsengine.Processor.__init__(self)
        self._reverse = reverse
        
    def _update_object_deps(self, pobj):
        own = pobj.o.s
        beforeoptional = ""
        if self._reverse:
            if own == "b":
                beforeoptional = "a"
            elif own == "c":
                beforeoptional = "b"
        else:
            if own == "a":
                beforeoptional = "b"
            elif own == "b":
                beforeoptional = "c"
        pobj.update(own, None, "", [], beforeoptional)


class Test(unittest.TestCase):
    
    def test_a(self):
        e = depsengine.Engine(defaultprocessorclass=MyProcessor)
        e.add_object(MyObject("b"))
        e.add_object(MyObject("a"))
        e.add_object(MyObject("c"))
        r1 = [x.up() for x in e.get_objects(reverse=False)]
        r2 = [x.lo() for x in e.get_objects(reverse=True)]
        self.assertEqual(r1, ["A", "B", "C"])
        self.assertEqual(r2, ["c", "b", "a"])

