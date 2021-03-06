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

r"""Copy a file.

USAGE:
    cp <remote_path> <remote_path>

OPTIONS:
    -f
        Overwrite remote directory without user confirmation.

DESCRIPTION:
    Copy a remote file to another remote destination.
    - remote file must be readable.
    - remote directory must be a writable directory.
    - Unless '-f' option has been provided, user confirmation is
    needed to overwrite remote directory (if it already exists).

LIMITATIONS:
    Unlike the standard GNU's 'cp' tool, recursive directory
    and multiple file copy are not available.

EXAMPLES:
    > cp -f exploit.php ../images/archive
      - Copy an exploit to a stealth location, force copy.
"""

import sys

from api import plugin
from api import server

argc = len(plugin.argv)

if argc not in [3, 4]:
    sys.exit(plugin.help)

payload = server.payload.Payload("payload.php")
payload['FORCE'] = 0

src_arg, dst_arg, arglen = [1, 2, argc]
if plugin.argv[1] == '-f':
    payload['FORCE'] = 1
    src_arg, dst_arg, arglen = [2, 3, (argc - 1)]

if arglen != 3:
    sys.exit(plugin.help)

payload['SRC'] = server.path.abspath(plugin.argv[src_arg])
payload['DST'] = server.path.abspath(plugin.argv[dst_arg])

src, dst = payload.send()

print("Copy complete: '%s' -> '%s'" % (src, dst))
