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
This variable contains php code which is interpreted
on each http request, just before payload execution.

This setting can be used for example in order to
override a php configuration option with a value
that extends execution scope.

The code will be executed before ANY payload execution.

* Only edit PAYLOAD_PREFIX if you really understand what you're doing
"""
import core
import linebuf
import datatypes


linebuf_type = linebuf.MultiLineBuffer


def validator(value):
    return datatypes.PhpCode(value)


def default_value():
    file_relpath = "data/tunnel/payload_prefix.php"
    file = datatypes.Path(core.BASEDIR, file_relpath)
    return file.read()
