#1. Import
import random
import day_4_module

#1.1 Own module
print(day_4_module.pi)

#2. Random integer
random_integer = random.randint(1, 100)

#2.1 Random float 0 - 1
random_float = random.random()

#2.2 Random float 0-5
random_float_multi = random.random() * 5

#3. Lists (Data Structure)
new_list = ["hello", True, 6, 6.1234]
boolean = new_list[1]
new_list[1] = False
new_list.append("world")
new_list.extend(["Joe", "Mama"])
where_joe = new_list[-2]

#3.1 Treasure map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x = int(position[0]) - 1
y = int(position[1]) - 1
map[y][x] = "X"

print(f"{row1}\n{row2}\n{row3}")

#3.2 Rock, paper, scissors
player_input = int(input("Press 1 for Rock, 2 for Paper and 3 for Scissors. "))
cmp_list = ["Rock", "Paper", "Scissors"]

print(f"You choose: {cmp_list[player_input - 1]}")

cmp_random = random.randint(0, 2)
cmp_input = cmp_list[cmp_random]
print("Computer choose: " + cmp_input)

if player_input == 1:
    if cmp_input == "Rock":
        print("Its a draw!")
    elif cmp_input == "Paper":
        print("You lose!")
    else:
        print("You win!")

if player_input == 2:
    if cmp_input == "Paper":
        print("Its a draw!")
    elif cmp_input == "Scissors":
        print("You lose!")
    else:
        print("You win!")
        
if player_input == 3:
    if cmp_input == "Scissors":
        print("Its a draw!")
    elif cmp_input == "Rock":
        print("You lose!")
    else:
        print("You win!")