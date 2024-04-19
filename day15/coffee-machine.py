MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0
def is_sufficient(ingredient):
    for item in ingredient:
        if resources[item] < ingredient[item]:
            print("Sorry there is not enough water.")
            return False
    return True

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name},enjoy")

def coin_calculator():
    total = int(input("how many quarter?")) * 0.25
    total += int(input("how many dime?")) * 0.10
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many quarter?")) * 0.01
    return total


def transaction(payments, drink_cost):
    global profit
    if drink_cost <= payments:
        profit += drink_cost
        change = round(payments - drink_cost, 2)
        print(f"Here is {change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


process = True
while process:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        process = False
    elif choice == "report":
        print(f"water={resources['water']}ml\nmilk={resources['milk']}ml\ncoffee{resources['coffee']}"
              f"\nmoney=${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = coin_calculator()
            transaction(payment, drink["cost"])
            make_coffe(choice, drink["ingredients"])







