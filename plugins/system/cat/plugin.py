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

r"""Print a file content.

USAGE:
    cat <remote_path>

DESCRIPTION:
    Print a file content.

LIMITATIONS:
    Unlike the standard GNU's 'cat' tool, multiple files cat
    is not supported.

EXAMPLES:
    > cat ../includes/connect.inc.php
      - Display the connect.inc.php's content.
"""

import sys
import base64

from core import encoding

from api import plugin
from api import server

if len(plugin.argv) != 2:
    sys.exit(plugin.help)

relative_path = plugin.argv[1]
absolute_path = server.path.abspath(relative_path)

payload = server.payload.Payload("payload.php")
payload['FILE'] = absolute_path

response = payload.send()

data = encoding.decode(base64.b64decode(response))
print(data)
