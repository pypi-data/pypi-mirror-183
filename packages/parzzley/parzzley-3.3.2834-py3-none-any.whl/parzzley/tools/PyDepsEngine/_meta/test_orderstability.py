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

    def _get_processed(self, ll):
        e = depsengine.Engine()
        for fz in ll:
            e.add_object(fz[0], own=fz[1:2], afterrequired=fz[2:3], beforerequired=fz[3:4])
        return e.get_objects()

    def _objs(self, ll):
        return [llx[0] for llx in ll]

    def test_a(self):
        fooz = [["Franz"], ["jagt"], ["im"], ["komplett"], ["verwahrlosten"], ["Taxi"], ["quer"], ["durch"], ["Bayern"]]
        barz = [["Büro"], ["ist"], ["wie"], ["Jazz"], ["nur"], ["ohne"], ["die"], ["Musik"]]
        foozproc = self._get_processed(fooz)
        barzproc = self._get_processed(barz)
        for i in range(0, 10):
            res = self._get_processed(fooz)
            self.assertEqual(res, foozproc)
        for i in range(0, 10):
            res = self._get_processed(fooz+barz)
            self.assertEqual(len(res), len(fooz)+len(barz))
            self.assertEqual(list(filter(lambda x: x in self._objs(fooz), res)), foozproc)
            self.assertEqual(list(filter(lambda x: x in self._objs(barz), res)), barzproc)

    def test_b(self):
        fooz = [["Franz"], ["jagt"], ["im", "a"], ["komplett", "b", "a", "c"], ["verwahrlosten", "c", "", "d"],
                ["Taxi", "d"], ["quer"], ["durch"], ["Bayern"]]
        barz = [["wie", "z"], ["Jazz"], ["nur"], ["ohne"], ["die"], ["Musik"], ["Büro", "x"], ["ist", "y", "x", "z"]]
        foozproc = self._get_processed(fooz)
        barzproc = self._get_processed(barz)
        for i in range(0, 10):
            res = self._get_processed(fooz)
            self.assertEqual(res, foozproc)
        for i in range(0, 10):
            res = self._get_processed(fooz+barz)
            self.assertEqual(len(res), len(fooz)+len(barz))
            self.assertEqual(list(filter(lambda x: x in self._objs(fooz), res)), foozproc)
            self.assertEqual(list(filter(lambda x: x in self._objs(barz), res)), barzproc)
