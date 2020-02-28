"""Omega base core elements loader.

The most basic Omega elements manager.
It handles user configuration directory, and defines
basic elements such as the following strings:
    BASEDIR -> /path/to/omega/
    COREDIR -> /path/to/omega/core/
    USERDIR -> /home/user/.omega/
"""
# constant directories
from src import BASEDIR, COREDIR
from .config import USERDIR

# session instance
from .session import session

# tunnel instance
from .tunnel import tunnel

# plugins instance
from .plugins import plugins
