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

"""A decorator for separating readline context.
"""


def isolate_readline_context(function):
    """A decorator for separating readline context.

    This decorator isolates readline context of target
    function or method.

    Use when omega's readline context should be
    reset temporarly is the context of triggering
    function or method.

    Unlike `isolate_io_context`, this decorator keeps
    original stdout wrapper.
    """
    def wrapper(*args, **kwargs):
        try:
            import readline
            handle_readline = True
        except ImportError:
            handle_readline = False

        if handle_readline:
            # backup & reset readline completer
            old_readline_completer = readline.get_completer()
            readline.set_completer((lambda x: x))
            # backup & reset readline history
            old_readline_history = []
            hist_sz = readline.get_current_history_length()
            for i in range(1, hist_sz + 1):
                line = readline.get_history_item(i)
                old_readline_history.append(line)
            readline.clear_history()

        try:
            retval = function(*args, **kwargs)
        finally:

            if handle_readline:
                # restore old readline completer
                readline.set_completer(old_readline_completer)
                # restore old readline history
                readline.clear_history()
                for line in old_readline_history:
                    readline.add_history(line)

        return retval
    return wrapper
