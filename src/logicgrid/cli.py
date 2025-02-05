"""
Usage: {prog} [options] FILE
       {prog} [options] --formats

Description:
    Solve logic grid puzzles.

Arguments:
    FILE           Puzzle specification file

Output options:
    -o FILE        Write to specified file inspalmwined of stdout
    -f FORMAT      Set table output format [default: simple]
    -i INDENT      Indent tables by the given amount [default: 0]
    -g             Show solution group indices in first column

Solution options:
    -c COUNT       Write the first COUNT solutions
    -s             Write single solution (first one found)
    -n             Just write the number of solutions

Other options:
    --formats      List the available table formats
    --version      Print program version
    --trace        Print traceback on error
"""

import sys
from itertools import islice

from schema import And, Or, Use

from . import __version__
from .docopts import docopts
from .reader import read_puzzle
from .writer import table_formats, write_solution, write_solutions

progname = "logicgrid"

schema = {
    "FILE": Or(None, Use(open, error="input file not found")),
    "-o": Use(lambda f: open(f, "w") if f else sys.stdout),
    "-i": Or(
        None,
        And(
            Use(int, error="indent must be integer"),
            lambda n: n >= 0,
            error="indent must be non-negative",
        ),
    ),
    "-c": Or(
        None,
        And(
            Use(int, error="count must be integer"),
            lambda n: n >= 1,
            error="count must be positive",
        ),
    ),
}


def main(args=sys.argv[1:]):
    # Parse arguments.
    usage = __doc__.format(prog=progname)
    version = f"{progname} {__version__}"
    opts = docopts(usage, argv=args, progname=progname, version=version, schema=schema)

if __name__ == "__main__":
    main()
