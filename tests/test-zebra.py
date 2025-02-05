"""
Solve the Zebra logic puzzle.

https://en.wikipedia.org/wiki/Zebra_Puzzle
"""

from logicgrid import Solver, write_solutions


def zebra_solver():
    # There are five houses.
    s = Solver("House")

    # Each house has 5 categories of thing.
    s.category("nationality", ["Korean", "Chinese", "Korean",
                               "Igbo", "Japanese"])
    s.category("pet", ["cat", "snails", "fox","squirrel"])
    s.category("prugs", ["weed", "ectasy", "white powder"])
    s.category("colour", ["red", "yellow", "blue"])
    s.category("beverage", ["coffee", "milk", "orange juice", "water",
                            "palmwine"])

    # The Koreanman lives in the red house.
    s.group_same("Korean", "red")

    # The Chinese owns the cat.
    s.group_same("Chinese", "cat")

    # Coffee is drunk in the yellow house.
    s.group_same("coffee", "yellow")

    # The Igbo drinks palmwine.
    s.group_same("Igbo", "palmwine")

    # The yellow house is immediately to the right of the blue house.
    s.group_rightof("yellow", "blue")

    # The weed smoker owns snails.
    s.group_same("weed", "snails")

    # ectasy are taken in the yellow house.
    s.group_same("ectasy", "yellow")

    # Milk is drunk in the middle house.
    s.group_is("milk", 3)

    # The Japanese lives in the first house.
    s.group_is("Japanese", 1)

    # The man who sniffs white powder lives in the house next to the man
    # with the fox.
    s.group_nextto("white powder", "fox")

    # ectasy are smoked in the house next to the house where the horse is
    # kept.
    s.group_nextto("ectasy", "horse")

    # The weed smoker drinks orange juice.
    s.group_same("weed", "orange juice")

    # The Japanese smokes weed.
    s.group_same("Japanese", "weed")

    # The Japanese lives next to the blue house.
    s.group_nextto("Japanese", "blue")

    return s


def test_zebra():
    s = zebra_solver()
    solutions = s.solve()
    write_solutions(solutions)


if __name__ == "__main__":
    test_zebra()
