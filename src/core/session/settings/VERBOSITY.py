"""
Enable or Disable omega framework verbosity.
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    return datatypes.Boolean(value)


def default_value():
    return False
