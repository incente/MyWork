import random

def create_num():

    while True:

        try:
            range_min = int(input("Min: "))
            break

        except ValueError:
            print("Minimum must be an integer")
        
    while True:

        try:
            range_max = int(input("Max: "))
            break

        except ValueError:
            print("Maximum must be an integer")

    num = random.randint(range_min, range_max)
    print(num) #little hint
    return num, range_min, range_max

def guess(range_min, range_max):

    while True:

        guess_num = input("Guess a number, type 'give up' if you want to end: ")

        if guess_num == "give up":
            print("Goodbye")
            break
        else:
            try:
                guess_num = int(guess_num)

                if guess_num < range_min:
                    print(f"You guessed {guess_num}, thats below the min of {range_min}")
                elif guess_num > range_max:
                    print(f"You guessed {guess_num}, thats above the max of {range_max}")
                else:
                    return guess_num

            except ValueError:
                    print("Guess must be an integer")
        
def check(guess_num, num, range_min, range_max):
    counter = 1
    while True:
        if guess_num == num:
            print(f"You guessed {guess_num}, thats the right number. Total guesses: {counter}")
            again = input("Type 'yes' if you want to go again? ")
            if again.lower() == "yes":
                start()
            else:
                break
            
        else:
            print(f"You guessed {guess_num}, thats the wrong number. Guesses: {counter}")
            guess_num = guess(range_min, range_max)
            counter += 1
            
def start():
    num, range_min, range_max = create_num()
    check(guess(range_min, range_max), num, range_min, range_max)

start()