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

# Test the character matrix initializer. This test ensures that the implemented
# generator is identical to the reference implementation in BiTe.

from xut import test

tests = [
    test("test_initializer_5x3", 5, 3, 0, 0, "")
            .claim()
            .size(5,3)
            .expect()
            .cpos(0,0)
            .char(0,0, 'J')
            .char(1,0, 'u')
            .char(2,0, 'j')
            .char(3,0, 'T')
            .char(4,0, ')')
            .char(0,1, '2')
            .char(1,1, 'D')
            .char(2,1, 'h')
            .char(3,1, 'P')
            .char(4,1, '!')
            .char(0,2, '#')
            .char(1,2, '\'')
            .char(2,2, '/')
            .char(3,2, '>')
            .char(4,2, ']')
    ,
    test("test_initializer_80x25", 80, 25, 0, 0, "")
            .claim()
            .size(80,25)
            .expect()
            .cpos(0,0)
            .char(0,0, 'J')
            .char(1,0, 'u')
            .char(2,0, 'j')
            .char(3,0, 'T')
            .char(4,0, ')')
            .char(5,0, '2')
            .char(6,0, 'D')
            .char(7,0, 'h')
            .char(8,0, 'P')
            .char(9,0, '!')
            .char(10,0, '#')
            .char(11,0, '\'')
            .char(12,0, '/')
            .char(13,0, '>')
            .char(14,0, ']')
            .char(79,0, 'L')
            .char(0,1, 'y')
            .char(79,24, 'L')
    ]

