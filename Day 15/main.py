


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
    "coffee": 100,
    "money": 0
}


def check_resources(t_of_coffee):
    chosen_coffee = MENU[t_of_coffee]["ingredients"]

    if resources['water'] < chosen_coffee['water']:
        print(f"Sorry!, there is not enough water to make {t_of_coffee}, only this amount of water left {resources['water']}")
    elif resources['milk'] < chosen_coffee.get('milk', 0):
        print(f"Sorry!, there is not enough milk to make {t_of_coffee}, only this amount of water left {resources['milk']}")
    elif resources['coffee'] < chosen_coffee['coffee']:
        print(f"Sorry!, there is not enough coffee to make {t_of_coffee}, only this amount of coffee left {resources['coffee']}")
    else:
        return True




def display_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def pay_bill(coffee, cost):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = (0.25*quarters) + (0.1*dimes) + (0.05*nickles) + (0.01 * pennies)
    if total < cost:
        print(f"Oops! You're a bit short. Coffee costs ${cost}, but you've got only {total}.")
        return False
    elif total == cost:
        print(f"Here is your {coffee} Enjoy!")
        return True
    elif total > cost:
        print(f"Great! Your coffee's brewing, and here's your change: ${round((total - cost), 2)}.\nHere is your {coffee} Enjoy! ")
        return True

def reduce_res(order):
    ingredients = MENU[order]['ingredients']
    money = MENU[order]['cost']
    milk = ingredients.get('milk', 0)
    water = ingredients['water']
    coffee = ingredients['coffee']


    resources['milk'] -= milk
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['money'] += money



# TODO: 1. print the report of coffee machine
while True:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if users_choice == "report":
        print(resources)
        display_report()
    elif users_choice in ['espresso' , 'latte', 'cappuccino']:
        cost_of_coffee = MENU[users_choice]['cost']
        if check_resources(users_choice):
           print(f"Time to feed the machine! It'll cost you ${cost_of_coffee}.")
           if pay_bill(users_choice,cost_of_coffee):
               reduce_res(users_choice)
               continue_using = input("Do you want to use the machine again? Type 'Y' or 'N'").lower()
               if continue_using != 'y':
                   exit()

