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
Use a proxy to connect to the target

You can set a proxy in order to encapsulate the whole Omega
requests for furtivity or network analysis purposes.

This setting supports HTTP, HTTPS, SOCKS4
and SOCKS5 proxy schemes.

PROXY SYNTAX: <SCHEME>://<ADDRESS>:<PORT>

* EXAMPLES:

# To unset PROXY, set it's value to 'None' magic string:
> set PROXY None

# To set a socks5 proxy to connect through Tor:
> set PROXY socks5://127.0.0.1:9050
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    return datatypes.Proxy(value)


def default_value():
    return None
