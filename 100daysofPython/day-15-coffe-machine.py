coffee_types = [
    {"name": "espresso", "price": 1, "water_ml": 50, "coffee_g": 20, "milk_ml": 0},
    {"name": "cappuccino", "price": 1.5, "water_ml": 50, "coffee_g": 20, "milk_ml": 50},
    {"name": "latte", "price": 1.5, "water_ml": 50, "coffee_g": 20, "milk_ml": 70}
]

storage = {"water_ml": 500, "coffee_g": 100, "milk_ml": 50}

def choose_coffee():
    while True:
        choice = input("Choose an coffee: (espresso/cappuccino/latte)\n")
        for coffee_type in coffee_types:
            if coffee_type["name"] == choice:
                return coffee_type
        print(f"ERROR Wrong input: [{choice}]")

def check_balance(coffee_type):
    name = coffee_type["name"]
    price = coffee_type["price"]
    balance_eur = 0.0
    while True:
        cash = input(f"Balance: {balance_eur}€. Price of {name}: {price}€. Please insert: (0.5/1/2). Stop (n)\n")
        if cash == "n":
            if balance_eur >= price:
                return balance_eur, coffee_type
        try:
            cash = float(cash)
            if cash in [0.5, 1.0, 2.0]:
                balance_eur += cash
            else: 
                print(f"ERROR Wrong Coin: [{cash}]")
        except ValueError:
            print(f"ERROR Wrong input: [{cash}]")

def check_storage(storage, balance_eur, coffee_type):
    storage_container = ["Water", "Coffee", "Milk"]
    storage_list = [storage["water_ml"], storage["coffee_g"], storage["milk_ml"]]
    usage_list = [coffee_type["water_ml"], coffee_type["coffee_g"], coffee_type["milk_ml"]]
    for n in range(len(storage_list)):
        if storage_list[n] < usage_list[n]:
            return False,storage_container[n], balance_eur, coffee_type
    for n in range(len(storage_list)):
        storage_list[n] -= usage_list[n]
    return True, None, balance_eur, coffee_type

def make_coffee(allowence, storage_container, balance_eur, coffee_type):
    name = coffee_type["name"]
    price = coffee_type["price"]
    if allowence == False:
        print(f"Sorry not enough {storage_container}")
        print(f"Returned: {balance_eur}")
    else: 
        change = balance_eur - price
        print(f"Here is your {name}")
        print(f"Returned: {change}")
        balance_eur = 0

            
make_coffee(*check_storage(storage, *check_balance(choose_coffee())))
            