# #1. Calculator and docstring
# My try

# def run(a):
#     op = input("Pick a operator: " )
#     b = float(input("Give me the second number: "))
#     calc(a, op, b)

# def again(ans):
#     again = input("Do you want to calculate further? YES or NO? ")
#     if again.lower() == "yes":
#         run(ans)

# def calc(a, op, b):
#     """Calculates with two numbers and a operator""" #1.1 Docstring
#     if op == "+":
#         sum = a + b
#         print(f"{a} + {b} = {sum}")
#         again(sum)
#     elif op == "-":
#         dif = a - b
#         print(f"{a} - {b} = {dif}")
#         again(dif)
#     elif op == "*":
#         pro = a * b
#         print(f"{a} * {b} = {pro}")
#         again(pro)
#     elif op == "/":
#         quo = a / b
#         print(f"{a} / {b} = {quo}")
#         again(quo)

# a = float(input("Give me a number: "))
# run(a)

#2. Tried again but better

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calc():
    run = True

    a = float(input("Number: "))

    while run:

        op = input("Operation: ")
        b = float(input("Number: "))

        operation = operations[op]
        result = operation(a, b)
        
        print(f"{a} {op} {b} = {result}")

        con = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")

        if con.lower() == "y":
            a = result
        elif con.lower() == "n":
            run = False
            calc()

calc()