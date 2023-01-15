# SudokuSolver

A simple sudoku solver implemented using a backtracking algorithm.

# Usage

```
$ python main.py input.txt
Input:
0 3 0 0 0 7 6 0 0
1 7 5 8 0 6 0 0 4
9 0 0 0 0 0 0 1 7
0 4 3 0 8 9 7 0 0
0 0 0 0 0 0 0 0 0
0 0 2 3 7 0 5 9 0
2 9 0 0 0 0 0 0 5
5 0 0 2 0 1 9 6 3
0 0 4 9 0 0 0 7 0

Successfully solved!
Took 0.01 seconds.

Solution:
4 3 8 1 2 7 6 5 9
1 7 5 8 9 6 2 3 4
9 2 6 4 3 5 8 1 7
6 4 3 5 8 9 7 2 1
7 5 9 6 1 2 3 4 8
8 1 2 3 7 4 5 9 6
2 9 1 7 6 3 4 8 5
5 8 7 2 4 1 9 6 3
3 6 4 9 5 8 1 7 2
```

The input file shall use `-` for empty cells, use space as separator and use one line for each line
of the puzzle. Note that only 9x9 puzzles are supported.
