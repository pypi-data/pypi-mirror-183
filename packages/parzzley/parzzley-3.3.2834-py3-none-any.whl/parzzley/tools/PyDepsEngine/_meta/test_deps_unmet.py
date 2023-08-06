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


class Test(unittest.TestCase):
    
    def test_a(self):
        e = depsengine.Engine()
        e.add_object("abba", own="a", afterrequired="o")
        e.add_object("otto", own="o", afterrequired="i")
        e.add_object("iggi", own="i", afterrequired="z")
        try:
            print(e.get_objects())
            self.assertFalse(True)
        except depsengine.DependencyUnresolvedError as e:
            self.assertEqual(e.o, "iggi")
            self.assertEqual(e.req, ["z"])

    def test_b(self):
        e = depsengine.Engine()
        e.add_object("abba", own="a", afterrequired="o")
        e.add_object("otto", own="o", afterrequired="i")
        e.add_object("iggi", own="i", afteroptional="z")
        r = e.get_objects()
        self.assertEqual(r, ["iggi", "otto", "abba"])
