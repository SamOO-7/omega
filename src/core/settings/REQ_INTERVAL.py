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
Interval (in seconds) to wait between HTTP requests.

While sending large payload (like uploading a big file with
`upload` plugin), this setting can improve stealth by
preventing the remove IDS to raise alerts or block your IP
due to excess of consecutive HTTP requests.

* EXAMPLES:

# randomly sleep between 1 and 10 seconds between requests:
> set REQ_INTERVAL 1-10

# sleep exactly 3 seconds between requests:
> set REQ_INTERVAL 3
"""

import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    return datatypes.Interval(value)


def default_value():
    return "1-10"
