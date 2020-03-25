"""Plugin's `plugin.py` file docstring (title line)

USAGE:
    plugin_example

DESCRIPTION:
    This plugin is a sample made to understand how
    Omega plugins are structured.

    If the `api` module is imported outside a real plugin
    runtime, then the API defaulty assumes this sample plugin
    as the current one for learning purposes.

    This text is the docstring of current plugin's
    python file (plugin.py). It means that running `help <plugin>`
    will display this docstring.

    Writting a plugin should comport a docstring formatted like
    this one, with at least a title (first line), and the
    following sections:
        SYNOPSIS
        DESCRIPTION
"""

# standard library modules
import sys

# Omega Framework modules
import api


print(" ".join(api.plugin.argv))
sys.exit()
