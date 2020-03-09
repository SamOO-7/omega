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

class History(list):
    """Commands history.

    This class is a specialisation of the list() obj, designed
    to store command line strings only.

    It maintains a `size` property which gives the full size (in bytes)
    of all strings in array.

    To do it, the class operates overriding append(), pop() and clear()
    methods to keep the current size updated in real time.

    """
    MAX_SIZE = 10000
    size = 0

    def append(self, string):
        if not isinstance(string, str):
            raise ValueError("Only strings could be added to history")
        while len(self) >= self.MAX_SIZE:
            self.pop(0)
        self.size += len(string)
        super().append(string)

    def pop(self, index=-1):
        try:
            self.size -= len(self[index])
        except IndexError:
            pass
        super().pop(index)

    def clear(self):
        self.size = 0
        super().clear()
