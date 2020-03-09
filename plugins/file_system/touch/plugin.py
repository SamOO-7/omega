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

"""Change file timestamps

SYNOPSIS:
    touch [OPTION]... <REMOTE-FILE>

OPTIONS:
    -t <STAMP>
        use YYYY[-mm[-dd[ HH[:MM[:SS]]]]] instead of current time
        NOTE: If partially defined (e.g: yyyy/mm only), other
              values will be randomly chosen, because random values
              are always less suspicious than 00:00:00
    -r <REF-FILE>
        use this remote file's times instead of current time

DESCRIPTION:
    Update the access and modification times of REMOTE-FILE
    to the current time.

    If REMOTE-FILE does not exist, it is created empty.

EXAMPLES:
    > touch file.txt
      - Set file atime/mtime to current time
    > touch -t '2012/12/21 23:59:59' file.txt
      - Set file atime/mtime to Dec 21 23:59:59 2012
    > touch -t '2015' file.txt
      - Set file atime/mtime to a random date in 2015
    > touch -r old.php new.php
      - Set `new.php`'s times to same values as `old.php`

AUTHOR:
    Entynetproject
"""

import sys

import utils

from api import plugin
from api import server

timestamp = None
reference = None

if len(plugin.argv) == 2:
    relative_path = plugin.argv[1]
elif len(plugin.argv) == 4 and plugin.argv[1] == '-t':
    timestamp = utils.time.get_smart_date(plugin.argv[2])
    relative_path = plugin.argv[3]
elif len(plugin.argv) == 4 and plugin.argv[1] == '-r':
    reference = server.path.abspath(plugin.argv[2])
    relative_path = plugin.argv[3]
else:
    sys.exit(plugin.help)

absolute_path = server.path.abspath(relative_path)

payload = server.payload.Payload("payload.php")
payload['FILE'] = absolute_path
payload['TIME'] = timestamp
payload['REF'] = reference

response = payload.send()
assert response == 'OK'
