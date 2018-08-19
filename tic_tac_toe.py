import random


def display_board(board):
    """Print the board"""
    for row in range(0, 3):
        print(f"   |   |   \n {board[3*row + 1]} | {board[3*row + 2]} | {board[3*row + 3]} \n   |   |   ")

        if row < 2:
            print("-----------")


def player_input():
    """Ask player 1 which marker to play as"""
    marker_list = ['#', '', '']
    marker_list[1] = input("Player 1: Do you want to be X or O? ").upper()

    while marker_list[1] != 'X' and marker_list[1] != 'O':
        marker_list[1] = input("Please enter X or O: ").upper()

    marker_list[2] = 'X' if marker_list[1] == 'O' else 'O'
    return marker_list


def place_marker(board, mark, position):
    """Place the chosen marker on the board"""
    board[position] = mark


def win_check(board, mark):
    """Check if player with respective marker wins"""
    if board[1] == mark:
        if (board[2] == mark and board[3] == mark
                or board[4] == mark and board[7] == mark
                or board[5] == mark and board[9] == mark):
            return True
    if board[5] == mark:
        if (board[2] == mark and board[8] == mark
                or board[3] == mark and board[7] == mark
                or board[4] == mark and board[6] == mark):
            return True
    if board[9] == mark:
        if (board[3] == mark and board[6] == mark
                or board[7] == mark and board[8] == mark):
            return True

    return False


def choose_first():
    """Randomly choose who goes first"""
    return random.randint(1, 2)


def space_check(board, position):
    """Check if space is freely available"""
    return board[position] == ' '


def full_board_check(board):
    """Check if board is full"""
    for position in range(1, len(board)):
        if space_check(board, position):
            return False

    return True


def player_choice(board):
    """Ask for player's next position if available"""
    position = input("Choose your next position: (1-9) ")

    while True:
        try:
            position = int(position)

            if position not in range(1, 10):
                position = input("Please enter a number between 1 and 9: ")
            elif not space_check(board, position):
                position = input("That space is full. Try again: ")
            else:
                return position
        except ValueError:
            position = input("That is not an integer. Try again: ")


def replay():
    """Ask if players want to play again"""
    resp = input("Do you want to play again? Enter Yes or No: ").lower()

    while resp != "yes" and resp != "no":
        resp = input("Please enter Yes or No: ").lower()

    return resp == "yes"


print("Welcome to Tic Tac Toe!")

while True:
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    markers = player_input()
    marker = markers[0]

    while not win_check(game_board, marker) and not full_board_check(game_board):
        if marker == markers[0]:
            player = choose_first()
            print(f"Player {player} will go first.")
        elif marker == markers[1]:
            player = 2
        else:
            player = 1

        marker = markers[player]
        display_board(game_board)
        space = player_choice(game_board)
        place_marker(game_board, marker, space)

    display_board(game_board)

    if win_check(game_board, marker):
        print(f"Congratulations! Player {player} has won the game!")
    else:
        print("The game ended in a draw.")

    if not replay():
        break
