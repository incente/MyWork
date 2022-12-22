import random

celebs = [
    {"name": "Neymar da Silvia Santos, a footballplayer from Brasil", "followers": 198000000},
    {"name": "Kyle Jenner, a media personality and businesswoman from USA", "followers": 376000000},
    {"name": "Christiano Ronaldo, a footballplayer from Portugal", "followers": 521000000}
]

def choose(x):
    rand_celeb = random.choice(x)
    return rand_celeb

def game():

    a = choose(celebs)

    counter = 0

    while True:

        a_name = a["name"]

        while True:

            b = choose(celebs)
            if b != a:
                break
        
        b_name = b["name"]

        print(f"A: {a_name}")
        print(f"B: {b_name}")

        select = input("Who has more followers? Type 'A' or 'B': ")

        higher = a
        if b["followers"] > a["followers"]:
            higher = b
        
        if select.lower() == "a" and higher == a:
            counter += 1
            print(f"Right guess, current score: {counter}")
        elif select.lower() == "b" and higher == b:
            counter += 1
            print(f"Right guess, current score: {counter}")
            a = b
        else:
            print(f"Wrong guess, total end score: {counter}")
            break

game()