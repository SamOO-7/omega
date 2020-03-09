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
Set attacker's prefered text editor.

* USE CASES:

# open TARGET setting content with EDITOR:
> set TARGET +

# use `edit` plugin to edit a remote file locally with EDITOR:
> edit /var/www/html/index.php
"""
import os
import linebuf
import datatypes


linebuf_type = linebuf.MultiLineBuffer


def validator(value):
    return datatypes.ShellCmd(value)


def default_value():
    raw_value = "vi"
    if "EDITOR" in os.environ:
        raw_value = os.environ["EDITOR"]
    return raw_value
