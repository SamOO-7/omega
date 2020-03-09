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

from core import session


def readonly_settings(*decorator_args):
    # no args = all settings
    if not decorator_args:
        decorator_args = list(session.Conf.keys())

    def decorator(function):
        def wrapper(*args, **kwargs):
            # backup all protected settings
            protected_settings = {}
            for name in decorator_args:
                protected_settings[name] = session.Conf[name]
            # execute decorated function
            try:
                retval = function(*args, **kwargs)
            # restore protected settings
            finally:
                for name, value in protected_settings.items():
                    session.Conf[name] = value
            return retval

        return wrapper

    return decorator
