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

"""Omega Framework core loader.

This pseudo module is designed to be imported (import lib) from
the Omega script launcher (./Omega).
It also can be imported from Omega root directory through a
python interpreter for debugging purposes.

It loads the Omega core, spreading required dependencies
(./deps directory) then overwriting sys.path's first element to
the current directory (./lib/), making all self contained elements
directly importable from python.

"""
import os
import sys

# load Omega dependencies before anything else
import deps

from . import utils

BASEDIR = utils.path.truepath(sys.path[0]) + os.sep
COREDIR = os.path.join(BASEDIR, __name__) + os.sep

# use current directory as main python path
sys.path[0] = COREDIR

del deps, sys, os  # clean package's content
