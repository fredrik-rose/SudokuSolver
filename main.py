"""
Program entry point.
"""
import time

import example as ex
import sudokusolver.sudokusolver as solver


def solve(sudoku, empty_cell_value):
    """
    Solves a sudoku puzzle.
    :param sudoku: Sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    """
    print("{}\n".format(sudoku))
    start = time.time()
    success = solver.solve(sudoku, empty_cell_value)
    end = time.time()
    if success:
        print("Successfully solved!")
    else:
        print("Could not solve!")
    print("Took {} seconds.\n".format(end - start))
    print("{}".format(sudoku))


def main():
    """
    Program entry point.
    """
    empty_cell_value = 0
    print("Easy sudoku puzzle:")
    solve(ex.easy(empty_cell_value), empty_cell_value)
    print("\nHard sudoku puzzle (this will take some time to solve):")
    solve(ex.hard(empty_cell_value), empty_cell_value)


if __name__ == "__main__":
    main()
