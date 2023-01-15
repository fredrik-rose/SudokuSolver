"""
Program entry point.
"""
import argparse
import pathlib
import time

import numpy as np

import sudokusolver.sudokusolver as solver


EMPTY_CELL_VALUE = 0


def parse_sudoku(file_path, empty_cell_value):
    """
    Parse a sudoku puzzle fro ma file.
    :param file_path: Path to file with the sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    """
    sudoku = []
    with open(file_path) as file:
        for line in file:
            line = line.rstrip().split(" ")
            sudoku.append([int(e) if e != "-" else 0 for e in line])
    return np.array(sudoku)


def print_sudoku(sudoku):
    """
    Print a sudoku puzzle.
    :param sudoku: Sudoku puzzle.
    """
    for line in sudoku:
        print(" ".join(str(e) for e in line))


def solve(sudoku, empty_cell_value):
    """
    Solve a sudoku puzzle.
    :param sudoku: Sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    """
    print("Input:")
    print_sudoku(sudoku)
    print("")
    start = time.time()
    success = solver.solve(sudoku, empty_cell_value)
    end = time.time()
    if success:
        print("Successfully solved!")
    else:
        print("Could not solve!")
    print("Took {:.2f} seconds.\n".format(end - start))
    print("Solution:")
    print_sudoku(sudoku)


def main():
    """
    Program entry point.
    """
    parser = argparse.ArgumentParser(description="A Sudoku puzzle solver.")
    parser.add_argument("input", type=pathlib.Path,
                        help="File with the puzzle to solve. Use - for empty cells and space as separator.")
    args = parser.parse_args()
    sudoku = parse_sudoku(args.input, EMPTY_CELL_VALUE)
    solve(sudoku, EMPTY_CELL_VALUE)


if __name__ == "__main__":
    main()
