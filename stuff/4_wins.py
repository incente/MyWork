import os

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

os.system('cls')
print("Welcome to 4 gewinnt!")
player1 = input("Player 1 select a username: ")
player2 = input("Player 2 select a username: ")
while player2 == player1:
    player2 = input("Player 2, name is already taken. Select a new one: ")

def player_select(turn):
    if turn % 2 == 0:
        return player1
    else:
        return player2

def win(gameIcon):
    if gameIcon == "X":
        os.system('cls')
        print(f"{player1} wins!")
    elif gameIcon == "I":
        os.system('cls')
        print(f"{player2} wins!")

def check(gameIcon):
    for y in range(1, len(field) + 1):
        for x in range(0, 3):
            if field[y][x] == field[y][x+1] == field[y][x+2] == field[y][x+3] == gameIcon:
                win(gameIcon)
                print_field()
                return True

    for y in range(1, 5):
        for x in range(0, 6):
            if field[y][x] == field[y+1][x] == field[y+2][x] == field[y+3][x] == gameIcon:
                win(gameIcon)
                print_field()
                return True
    else:
        return False

def add(x, y):
    if pos[x] == 0:
        print("That column is full")
        start(player_select(turn))
        os.system('cls')
    else:
        pos[x] -= 1
        field[x][pos[x]] = y

def gameicon(player):
    if player == player1:
        return "X"
    else:
        return "I"

def start(player):
    print_field()
    col_nr = int(input(f"It is {player}'s turn. Select a column: "))
    if col_nr > 7:
        print("That aint no column. Only digits between 1 - 7 count.")
        start(player_select(turn))
    else:
        add(col_nr, gameicon(player))

print(f"{player1} your gameicon is {gameicon(player1)}")
print(f"{player2} your gameicon is {gameicon(player2)}")

while end_of_game == False:
    os.system('cls')
    start(player_select(turn))
    end_of_game = check(gameicon(player_select(turn)))
    turn += 1
