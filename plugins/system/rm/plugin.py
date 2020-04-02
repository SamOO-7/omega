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

"""Remove a remote file.

USAGE:
    rm <remote_path>

DESCRIPTION:
    Remove remote file from server.

LIMITATIONS:
    Unlike the standard GNU's 'rm' tool, recursive
    and multiple file removal are not available.

EXAMPLES:
    > rm pdfs/r57.php
      - Remove "./pdfs/r75.php" file from remote server
"""

import sys

from api import plugin
from api import server

if len(plugin.argv) not in [2, 3]:
    sys.exit(plugin.help)

recurse = 0

if plugin.argv[1] == "-r":
    if len(plugin.argv) == 2:
        sys.exit(plugin.help)
    recurse = 1
    rel_path = plugin.argv[2]
else:
    if len(plugin.argv) == 3:
        sys.exit(plugin.help)
    rel_path = plugin.argv[1]

abs_path = server.path.abspath(rel_path)
dirname = server.path.dirname(abs_path)
basename = server.path.basename(abs_path)

if recurse:
    sys.exit("Recursive mode is not yet available")

payload = server.payload.Payload("single.php")
payload["FILE"] = abs_path

payload.send()
