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
Custom string to append to POST data.

Some TARGET URLs may require specific variables to be set
in POST data (http request message body)

This setting only affects HTTP POST Requests, so you should
set REQ_DEFAULT_METHOD to "POST" for it to take effect.

* EXAMPLE:
# if TARGET url needs alternative POST vars to work properly:
> set REQ_POST_DATA "user=admin&pass=w34kp4ss"

* NOTE:
This setting is useful only to specific cases where TARGET URL
cannot work without it, if you don't need it, or don't know what
you're doing, you should ignore this setting until you need it.
"""
import linebuf


linebuf_type = linebuf.MultiLineBuffer


def validator(value):
    return str(value)


def default_value():
    return ""
