import numpy as np

print("""
    Welcome to tic tac toe. The rules are simple you must get 3 in a row to win.\n
    Player 1 will be 'O' and player 2 will be 'X', in order to place a marker you
    can select from the following choices which are also displayed on the grid.\n
    TopLeft - TL    TopCenter - TC  TopRight - TR

    MiddleLeft - ML MiddleCenter - MC   MiddleRight - MR

    BottomLeft - BL BottomCenter - BC   BottomRight - BR

    Good luck!
""")

positions = np.array(
    [['TL', 'TC', 'TR'],
     ['ML', 'MC', 'MR'],
     ['BL', 'BC', 'BR']])

gameOn = True
turnCounter = 1
gameOutcome = ''


def create_playing_board():
    print('\n')
    print(f'{positions[0][0]}|{positions[0][1]}|{positions[0][2]}')
    print(f'{positions[1][0]}|{positions[1][1]}|{positions[1][2]}')
    print(f'{positions[2][0]}|{positions[2][1]}|{positions[2][2]}')
    print('\n')


def receive_input():
    text = 'Player 1 Please pick a position: ' if turnCounter % 2 != 0 \
        else 'Player 2 Please pick a position: '
    return input(text).upper()


def add_marker(position_to_change):
    if turnCounter % 2 != 0:
        positions[np.where(positions == position_to_change)] = 'O'
    else:
        positions[np.where(positions == position_to_change)] = 'X'


def validate_input(user_input):
    if not isinstance(user_input, str):
        print('You need to enter a string')
        return False
    elif user_input not in positions.ravel():
        print('Please pick a valid position')
        return False

    return True


def check_for_winner():
    # check rows
    for row in positions:
        if row[0] == row[1] and row[0] == row[2]:
            if turnCounter % 2 == 0:
                return 'player1'
            else:
                return 'player2'

    # check columns
    for row in np.transpose(positions):
        if row[0] == row[1] and row[0] == row[2]:
            if turnCounter % 2 == 0:
                return 'player1'
            else:
                return 'player2'

    # check diagonals
    if ((positions[0][0] == positions[1][1]) and (positions[0][0] == positions[2][2])) \
            or ((positions[0][2] == positions[1][1]) and (positions[0][2] == positions[2][0])):
        if turnCounter % 2 == 0:
            return 'player1'
        else:
            return 'player2'


def display_outcome(outcome):
    if outcome == 'draw':
        print('\nYou have drawn')
    elif outcome == 'player1':
        print('\nWinner: Player 1!!')
    elif outcome == 'player2':
        print('\nWinner: Player 2!!')
    create_playing_board()


while gameOn:

    create_playing_board()
    position = receive_input()
    if not validate_input(position):
        continue
    add_marker(position)
    turnCounter += 1
    winner = check_for_winner()
    if check_for_winner():
        gameOutcome = winner
        gameOn = False
        break

    if turnCounter == 10:
        gameOutcome = 'draw'
        gameOn = False
        break

display_outcome(gameOutcome)
