# having a game field w by h
# having a turn by turn loop
# detect if there has been a 4 in a row, either vertical, horizontal or diagonal

import random

def initialize(w, h):
    return([[0]*w]*h)

def pretty_print(board_array):
    for y in board_array:
        for x in y:
            print(f'{x}   ', end="")
        print("\n", end="")

def transpose(board_array):
    new_board = []
    for i in range(0, len(board_array[0])):
        col = []
        for y in board_array:
            col.append(y[i])
        new_board.append(col)
    return(new_board)

def insert(board_array, x, player):
    t = transpose(board_array)
    t[x].reverse()
    for i in range(0, len(t[x])):
        if(t[x][i] == 0):
            t[x][i] = player
            break
        else:
            continue
    t[x].reverse()
    return transpose(t)

def turn(player):
    return 1 if player == 2 else 2

def check_horizontal(board):
    players = [1, 2]
    for player in players:
        for y in board:
            count = 0
            for x in y:
                if x == player:
                    count = count + 1
                else:
                    count = 0
            if count == 4:
                print("in row ", str(y))
                return player
    return 0

def check_vertical(board):
    return check_horizontal(transpose(board))

# simulates a play between two players,
def play(board_array, player_turn=1, steps=50):
    if steps < 0:
        return 0
    else:
        xlen = len(board_array[0])
        new_board = insert(board_array,\
                           random.choice(range(xlen)),\
                           player_turn)
        pretty_print(new_board)

        # check winner
        winw = check_horizontal(new_board)
        if winw > 0:
            print("horizontal winner")
            return winw
        winh = check_vertical(new_board)
        if winh > 0:
            print("vertical winner")
            return winh

        print("---")
        return play(new_board, turn(player_turn), steps - 1)

print(play(initialize(5, 5)))
