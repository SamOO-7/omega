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

"""Create a directory.

USAGE:
    mkdir <remote_dir>

OPTIONS:
    -p
        No error if existing, make parent directories as needed.

DESCRIPTION:
    The 'mkdir' plugin creates remote directory. It reports
    an error if it already exists.
    - Unless '-p' option is provided, parent directory must exist.

LIMITATIONS:
    Unlike GNU's mkdir core util, this plugin does not support
    multiple path arguments.

EXAMPLES:
    > mkdir includes
      - Create the 'includes' directory from current location
    > mkdir /srv/www/data/img/thumb/
      - Create the 'thumb' directory if it's parent exists
    > mkdir /srv/www/data/img/thumb/
      - Create the 'thumb' directory even if parent don't exist
    > mkdir -p /var/www/a/b/c/d/e/f/g/h/
      - Create 'h/' directory, and parent directories as needed.
"""

import sys

from api import plugin
from api import server
from api import environ

if len(plugin.argv) == 2 and plugin.argv[1] != '-p':
    relpath = plugin.argv[1]
elif len(plugin.argv) == 3 and plugin.argv[1] == '-p':
    relpath = plugin.argv[2]
else:
    sys.exit(plugin.help)

abspath = server.path.abspath(relpath)

if plugin.argv[1] == '-p':
    payload = server.payload.Payload("parent.php")
    drive, path = server.path.splitdrive(abspath)
    payload['DRIVE'] = drive
    payload['PATH_ELEMS'] = [x for x in path.split(environ['PATH_SEP']) if x]
else:
    payload = server.payload.Payload("payload.php")
    payload['DIR'] = abspath

payload.send()
