# insert wanted sudoku board
sudoku_board = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
                [0, 6, 2, 0, 5, 0, 0, 9, 0],
                [0, 7, 0, 0, 0, 8, 0, 0, 0],
                [0, 9, 0, 6, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 2, 0, 0, 0, 4],
                [0, 0, 8, 0, 0, 5, 0, 7, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [0, 2, 0, 0, 1, 0, 7, 5, 0],
                [3, 8, 0, 0, 7, 0, 0, 4, 2]]

# dictionary holding staring position of each box
box_positions = {1: [0, 0],
                 2: [0, 3],
                 3: [0, 6],
                 4: [3, 0],
                 5: [3, 3],
                 6: [3, 6],
                 7: [6, 0],
                 8: [6, 3],
                 9: [6, 6]}

# entire number of rows and columns
num_row = len(sudoku_board)
num_col = len(sudoku_board[0])


def print_board(board):
    # number of rows and columns inside one box
    num_row_box = num_row / 3
    num_col_box = num_col / 3

    # printing
    for row in range(num_row):
        if row % num_row_box == 0:
            print(" ══════   ══════  ══════ ")

        for col in range(num_col):
            if col % num_col_box == 0:
                print("║", end=" ")
            print(board[row][col], end=" ")
        print("║")
    print(" ══════   ══════  ══════ ")


def find_zero(board):
    zero_position = [None, None]

    for row in range(num_row):
        for col in range(num_col):
            if board[row][col] == 0:
                zero_position[0] = row
                zero_position[1] = col
                return zero_position
    return None


def is_valid(board, row, col, value):
    start_position = [0, 0]
    return_value = False

    if row < num_row and col < num_col:
        # check value inside columns
        for _row in range(num_row):
            if board[_row][col] == value:
                #print("There is already " + str(value) + " in the same column.")
                return_value = False

        # check value inside rows
        for _col in range(num_col):
            if board[row][_col] == value:
                #print("There is already " + str(value) + " in the same row.")
                return_value = False

        # check value inside box
        box = get_box_number(row, col)
        start_position = box_positions[box]

        _row = start_position[0]
        _col = start_position[1]

        for _row in range(_row, _row + 3):
            for _col in range(_col, _col + 3):
                if board[_row][_col] == value:
                    # print("There is already " + str(value) +
                    #      " in the " + str(box) + ". box.")
                    is_valid = False
                    return is_valid
            _col = start_position[1]
    else:
        print("Invalid number of cell.")
    return_value = True
    return return_value


def get_box_number(row, col):
    if row < 3:
        if col < 3:
            box = 1
        elif col < 6:
            box = 2
        else:
            box = 3
    elif row < 6:
        if col < 3:
            box = 4
        elif col < 6:
            box = 5
        else:
            box = 6
    else:
        if col < 3:
            box = 7
        elif col < 6:
            box = 8
        else:
            box = 9
    return box


# holding position of last zero value
last_zero_position = [0][0]


def solve_sudoku(board):
    zero_position = [0, 0]

    # no more zeros
    if find_zero(board) == None:
        return True
    # new zero value detected
    else:
        # zero value position
        zero_position = find_zero(board)

    # brut force mechanism
    for value in range(1, 10):
        if is_valid(board, zero_position[0], zero_position[1], value):
            board[zero_position[0]][zero_position[1]] = value

            if solve_sudoku(board):
                return True
            board[zero_position[0]][zero_position[1]] = 0

    return False


print("Sudoku board:")
print_board(sudoku_board)
solve_sudoku(sudoku_board)
print("Resolved:")
print_board(sudoku_board)
