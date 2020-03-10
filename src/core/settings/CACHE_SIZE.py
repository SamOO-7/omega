#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Omega Framework
#            ---------------------------------------------------
#                  Copyright (C) <2020>  <Entynetproject>       
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Set the maximum Omega session file size.

While using the Omega Framework, some usage informations
are stored, such as commands history.
Changing this limit ensures that the session, if saved whith
`session save` command will not exceed a certain size.

* USE CASES:
Omega history uses this value to determine the maximum
number of command lines to store in session file.
"""
import linebuf
import datatypes

linebuf_type = linebuf.MultiLineBuffer


def validator(value):
    return datatypes.ByteSize(value)


def default_value():
    return "1 MiB"
