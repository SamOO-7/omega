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

import re

import linebuf


linebuf_type = linebuf.MultiLineBuffer


def validator(value):
    value = str(value)
    reserved_headers = ['host', 'accept-encoding', 'connection',
                        'user-agent', 'content-type', 'content-length']
    if not value:
        raise ValueError("can't be an empty string")
    if not re.match("^[a-zA-Z0-9_]+$", value):
        raise ValueError("only chars from set «a-Z0-9_» are allowed")
    if re.match('^zz[a-z]{2}$', value.lower()) or \
       value.lower().replace('_', '-') in reserved_headers:
        raise ValueError("reserved header name: «{}»".format(value))
    return value


def default_value():
    raw_value = "omega"
    return raw_value
