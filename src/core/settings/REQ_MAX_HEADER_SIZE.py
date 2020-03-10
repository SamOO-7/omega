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
Set the maximum length of a single HTTP Header.

This setting is needed to tell Omega to generate HTTP
requests that are acceptable for the target server.

* EXAMPLE:
Most http servers allow up to 4KB of data per HTTP Header.
Therefore, if the server is configured to only allow up to
500 bytes Headers, Omega could fail to execute payloads
unless you change value of REQ_MAX_HEADER_SIZE to 500:
> set REQ_MAX_HEADER_SIZE 500

* NOTE:
If you encounter http error 500 or if payload execution fails,
you may need to lower the default limit of this setting.

* REFERENCES:
http://httpd.apache.org/docs/2.2/mod/core.html#LimitRequestFields
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    value = datatypes.ByteSize(value)
    if 250 > value:
        raise ValueError("can't be less than 250 bytes")
    return value


def default_value():
    return "4 KiB"
