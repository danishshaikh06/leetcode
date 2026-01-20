'''37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

'''

def sudoku_solver(board, row=0, col=0):
    if row == 9:
        return True

    if col == 9:
        return sudoku_solver(board, row + 1, 0)

    if board[row][col] != '.':
        return sudoku_solver(board, row, col + 1)

    for dig in range(1, 10):
        if issafe(board, row, col, dig):
            board[row][col] = str(dig)
            if sudoku_solver(board, row, col + 1):
                return True
            board[row][col] = '.'

    return False


def issafe(self, board, col, row, dig):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(9):
        # check row, column, and box in one loop
        if board[row][i] == dig:
            return False
        if board[i][col] == dig:
            return False
        # box check: map i from 0-8 to 3x3 box
        r = start_row + i // 3
        c = start_col + i % 3
        if board[r][c] == dig:
            return False

    return True



