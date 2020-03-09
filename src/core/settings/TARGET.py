
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if str(value).lower() in ["", "none"]:
        return default_value()
    else:
        return datatypes.Url(value)


def default_value():
    return None
