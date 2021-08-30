sudoku_board = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
                [0, 6, 2, 0, 5, 0, 0, 9, 0],
                [0, 7, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 6, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 2, 0, 0, 0, 4],
                [0, 0, 8, 0, 0, 5, 0, 7, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [0, 2, 0, 0, 1, 0, 7, 5, 0],
                [3, 8, 0, 0, 7, 0, 0, 4, 2]]


def print_board(board):
    # entire number of rows and columns
    num_row = len(board)
    num_col = len(board[0])

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
            print(board[row][col], end=" ")
        print("║")
    print(" ══════   ══════  ══════ ")


def solve_sudoku(board):
    solution = solve_sudoku_wrapper(board)
    return solution


def solve_sudoku_wrapper(board):
    solution = "Solution is not implemented."
    return solution


def find_zero(board):
    zero_position = [None, None]
    num_row = len(board)
    num_col = len(board[0])

    for row in range(num_row):
        for col in range(num_col):
            if board[row][col] == 0:
                zero_position[0] = row
                zero_position[1] = col
                return zero_position


print(find_zero(sudoku_board))
# print(zero_position)

# solution = solve_sudoku(board)
# print(solution)
