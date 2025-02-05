"""
Logic grid problem solver.
"""
from collections import OrderedDict as odict
from collections import namedtuple

from constraint import (
    AllDifferentConstraint,
    InSetConstraint,
    NotInSetConstraint,
    Problem,
)

class Solver:
    def __init__(self, recname="Group"):
        # Record name for solutions.
        self.recname = recname

        # Mapping of category names to lists of items.
        self.categories = odict()

        # Mapping of item names to their categories.
        self.namemap = {}

        # List of puzzle constraints (function, args).
        self.constraints = []

        # The size of each category.
        self.groups = None

    def category(self, name, items):
        items = list(map(str, items))

        # Check category is unique.
        if name in self.categories:
            raise ValueError(f"category '{name}' is already defined")

        # Check category has content.
        if len(items) == 0:
            raise ValueError(f"category '{name}' has no items")

        # Check categories all have the same size.
        if self.groups is None:
            self.groups = len(items)
        elif self.groups != len(items):
            raise ValueError("all categories must be equal size")

        # Check item names are unique.
        for item in items:
            cname = self.namemap.get(item, None)
            if not cname:
                self.namemap[item] = name
            else:
                raise ValueError(f"'{item}' used in category '{cname}'")

        # Add the new category.
        self.categories[name] = items

    def group_is(self, item, groups):
        self.validate(item)
        groups = collection(groups)
        groups = list(map(int, groups))
        func = InSetConstraint(groups)
        self.constraints.append([func, [item]])

    def group_isnot(self, item, groups):
        self.validate(item)
        groups = collection(groups)
        groups = list(map(int, groups))
        func = NotInSetConstraint(groups)
        self.constraints.append([func, [item]])

    def group_same(self, item1, item2):
        self.validate(item1, item2)

        def func(x, y):
            return x == y

        self.constraints.append([func, [item1, item2]])

    def group_notsame(self, item1, item2):
        self.validate(item1, item2)

        def func(x, y):
            return x != y

        self.constraints.append([func, [item1, item2]])

    def group_nextto(self, item1, item2):
        self.group_diff(item1, item2, [-1, 1])

    def group_leftof(self, item1, item2):
        self.group_diff(item1, item2, -1)

    def group_rightof(self, item1, item2):
        self.group_diff(item1, item2, 1)

    def group_diff(self, item1, item2, diff):
        self.validate(item1, item2)
        diff = collection(diff)

        def func(x, y):
            return x - y in diff

        self.constraints.append([func, [item1, item2]])

    def validate(self, *items):
        for item in items:
            if item not in self.namemap:
                raise ValueError(f"'{item}' is not in any category")

    def problem(self):
        if not self.categories:
            raise ValueError("no categories defined")

        p = Problem()

        # Add items from each category.
        for items in self.categories.values():
            # One variable per item.
            p.addVariables(items, list(range(1, self.groups + 1)))

            # Each item in a category must have different group.
            p.addConstraint(AllDifferentConstraint(), items)

        # Add explicit constraints.
        for func, values in self.constraints:
            p.addConstraint(func, values)

        return p

    def solve(self):
        # Create solution record.
        fields = self.categories.keys()
        rec = namedtuple(self.recname, fields)

        # Get solutions from solver.
        for sol in self.problem().getSolutionIter():
            # Create a solution record for each group.
            solution = []
            for group in range(1, self.groups + 1):
                data = {}
                for name, items in self.categories.items():
                    for item in items:
                        if sol[item] == group:
                            data[name] = item

                solution.append(rec(**data))

            yield solution


def collection(value):
    if not isinstance(value, set | list | tuple):
        return set([value])
    else:
        return value
