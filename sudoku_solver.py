sudoku_board = [
    ["1", "2", "3", "1", "2", "3", "1", "2", "3"],
    ["4", "5", "6", "4", "5", "6", "4", "5", "6"],
    ["7", "8", "9", "7", "8", "9", "7", "8", "9"],
    ["1", "2", "3", "1", "2", "3", "1", "2", "3"],
    ["4", "5", "6", "4", "5", "6", "4", "5", "6"],
    ["7", "8", "9", "7", "8", "9", "7", "8", "9"],
    ["1", "2", "3", "1", "2", "3", "1", "2", "3"],
    ["4", "5", "6", "4", "5", "6", "4", "5", "6"],
    ["7", "8", "9", "7", "8", "9", "7", "8", "9"],
]


def print_sudoku_board(sudoku_board):
    # entire number of rows and columns
    num_row = len(sudoku_board)
    num_col = len(sudoku_board[0])

    # number of rows and columns inside one block
    num_row_block = num_row / 3
    num_col_block = num_col / 3

    # printing
    for row in range(num_row):
        if row % num_row_block == 0:
            print(" ══════   ══════  ══════ ")

        for col in range(num_col):
            if col % num_col_block == 0:
                print("║", end=" ")
            print(sudoku_board[row][col], end=" ")
        print("║")
    print(" ══════   ══════  ══════ ")


def solve_sudoku(sudoku_board):
    solution = solve_sudoku_wrapper(sudoku_board)
    return solution


def solve_sudoku_wrapper(sudoku_board):
    solution = "Solution is not implemented."
    return solution


print_sudoku_board(sudoku_board)

solution = solve_sudoku(sudoku_board)
print(solution)
