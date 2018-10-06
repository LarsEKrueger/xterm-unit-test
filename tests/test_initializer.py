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
            .attr(0,0, 'ucdv')
            .char(1,0, 'u')
            .attr(1,0, 'ibfa')
            .char(2,0, 'j')
            .attr(2,0, 'iulpt')
            .char(3,0, 'T')
            .attr(3,0, 'iubcds')
            .char(4,0, ')')
            .attr(4,0, 'iublfaw')
            .char(0,1, '2')
            .attr(0,1, 'ublcptv')
            .char(1,1, 'D')
            .attr(1,1, 'blcfds')
            .char(2,1, 'h')
            .attr(2,1, 'ilcfpaw')
            .char(3,1, 'P')
            .attr(3,1, 'ucfpdtv')
            .char(4,1, '!')
            .attr(4,1, 'ibfpdas')
            .char(0,2, '#')
            .attr(0,2, 'iulpdatw')
            .char(1,2, '\'')
            .attr(1,2, 'iubcdastv')
            .char(2,2, '/')
            .attr(2,2, 'ublfastw')
            .char(3,2, '>')
            .attr(3,2, 'iblcpstwv')
            .char(4,2, ']')
            .attr(4,2, 'ulcfdswv')
    ,
    test("test_initializer_80x25", 80, 25, 0, 0, "")
            .claim()
            .size(80,25)
            .expect()
            .cpos(0,0)
            .char(0,0, 'J')
            .attr(0,0, 'ucdv')
            .char(1,0, 'u')
            .attr(1,0, 'ibfa')
            .char(2,0, 'j')
            .attr(2,0, 'iulpt')
            .char(3,0, 'T')
            .attr(3,0, 'iubcds')
            .char(4,0, ')')
            .attr(4,0, 'iublfaw')
            .char(5,0, '2')
            .attr(5,0, 'ublcptv')
            .char(6,0, 'D')
            .attr(6,0, 'blcfds')
            .char(7,0, 'h')
            .attr(7,0, 'ilcfpaw')
            .char(8,0, 'P')
            .attr(8,0, 'ucfpdtv')
            .char(9,0, '!')
            .attr(9,0, 'ibfpdas')
            .char(10,0, '#')
            .attr(10,0, 'iulpdatw')
            .char(11,0, '\'')
            .attr(11,0, 'iubcdastv')
            .char(12,0, '/')
            .attr(12,0, 'ublfastw')
            .char(13,0, '>')
            .attr(13,0, 'iblcpstwv')
            .char(14,0, ']')
            .attr(14,0, 'ulcfdswv')
            .char(79,0, 'L')
            .attr(79,0, 'blfps')
            .char(0,1, 'y')
            .attr(0,1, 'lcpdw')
            .char(79,24, 'L')
            .attr(79,24, 'lfpaswv')
    ]

