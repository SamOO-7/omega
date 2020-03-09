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

from ui.color import colorize


class Boolean(int):
    """High level boolean representation. (extends int)

    This datatype could be instanciated by passing a string
    "True" of "False", both case insensitive.
    It also can pass an int, 0 meaning false, and anything else
    true.

    >>> Boolean("fAlSe")
    False
    >>> Boolean(1)
    True
    >>> Boolean(False)
    False
    """

    def __new__(cls, value):
        try:
            value = int(value)
        except ValueError:
            value = str(value).capitalize()
            if value == "False":
                value = False
            elif value == "True":
                value = True
            else:
                raise ValueError("boolean must be True/False")
        return int.__new__(cls, value)

    def _raw_value(self):
        return int(self)

    def __call__(self):
        return self._raw_value()

    def __str__(self):
        return colorize("%BoldCyan", "True" if self else "False")
