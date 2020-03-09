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

from shnake import parse

from .Code import Code


class ShellCmd(Code("sh")):
    """ShellCmd is an executable program or shell command. (extends str)

    Takes an executable program path or shell command.

    >>> text_editor = ShellCmd('vim')
    >>> text_editor()
    "vim"

    """
    def __new__(cls, executable):
        try:
            parse(executable)
        except SyntaxError:
            raise ValueError("«%s» is not a valid shell command" % executable)

        # Value is OK, now we maintain original.
        return str.__new__(cls, executable)
