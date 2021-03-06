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

import argparse
import sys
from api import plugin
import ui.output


def help_format_network_scan(prog):
    kwargs = dict()
    kwargs['width'] = ui.output.columns()
    kwargs['max_help_position'] = 34
    format = argparse.HelpFormatter(prog, **kwargs)
    return (format)


def parse(args):
    parser = argparse.ArgumentParser(prog="scan", add_help=False, usage=argparse.SUPPRESS)
    parser.formatter_class = help_format_network_scan
    parser.add_argument('-p', '--port',
                        metavar="<PORT>", default='20-10000')
    parser.add_argument('-t', '--timeout', type=float,
                        metavar="<TIMEOUT>", default=0.2)
    parser.add_argument('address')
    options = vars(parser.parse_args(args))
    options['port'] = parse_port(options['port'])

    return options

def parse_port(input):
    if input.count('-') == 1:
        data = input.split('-')
    else:
        data = [input, input]

    try:
        data = [int(x) for x in data]
    except:
        sys.exit("Illegal port specifications")

    if min(data) < 0 or max(data) > 65535:
        sys.exit("Ports specified must be between 0 and 65535 inclusive")
    if data[0] > data[1]:
        sys.exit("Your port range %d-%d is backwards. Did you mean %d-%d?"
                 % (data[0], data[1], data[1], data[0]))

    return data
