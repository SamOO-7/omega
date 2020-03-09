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

"""Omega User Input (STDIN) Handler

This package provides UI features relaed to Standard Input
"""
__all__ = ["Expect", "isatty"]

import sys
from .expect import Expect


def isatty() -> bool:
    """Return whether input is an 'interactive' stream.

    Return False if it can't be determined.
    """
    return sys.__stdin__.isatty()
