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

import metadict
from core import session, tunnel, plugins
from datatypes import Path


class Payload(metadict.MetaDict):
    # the omega env vars to auto add
    # to $OMEGA array on php side
    _unherited_env_vars = ["PATH_SEP"]

    _php_vars_template = 'global $OMEGA;$OMEGA=%s;\n'

    def __init__(self, filename, **kwargs):
        self.response = None
        for key in self._unherited_env_vars:
            self[key] = session.Env[key]
        for key, value in kwargs.items():
            self[key] = value
        plugin_path = plugins.current_plugin.path
        self.payload = Path(plugin_path, filename, mode='fr').phpcode()

    def send(self, **kwargs):
        var_list = dict(self)
        for key, value in kwargs.items():
            var_list[key] = value
        php_vars = self._php_vars_template % tunnel.payload.py2php(var_list)

        result = tunnel.send(php_vars + self.payload)
        if result.response_error:
            raise PayloadError(result.response_error)
        return result.response


class PayloadError(Exception):
    """Exception raised when a send payload returned an __ERROR__ obj"""
