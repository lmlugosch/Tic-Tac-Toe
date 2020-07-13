def update_player(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'


def new_board():
    board = []
    for row in range(3):
        board.append([])
        for column in range(3):
            board[row].append(' ')
    return board


def print_board(board):
    spacer = '---+---+---'
    for count, row in enumerate(board):
        print(' ' + ' | '.join(row))
        if count < (len(board)-1):
            print(spacer)
    print()


def next_move(player):
    move = input(f"{player}'s turn!\nEnter move: ")
    move = move.lower()
    print()
    row = {'a': 0, 'b': 1, 'c': 2}
    col = {'1': 0, '2': 1, '3': 2}
    x = row.get(move[0])
    y = col.get(move[1])
    return x, y


def check_move(move, board):
    if move[0] is None or move[1] is None:
        print('Invalid entry!', end = '\n\n')
        return False
    elif board[move[0]][move[1]] != ' ':
        print('That spot is already taken!', end = '\n\n')
        return False
    else:
        return True


def update_board(board, move, player):
    board[move[0]][move[1]] = player
    return board


def check_win(board):

    for row in board:
        for item in row:
            if item != row[0] or item == ' ':
                break
        return True

    transpose = list(zip(*board))
    for row in transpose:
        for item in row:
            if item != row[0] or item == ' ':
                break
        return True

    return False


def main_loop():
    board = new_board()
    turn = 0
    win = False
    print_board(board)

    while not win and turn < 9:
        player = update_player(turn)
        move = next_move(player)
        while not check_move(move, board):
            move = next_move(player)
        board = update_board(board, move, player)
        print_board(board)
        win = check_win(board)
        turn += 1

    if win:
        print(f'Game over! {player} wins!')
    else:
        print("Game over! Cat's game!")


main_loop()
