col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []

p = True

turn = 1

def add(x, y):

    if x == 1:
        col0.append(y)

    elif x == 2:
        col1.append(y)
    
    elif x == 2:
        col2.append(y)
    
    elif x == 2:
        col3.append(y)
    
    elif x == 2:
        col4.append(y)
    
    elif x == 2:
        col5.append(y)
    
    else:
        col6.append(y)
    turn += 1



print("Wilkommen zu 4 gewinnt")
print("Plaziere deine Steine in den Spalten 1 - 7.")

while p:
    if turn % 2 != 0:
        x = input("Spieler 1 ist an der Reihe. Spalte: ")
        add(x, "X")

    else:
        x = input("Spieler 2 ist an der Reihe. Spalte: ")
        add(x, "O")

    if turn == 4:
        p = False


print(col0, col1, col2, col3, col4, col5, col6)
