import random

def create_num():

    def create_min():
        try:
            min = int(input("Min: "))
            return min

        except ValueError:
            print("Minimum must be an integer")
            create_min()
        
    def create_max():
        try:
            max = int(input("Max: "))
            return max

        except ValueError:
            print("Maximum must be an integer")
            create_max()

    num = random.randint(create_min(), create_max())
    print(num)
    return num

def guess():
    while guess != create_num():
        guess = input("Guess: ")

def check(x, y):
    if x == y:
        print(f"You guessed {x}, thats the right number")