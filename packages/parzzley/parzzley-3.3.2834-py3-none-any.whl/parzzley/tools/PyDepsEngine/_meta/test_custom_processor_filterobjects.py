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


class MyProcessor(depsengine.Processor):
    
    def __init__(self):
        depsengine.Processor.__init__(self)

    def _filter_objects(self, pobj):
        return [x for x in pobj if x.o[0]==x.o[-1]]


class Test(unittest.TestCase):
    
    def test_a(self):
        e = depsengine.Engine(defaultprocessorclass=MyProcessor)
        e.add_object("abba", own="a", afterrequired="o")
        e.add_object("hanz", own="h", afteroptional="o")
        e.add_object("otto", own="o", afterrequired="i")
        e.add_object("heintz", own="h", afteroptional="a")
        e.add_object("iggi", own="i")
        r = e.get_objects()
        self.assertEqual(r, ["iggi", "otto", "abba"])
