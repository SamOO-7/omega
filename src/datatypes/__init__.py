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

"""Useful data types collection.

This package includes some useful data types, which supports
dynamic value and enhanced representations.
It has been developped in order to properly handle the Omega
framework's session settings and environment variables.

Omega dedicated datatypes obey the following conventions:
=============================================================

* _raw_value()
    Returns the unherited type's raw value. It convention has been
    made to assist session pickling, because even if custom types
    can be pickled, it stands hard to work with pickled sessions
    on future Omega versions that use different datatypes names,
    or if the structure changes in the future.
    >>> val = Interval('1-10')
    >>> print( type(val), "==>", repr(val) )
    <class 'datatypes.Interval.Interval'> ==> (1.0, 10.0)
    >>> raw = val._raw_value()
    >>> print( type(raw), "==>", repr(raw) )
    <class 'tuple'> ==> (1.0, 10.0)

* __call__()
    Returns a usable value. If dynamic, it must return one of the
    possible values. In the case it is static, it returns the same as
    _raw_value().
    >>> val = Interval('1-10')
    >>> val()
    3.2

* __str__()
    Returns a nice string representation of the object, it may include
    ANSI colors, because the Omega framework's output manager
    automagically strips them if they cannot be displayed anyways.
    >>> print(Interval('1-10'))
    1 <= x <= 10 (random interval)

* Initialization:
    Any data type MUST be able to take its _raw_value() as instance
    initializer.
    >>> Interval( Interval("1-10")._raw_value() ) # it must be valid

"""

from .ByteSize import ByteSize
from .Boolean import Boolean
from .Path import Path
from .WebBrowser import WebBrowser
from .Interval import Interval
from .Proxy import Proxy
from .Url import Url
from .Code import Code
from .PhpCode import PhpCode
from .ShellCmd import ShellCmd
