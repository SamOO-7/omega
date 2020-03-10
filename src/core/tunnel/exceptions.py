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

"""Omega requests and tunnel exceptions
"""
__all__ = ["BuildError", "RequestError", "ResponseError"]


class TunnelException(Exception):
    """Parent class for tunnel exception types
    """


class BuildError(TunnelException):
    """Tunnel request builder exception

    This exception is raised by the tunnel handler if
    something during the request crafting process fails.

    Used by the tunnel.handler.Request().Build() method.
    """


class RequestError(TunnelException):
    """Tunnel request sender exception

    This exception is raised by the tunnel handler if
    something fails while sending Omega requests.

    Used by the tunnel.handler.Request.Send() method.
    """


class ResponseError(TunnelException):
    """Tunnel payload dumper exception

    This exception is raised by the tunnel handler if
    the process of payload response extraction within
    the HTTP response fails.

    Used by the tunnel.handler.Request.Read() method.
    """
