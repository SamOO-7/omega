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

r"""Change current directory.

USAGE:
    cd <remote_dir>

DESCRIPTION:
    Change current working directory of omega target.

    - This plugin checks if the given path is remotely
    reachable, then changes $PWD environment variable if
    no errors were found.
    - If run without argument, $HOME env var is used as
    new current working directory.

EXAMPLES:
    > cd ..
      - Go to the directory below
    > cd "C:\Program Files\"
      - Go to "Program Files" directory
    > cd ~
      - Move the the user's HOME directory

ENVIRONMENT:
    * PWD
        The current remote working directory

WARNING:
    - Manual edition of the $PWD environment variable without using
    this plugin is usually a bad idea, because we take the risk
    to set it to an invalid location, without the checks done by
    this plugin.
    - Therefore, in a few use cases, manual edition of the $PWD
    variable is the only option.
"""

import sys

from api import plugin
from api import server
from api import environ

if len(plugin.argv) > 2:
    sys.exit(plugin.help)

if len(plugin.argv) == 2:
    relative_path = plugin.argv[1]
else:
    relative_path = environ['HOME']

absolute_path = server.path.abspath(relative_path)

payload = server.payload.Payload("payload.php")
payload['DIR'] = absolute_path

response = payload.send()

if response != "ok":
    sys.exit("Unexpected response: %r" % response)

# change $PWD omega environment variable
environ['PWD'] = absolute_path
