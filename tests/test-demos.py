"""
Test the demo puzzles.
"""

from logicgrid import read_puzzle, write_solutions


def test_demos(demodir):
    for path in demodir.glob("*.yaml"):
        with open(path) as f:
            s = read_puzzle(f)
            solutions = s.solve()
            write_solutions(solutions)
