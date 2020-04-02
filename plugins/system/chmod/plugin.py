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

r"""Change file mode bits.

USAGE:
    chmod <mode> <remote_path>

DESCRIPTION:
    The mode parameter consists of three octal number components
    specifying access restrictions for the owner, the user group
    in which the owner is in, and to everybody else in this order.

    One component can be computed by adding up the needed permissions
    for that target user base. Number 1 means that you grant execute
    rights, number 2 means that you make the file writeable,
    number 4 means that you make the file readable.
    Add up these numbers to specify needed rights.

    You can also read more about modes on Unix systems with 'man chmod'.

EXAMPLES:
    > chmod 755 ../cgi-bin/test.cgi
      - Set chmod 755 to test.cgi
    > chmod 4222 /tmp/sploit
      - Grant execution and setuid bit on file
"""

import sys

from api import plugin
from api import server

if len(plugin.argv) != 3:
    sys.exit(plugin.help)

try:
    mode = int(plugin.argv[1], 8)
    assert mode < 0o10000
except:
    sys.exit("invalid mode: '%s'" % plugin.argv[1])

relative_path = plugin.argv[2]
absolute_path = server.path.abspath(relative_path)

payload = server.payload.Payload("payload.php")
payload['FILE'] = absolute_path
payload['MODE'] = mode

response = payload.send()

assert response == 'ok'
