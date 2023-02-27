menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 2.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 3.0
    }
}

profit = 0

ressources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

is_on = True

while is_on:
    user_input = input("What would you like? (espresso/cappuccino/latte): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        for n in ressources:
            print(f"{n}: {ressources[n]}")
        print(f"profit: {profit}$")
    elif user_input in ["espresso", "cappucino", "latte"]:
        print (user_input)
    else:
        print("ERROR Wrong input")