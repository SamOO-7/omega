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

"""Remove empty directory

SYNOPSIS:
    rmdir <REMOTE-DIRECTORY>

DESCRIPTION:
    Remove REMOTE-DIRECTORY if it is empty.

AUTHOR:
    Entynetproject
"""

import sys

from api import plugin
from api import server

if len(plugin.argv) != 2:
    sys.exit(plugin.help)

rel_path = plugin.argv[1]
abs_path = server.path.abspath(rel_path)

payload = server.payload.Payload("payload.php")
payload["DIR"] = abs_path

payload.send()
