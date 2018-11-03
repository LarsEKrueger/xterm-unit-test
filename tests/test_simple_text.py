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

# Test simple text placements.

from xut import test

tests = [
    test("test_cr", 5, 3, 0, 0, "he\\rwo")
    .claim()
    .size(5,3)
    .expect()
    .cpos(2,0)
    .char(0,0, 'w')
    .char(1,0, 'o')
    ,
    test("test_nl", 5, 3, 0, 0, "he\\nwo")
    .expect()
    .cpos(2,1)
    .char(0,0, 'h')
    .char(1,0, 'e')
    .char(0,1, 'w')
    .char(1,1, 'o')
    ]

