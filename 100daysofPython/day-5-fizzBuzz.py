import random
#1. Fizzbuzz
output = 0
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        output = "FizzBuzz"
    elif n % 3 == 0:
        output = "Fizz"
    elif n % 5 == 0:
        output = "Buzz"
    else:
        output = n
    print(output)

#1.2 Password generator
all_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
all_symbols = ["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")", "_", "-", "+", "="]
all_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
digits = int(input("How many numbers would you like?\n"))

password_sort = ""

for n in range(0, letters):
    password_sort += all_letters[random.randint(0, len(all_letters) - 1)]

for n in range(0, symbols):
    password_sort += all_symbols[random.randint(0, len(all_symbols) - 1)]

for n in range(0, digits):
    password_sort += all_digits[random.randint(0, len(all_digits) - 1)]

password = ""
old_order = []
new_order = []

for n in range(0, len(password_sort) - 1):
    old_order.append(n)

print(old_order)

for n in range(0, len(password_sort)):
    rand = random.randint(0, len(old_order) - 1)
    print(rand)
    new_order.append(old_order[rand])
    old_order.pop(rand)

print(new_order)
