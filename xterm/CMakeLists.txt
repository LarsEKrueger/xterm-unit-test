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
# Xterm test rig CMake file

include(FindX11)
include(FindCurses)

# Build the test executable
add_executable(test_xterm
  test_xterm_main.c
  ${XTERM_SOURCE_DIR}/data.c
  ${XTERM_SOURCE_DIR}/util.c
  ${XTERM_SOURCE_DIR}/screen.c
  ${XTERM_SOURCE_DIR}/linedata.c
  ${XTERM_SOURCE_DIR}/scrollbar.c
  ${XTERM_SOURCE_DIR}/button.c
  ${XTERM_SOURCE_DIR}/cursor.c
  ${XTERM_SOURCE_DIR}/misc.c
  ${XTERM_SOURCE_DIR}/charproc.c
  ${XTERM_SOURCE_DIR}/VTPrsTbl.c
  ${XTERM_SOURCE_DIR}/TekPrsTbl.c
  ${XTERM_SOURCE_DIR}/cachedGCs.c
  ${XTERM_SOURCE_DIR}/Tekproc.c
  ${XTERM_SOURCE_DIR}/xstrings.c
  ${XTERM_SOURCE_DIR}/menu.c
  ${XTERM_SOURCE_DIR}/input.c
  ${XTERM_SOURCE_DIR}/charsets.c
  ${XTERM_SOURCE_DIR}/print.c
  ${XTERM_SOURCE_DIR}/fontutils.c
  ${XTERM_SOURCE_DIR}/xtermcap.c
  ${XTERM_SOURCE_DIR}/tabs.c
  ${XTERM_SOURCE_DIR}/doublechr.c
  ${XTERM_SOURCE_DIR}/ptydata.c
  ${XTERM_SOURCE_DIR}/version.c
)

target_include_directories(test_xterm
  PRIVATE ${XTERM_SOURCE_DIR}
)

target_link_libraries(test_xterm
  ${X11_ICE_LIB}
  ${X11_X11_LIB}
  ${X11_Xt_LIB}
  ${X11_Xmu_LIB}
  Xaw7
  ${CURSES_LIBRARY}
)

# Make it depend on having the XTerm sources
add_dependencies(test_xterm
  XtermSource)


add_test(
  NAME test_xterm
  COMMAND test_xterm)
