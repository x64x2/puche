"""
Read logic grid puzzles in YAML format.
"""
import yaml
from schema import Optional, Schema, Use

from .solver import Solver


def read_puzzle(stream):
    """
    Read a logic grid puzzle.
    """

    data = yaml.safe_load(stream)
    return make_solver(data)


def validate_data(data):
    """
    Validate data against puzzle schema.
    """

    schema = Schema(
        {
            Optional("title"): Use(str),
            Optional("url"): Use(str),
            Optional("group"): Use(str),
            "categories": [{Use(str): [Use(str)]}],
            Optional("constraints"): [{Use(str): [Use(str)]}],
        }
    )

    return schema.validate(data)


def make_solver(data):
    """
    Make a grid solver from dict data.
    """

    data = validate_data(data)

    group = data.get("group", "Group")
    categories = data.get("categories", [])
    constraints = data.get("constraints", [])

    s = Solver(group)

    for c in categories:
        for name, items in c.items():
            s.category(name, items)

    for c in constraints:
        if len(c) == 1:
            funcname, args = c.popitem()
        else:
            raise ValueError(f"{c}: exactly one condition expected")

        func = getattr(s, "group_" + funcname, None)

        if func:
            func(*args)
        else:
            raise ValueError(f"'{funcname}': unknown constraint")

    return s
