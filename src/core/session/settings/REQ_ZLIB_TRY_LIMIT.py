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
Control over which payload size the zlib compression feature
will be disabled.

The omega request engine does'its best to compress and fit
the payload within as little HTTP Requests as possible.

Therefore, zlib compression becomes exponentially CPU greedy
as payload size gows up, and it might be extremelly slow to
process very large requests.

The REQ_ZLIB_TRY_LIMIT defines a value over which the payload
is no more processed by zlib compression. Payloads over this
value will then be encoded without zlib compression, making them
bigger, but also a lot faster to generate.
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    value = datatypes.ByteSize(value)
    if value < 1:
        raise ValueError("must be a positive bytes number")
    return value


def default_value():
    return "20 MiB"
