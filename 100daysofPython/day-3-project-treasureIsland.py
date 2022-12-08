print("Welcome to treasure Island! Your mission is to find the treasure.")
l_or_r = input("You stand next to a crossroad, where are you going? L or R? ")
if l_or_r == "L":
    s_or_w = input("You stand next to a river. Do you swim over it or wait for a Boat. S or W? ")
    if s_or_w == "W":
        doors = input("You stand next to three doors. Which one do you choose? R, B or Y? ")
        if doors == "Y":
            print("Congrats you found the treasure!")
        else:
            print("Youre dead!")
    else:
        print("Youre dead!")
else:
    print("Youre dead!")