end_of_game = False
turn = 0

pos = {
    1: 6,
    2: 6,
    3: 6,
    4: 6,
    5: 6,
    6: 6,
    7: 6
}

field = {
    1: ["O", "O", "O", "O", "O", "O"],
    2: ["O", "O", "O", "O", "O", "O"],
    3: ["O", "O", "O", "O", "O", "O"],
    4: ["O", "O", "O", "O", "O", "O"],
    5: ["O", "O", "O", "O", "O", "O"],
    6: ["O", "O", "O", "O", "O", "O"],
    7: ["O", "O", "O", "O", "O", "O"]
}

def print_field():
    print(field[1][0], field[2][0], field[3][0], field[4][0], field[5][0], field[6][0], field[7][0])
    print(field[1][1], field[2][1], field[3][1], field[4][1], field[5][1], field[6][1], field[7][1])
    print(field[1][2], field[2][2], field[3][2], field[4][2], field[5][2], field[6][2], field[7][2])
    print(field[1][3], field[2][3], field[3][3], field[4][3], field[5][3], field[6][3], field[7][3])
    print(field[1][4], field[2][4], field[3][4], field[4][4], field[5][4], field[6][4], field[7][4])
    print(field[1][5], field[2][5], field[3][5], field[4][5], field[5][5], field[6][5], field[7][5])

print("Welcome to 4 gewinnt!")
player1 = input("Player 1 select a username: ")
player2 = input("Player 2 select a username: ")

def player_select(turn):
    if turn % 2 == 0:
        return player1
    else:
        return player2



def add(x, y):
    if pos[x] == 0:
        print("That column is full")
        start(player_select(turn))
    else:
        pos[x] -= 1
        field[x][pos[x]] = y

def start(player):
    col_nr = int(input(f"It is {player}'s turn. Select a column: "))
    if player == player1:
        gameIcon = "X"
    else:
        gameIcon = "I"
    add(col_nr, gameIcon)




while end_of_game == False:
    start(player_select(turn))
    turn += 1
    print_field()

    if turn == 10:
        end_of_game = True