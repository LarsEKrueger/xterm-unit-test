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
# Main CMake file

cmake_minimum_required(VERSION 3.0.0)
project(XTermUnitTest)

# Download xterm only once
add_custom_command(
  OUTPUT ${CMAKE_BINARY_DIR}/../download/xterm-${XTERM_VERSION}.tar.gz
  COMMAND wget -O ${CMAKE_BINARY_DIR}/../download/xterm-${XTERM_VERSION}.tar.gz ftp://ftp.invisible-island.net/xterm/xterm-${XTERM_VERSION}.tgz
)
add_custom_target(XtermArchive
  DEPENDS ${CMAKE_BINARY_DIR}/../download/xterm-${XTERM_VERSION}.tar.gz
  )

# Unpack the archive when necessary
add_custom_command(
  OUTPUT ${CMAKE_BINARY_DIR}/xterm-${XTERM_VERSION}/configure.sh
  COMMAND tar -f ${CMAKE_BINARY_DIR}/../download/xterm-${XTERM_VERSION}.tar.gz -C ${CMAKE_BINARY_DIR} -x -z
  DEPENDS XtermArchive
)
add_custom_target(XtermSource
  DEPENDS ${CMAKE_BINARY_DIR}/xterm-${XTERM_VERSION}/configure.sh
)

enable_testing()
add_subdirectory(xterm)
