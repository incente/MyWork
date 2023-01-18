coffee_types = [
    {"name": "espresso", "price": 1, "water_usage": 50, "coffee_usage": 20, "milk_usage": 0},
    {"name": "cappuchino", "water_usage": 50, "coffee_usage": 20, "milk_usage": 50},
    {"name": "latte", "water_usage": 50, "coffee_usage": 20, "milk_usage": 70}
]

storage = [
    {"water": 500},
    {"coffee": 100},
    {"milk": 250}
]

def choose():   
    choice = input("What do you like? (espresso/cappuchino/latte)\n")
    
    return choice

def bill(price):

    while True:

        try:
            cash = int(input("Please insert:\n"))
            break

        except:
            print("Error just coins!")
    
    cash -= price
    print(f"Returned {cash}")

def usage(choice):

    coffee_list_num = 0

    if choice.lower() == "espresso":
        storage[0]["water"] -= coffee_types[coffee_list_num]["water_usage"]
        storage[1]["coffee"] -= coffee_types[coffee_list_num]["coffee_usage"]
        storage[2]["milk"] -= coffee_types[coffee_list_num]["milk_usage"]
        bill(coffee_types[coffee_list_num]["price"])

usage(choose())