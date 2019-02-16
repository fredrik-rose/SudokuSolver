"""
Sudoku puzzle examples.
"""
import numpy as np


def easy(empty_cell_value):
    """
    An example of an easy sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    :return: Sudoku puzzle.
    """
    e = empty_cell_value
    return np.array(
        [[e, 3, e, e, e, 7, 6, e, e],
         [1, 7, 5, 8, e, 6, e, e, 4],
         [9, e, e, e, e, e, e, 1, 7],
         [e, 4, 3, e, 8, 9, 7, e, e],
         [e, e, e, e, e, e, e, e, e],
         [e, e, 2, 3, 7, e, 5, 9, e],
         [2, 9, e, e, e, e, e, e, 5],
         [5, e, e, 2, e, 1, 9, 6, 3],
         [e, e, 4, 9, e, e, e, 7, e]])


def hard(empty_cell_value):
    """
    An example of a hard (for a backtracking algorithm) sudoku puzzle.
    :param empty_cell_value: Value of an empty cell.
    :return: Sudoku puzzle.
    """
    e = empty_cell_value
    return np.array(
        [[e, 2, e, e, 3, e, e, 4, e],
         [6, e, e, e, e, e, e, e, 3],
         [e, e, 4, e, e, e, 5, e, e],
         [e, e, e, 8, e, 6, e, e, e],
         [8, e, e, e, 1, e, e, e, 6],
         [e, e, e, 7, e, 5, e, e, e],
         [e, e, 7, e, e, e, 6, e, e],
         [4, e, e, e, e, e, e, e, 8],
         [e, 3, e, e, 4, e, e, 2, e]])
