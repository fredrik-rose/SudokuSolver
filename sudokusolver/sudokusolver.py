"""
Sudoku solver implemented using a backtracking algorithm.
"""
import numpy as np


def solve(sudoku: np.ndarray, empty_cell_value=0):
    """
    Solves a classic 9x9 sudoku puzzle.
    :param sudoku: Sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    :return: True if the Sudoku puzzle is successfully solved, false otherwise.
    """
    cell = find(sudoku, empty_cell_value)
    if cell is None:
        return True
    for value in range(1, 10):
        if valid(sudoku, cell, value):
            sudoku[cell] = value
            if solve(sudoku):
                return True
            sudoku[cell] = empty_cell_value
    return False


def find(array, value):
    """
    Finds the index of the first occurrence of a given value in the array.
    :param array: Array.
    :param value: Value.
    :return: Index of value, None if value is not found.
    """
    for index, element in np.ndenumerate(array):
        if element == value:
            return index
    return None


def valid(sudoku, cell, value, box_size=3):
    """
    Checks if a value is allowed to be placed in a given cell.
    :param sudoku: Sudoku puzzle.
    :param cell: Cell.
    :param value: Value.
    :param box_size: Sudoku box size.
    :return: True if value is allowed, false otherwise.
    """
    row = sudoku[cell[0], :]
    column = sudoku[:, cell[1]]
    box_cell = cell - np.mod(cell, box_size)
    box = sudoku[box_cell[0]:box_cell[0] + box_size, box_cell[1]:box_cell[1] + box_size]
    return value not in row and value not in column and value not in box
