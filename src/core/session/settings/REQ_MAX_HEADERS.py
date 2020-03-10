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
Define how many HTTP Headers can be sent in a request.

This setting is needed to tell Omega to generate HTTP
requests that are acceptable for the target server.

* EXAMPLE:
Most http servers allow up to 100 Headers per HTTP request.
Therefore, if the server is configured to only allow up
to 20 headers, Omega could fail to execute payloads
unless you change value of REQ_MAX_HEADERS to 20:
> set REQ_MAX_HEADERS 20

* NOTE:
If you encounter http error 500 or if payload execution fails,
you may need to lower the default limit of this setting.

* REFERENCES:
http://httpd.apache.org/docs/2.2/mod/core.html#LimitRequestFieldSize
"""
import linebuf


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if 10 <= int(value) <= 680:
        return int(value)
    raise ValueError("must be an integer from 10 to 680")


def default_value():
    return 100
