"""
Write solutions in tabular format.
"""
import sys
import textwrap

from tabulate import _table_formats, tabulate


def write_solutions(solutions, **kw):
    """
    Write logic grid solutions to a stream.
    """

    stream = kw.pop("stream", sys.stdout)

    for num, solution in enumerate(solutions, 1):
        # Write header.
        header = "\n" if num > 1 else ""
        header += "Solution " + str(num) + "\n"
        print(header, file=stream)

        # Write solution.
        write_solution(solution, stream=stream, **kw)


def write_solution(solution, stream=sys.stdout, **kw):
    """
    Write a single logic grid solution to a stream.
    """

    indent = kw.pop("indent", 0)

    # Allow special-case 'showindex' value counting from 1.
    if kw.get("showindex", None) is True:
        kw["showindex"] = range(1, len(solution) + 1)

    # Build table text.
    table = [list(row) for row in solution]
    headers = solution[0]._fields
    text = tabulate(table, headers=headers, **kw)

    # Indent as required.
    text = textwrap.indent(text, " " * indent)

    # Write it.
    stream.write(text)
    stream.write("\n")


def table_formats():
    return sorted(_table_formats.keys())
