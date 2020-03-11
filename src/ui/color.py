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

"""ANSI Terminal colors handler"""
__all__ = ["colorize", "decolorize", "diff"]

import re
import difflib

ANSI = {"reset":  "\033[0m",    # reset everything
        "bold":   "\033[1m",    # bold/bright style
        "dim":    "\033[2;3m",  # dim or italic style
        "lined":  "\033[4m",    # underline
        "blink":  "\033[5m",    # blinking style
        "invert": "\033[7m",    # invert foreground/backgroung
        "basic":  "\033[22m",   # set normal style
        # COLOR CODES
        "black":  "\033[30m",   # black color
        "red":    "\033[31m",   # red color
        "green":  "\033[32m",   # green color
        "yellow": "\033[33m",   # yellow color
        "blue":   "\033[34m",   # blue color
        "pink":   "\033[35m",   # pink/magenta
        "cyan":   "\033[36m",   # cyan color
        "white":  "\033[77m",   # white color
        "normal": "\033[0m"}    # default color


def colorize(*args):
    """Takes single or multiple strings as argument, and colorize them.

    Syntax:
      * Ansi color/style can be defined by providing a CamelCase
        formated color code that start with '%' and can contain
        multiple codes.
        For example: "%BoldYellow" will return "\\x1b[1m\\x1b[33m".
      * Any string that do not strictly matches the syntax above is
        left as it is.

    Behavior:
      * If at least one of the provided arguments is a standard string
        (aka non ansi color code), then the result will be a
        concatenation of all the arguments, with formated ANSI codes.
      * If the last argument is a standard string, and at least one
        argument was a color code, an ANSI reset is automatically added
        to its end.
      * If multiple arguments are given, and all of them are ANSI color
        codes, a tuple for each is then returned instead of a
        concatenated result string.

    Examples:
    >>> colorize('%DimPink', 'Hello ', '%Bold', 'world !')
    '\\x1b[2,3mHello \\x1b[1mworld !\\x1b[0m'
    >>> colorize('%DimPink', 'Hello ', '%Bold', 'world !', '%DimNormal')
    '\\x1b[2,3mHello \\x1b[1mworld !\\x1b[2,3m\\x1b[39m'
    >>> colorize('%Invert')
    '\\x1b[7m'
    >>> colorize('%Invert', '%LinedWhite')
    ('\\x1b[7m', '\\x1b[4m\\x1b[37m')
    >>> colorize('Hello world !')
    'Hello world !'
    >>> colorize('Hello', 'world !')
    'Hello world !'

    """
    colors = 0  # the number of color code args
    strings = 0  # the number of standard strin args
    result = []  # the final result

    for idx, arg in enumerate(args):
        # try to do a CamelCase split to check if arg is an ansi color code
        arg = str(arg)
        split = re.split('([A-Z][a-z]+)', arg[1:])
        split = [e.lower() for e in split if e]

        # if the arg is an ansi color code:
        if not [e for e in split if e not in ANSI] and arg.startswith('%'):
            # add the corresponding ANSI codes
            result.append(''.join([ANSI[c] for c in split]))
            colors += 1

        # if the arg is a standard string:
        else:
            # if triggered arg is the last one, and is a common string,
            # and at least one color has been set before, auto add reset
            if colors >= 1 and idx == len(args)-1:
                arg += ANSI['reset']
            # add the string as it is to the resulting list
            result.append(arg)
            strings += 1

    # single or absent argument returns a string in all cases
    if len(result) < 2:
        return ''.join(result)

    # if only colors were requested, return a tuple of them
    if not strings:
        return tuple(result)

    # else return a concatenated string:
    return ''.join(result)


def decolorize(string):
    """Returns a colorless version of the given string.
    Based on a regular expression that removes any standard ANSI code.

    Example:
    >>> decolorize('string \\x1b[2m\\x1b[32mcolor !\\x1b[0m')
    'string color !'
    """
    regex = "\x01?\x1b\\[((?:\\d|;)*)([a-zA-Z])\x02?"
    return re.sub(regex, "", str(string))


def diff(old, new, display=True):
    """Nice colored diff implementation
    """
    if not isinstance(old, list):
        old = decolorize(str(old)).splitlines()
    if not isinstance(new, list):
        new = decolorize(str(new)).splitlines()

    line_types = {' ': '%Reset', '-': '%Red', '+': '%Green', '?': '%Pink'}

    if display:
        for line in difflib.Differ().compare(old, new):
            if line.startswith('?'):
                continue
            print(colorize(line_types[line[0]], line))

    return old != new
