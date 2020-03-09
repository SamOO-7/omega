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

import re
from .Code import Code


class PhpCode(Code("php")):
    """Line of PHP Code. (extends str)
    Takes a string representing a portion of PHP code.

    >>> code = PhpCode('<? phpinfo() ?>')
    >>> code()
    'phpinfo();'
    >>> print(code)
    '<?php phpinfo(); ?>'

    """
    def __new__(cls, string):
        pattern = (r"^(?:<\?(?:[pP][hH][pP])?\s+)?\s*("
                   r"[^\<\s].{4,}?)\s*;?\s*(?:\?\>)?$")
        # disable check if code is multiline
        string = string.strip()
        if len(string.splitlines()) == 1:
            try:
                # regex validates and parses the string
                string = re.match(pattern, string).group(1)
            except:
                raise ValueError('«%s» is not PHP code' % string)

        return super().__new__(cls, string)

    def _code_value(self):
        return "<?php %s; ?>" % self.__call__()
