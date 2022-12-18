import os

#1. Print dictionary key and value

abc = {
    1: "Aa",
    2: "Bb",
    3: "Cc"
}

for key in abc:
    print(key, abc[key])

#2. Blind auction

bidders = []

def new_bidder():
    name = input("Whats your Name? ")
    bid = int(input(f"Welcome to the auction {name}, whats your bid? $"))
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    bidders.append(new_bidder)
    another_One()

def winner():
    highest = 0
    winner = ""
    for n in range(0, len(bidders)):
        new_bid = bidders[n]["bid"]
        bidder = bidders[n]["name"]
        if new_bid > highest:
            highest = new_bid
            winner = bidder
    print(f"Congrats, the winner is {winner} with ${highest}")

def another_One():
    another = input("Is there a nother bidder? YES or NO? ")
    if another.lower() == "yes":
        os.system('cls')
        new_bidder()
    elif another.lower() == "no":
        os.system('cls')
        winner()
    else:
        print("ERROR 364 only possible input: YES or NO")
        another_One()

print("Blind auction")
new_bidder()



