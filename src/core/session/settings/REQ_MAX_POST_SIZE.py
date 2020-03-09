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
Set max size of POST data allowed in an HTTP request.

This setting is needed to tell omega to generate HTTP
requests that are acceptable for the target server.

* EXAMPLE:
Most http servers allow up to 4MiB per request message body.
Therefore, if the server is configured to only allow up
to 300KiB, omega could fail to execute payloads
unless you change value of REQ_MAX_HEADERS to 300 KiB:
> set REQ_MAX_HEADERS 300KiB

* NOTE:
If you encounter http error 500 or if payload execution fails,
you may need to lower the default limit of this setting.

* REFERENCES:
http://httpd.apache.org/docs/2.2/mod/core.html#LimitRequestBody
https://secure.php.net/manual/en/ini.core.php#ini.post-max-size
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
    return "4 MiB"
