#1. Functions with parameters

def greet(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet(location="bergheim", name="vincente")

#2. Caeser Ciper

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encode(s, shift):
    li = []
    newli = []
    for letter in s.lower():
        li.append(letter)
    for letter in li:
        count = 0
        for n in abc:
            count += 1
            if n == letter:
                newIndex = count + shift - 1
                if newIndex > 26:
                    newIndex -= 26
                    newli.append(abc[newIndex])
                else:
                    newli.append(abc[newIndex])
    print(f'Your encoded word is {"".join(newli)}')

def decode(s, shift):
    li = []
    newli = []
    for letter in s:
        li.append(letter)
    for letter in li:
        count = 0
        for n in abc:
            count += 1
            if n == letter:
                newIndex = count - shift - 1
                if newIndex < 0:
                    newIndex += 26
                    newli.append(abc[newIndex])
                else:
                    newli.append(abc[newIndex])
    print(f'Your decoded word is {"".join(newli)}')

def startagain():
    startagain = input("Do you want to start again? Yes or No? ")
    if startagain.lower() == "yes":
        start()

def start():
    enorde = input("Do you want to encode or decode?" )
    if enorde == "encode":
        word = input("What message do you want to encode? (without spaces) ")
        shift = int(input("Shift number? "))
        encode(word, shift)
        startagain()
    elif enorde == "decode":
        word = input("What message do you want to decode? (without spaces) ")
        shift = int(input("Shift number? "))
        decode(word, shift)
        startagain()

start()