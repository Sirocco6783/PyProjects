from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Bad move. Try again.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ("X", "O"):
                print("Field already occupied. Try again.")
                continue
            board[row][col] = "O"
            break
        except ValueError:
            print("Not a number. Try again.")

def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ("X", "O"):
                free.append((r, c))
    return free

def victory_for(board, sign):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == sign:
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = "X"

board[1][1] = "X"

while True:
    display_board(board)
    enter_move(board)
    if victory_for(board, "O"):
        display_board(board)
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break
    draw_move(board)
    if victory_for(board, "X"):
        display_board(board)
        print("Computer won!")
        break
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break