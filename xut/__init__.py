#
#  xterm-unit-test
#  Copyright (C) 2018  Lars Krüger
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Test generator framework

import sys
import os
import runpy

class CheckCPos:
    def __init__(self,error,x,y):
        self.error = error
        self.x = x
        self.y = y

class CheckSize:
    def __init__(self,error,w,h):
        self.error = error
        self.w= w
        self.h=h

class TestBuilder:
    def __init__(self, name, w, h, x, y, seq):
        self.name = name
        self.w = w
        self.h = h
        self.curs_x = x
        self.curs_y = y
        self.seq = seq

        self.error = True
        self.checks = []

    def claim(self):
        self.error = True
        return self

    def expect(self):
        self.error = False
        return self

    def size(self,w,h):
        self.checks.append(CheckSize(self.error,w,h))
        return self

    def cpos(self,x,y):
        self.checks.append(CheckCPos(self.error,x,y))
        return self

    def generate(self, generator):
        generator.begin_test(self.name)
        generator.create_screen(self.w,self.h)
        generator.place_cursor(self.curs_x,self.curs_y)
        generator.export_sequence(self.seq)
        generator.begin_checks()
        for c in self.checks:
            generator.add_check(c)
        generator.end_checks()
        generator.end_test(self.name)

def test(name,w,h,x,y,seq):
    return TestBuilder(name,w,h,x,y,seq)

def generate( generator, tests_path):
    # Find all python files in <tests_path> and run them.
    for root, dirs, files in os.walk(tests_path):
        for name in files:
            path=os.path.join(root,name)
            (_,ext) = os.path.splitext(path)
            if ext == ".py":
                mod = runpy.run_path(path)
                generator.begin_file(path)
                for test in mod['tests']:
                    test.generate( generator)
                generator.end_file(path)
