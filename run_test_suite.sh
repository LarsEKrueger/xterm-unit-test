#! /bin/bash

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
# Main start script

SELF=$(readlink -f "$0")
SELFDIR=$(dirname "$SELF")

CMAKE=cmake
XTERM_VERSION=337

DOWNLOADDIR="${SELFDIR}/download"
mkdir -p "${DOWNLOADDIR}"

BUILDDIR="${SELFDIR}/build"
mkdir -p "${BUILDDIR}"
cd "$BUILDDIR"
"${CMAKE}" -DXTERM_VERSION:STRING="$XTERM_VERSION" "$SELFDIR"

make && make test