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

"""Print working directory

SYNOPSIS:
    pwd

DESCRIPTION:
    Print the absolute path name of current/working remote
    directory on target server.

    * PASSIVE PLUGIN:
    No requests are sent to server, as current directory
    is known by $PWD environment variable (`env PWD`)

AUTHOR:
    Entynetproject
"""

from api import environ

print(environ['PWD'])
