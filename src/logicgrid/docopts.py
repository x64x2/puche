"""
Docopt wrapper.
"""

import re
import sys

from docopt import docopt
from schema import Schema, SchemaError


class docopts:
    """Improved docopt front end.

    - Allow access via attributes as well
    - Apply schema validation
    """

    def __init__(self, *args, **kw):
        # Get program name.
        progname = kw.pop("progname", None)

        # Get option schema.
        schema = kw.pop("schema", {})

        # Pass rest of args to docopt.
        opts = docopt(*args, **kw)

    def __getattr__(self, attr):
        return self._opts[attr]
