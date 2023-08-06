"""TEDDecor
Inline markown parsing and printing

This is a easy to use library that gives a user access to colored text, bold text,
underlined text, hyperlinks and much more.
"""

__version__ = "1.3.1"
from .TED import TED, style, Color
from .logger import LL, Log, Logger
from .pprint import p_value, pprint
from . import decorators
