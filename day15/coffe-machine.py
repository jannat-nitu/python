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
        if ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}.")

def process_coin():
    print("please insert coin")
    total = int(input("how many quarters?\n")) * 0.25
    total += int(input("how many dimes?\n")) * 0.10
    total += int(input("how many nickels?\n")) * 0.05
    total += int(input("how many pennies?\n")) * 0.01
    return total


def is_transaction_successful(money_receive, drink_cost):
    global profit
    if payment >= drink["cost"]:
        back = round(money_receive - drink_cost, 2)
        profit = drink["cost"]
        print(f"Here is {back} dollars in change.")
        return True
    else:
        print("Sorry there is not enough.Money refunded")
        return False



process = False
while not process:
    choice = input("What would you like? espresso/latte/cappuccino): ")
    if choice == "off":
        process = True
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: "
              f"{profit}")

    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


