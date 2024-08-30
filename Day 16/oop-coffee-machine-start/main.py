from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
espresso = MenuItem("espresso",50,0,18,1.5)
latte = MenuItem("latte",200,150,24,2.5)
cappuccino = MenuItem("cappuccino",250,100,24,3)
cf = CoffeeMaker()
do_payment = MoneyMachine()


is_on = True
while is_on:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if users_choice == "report":
        cf.report()
        do_payment.report()

    elif users_choice == "off":
        is_on = False

    elif users_choice in [espresso.name , latte.name, cappuccino.name]:
        drink = menu.find_drink(users_choice)
        if cf.is_resource_sufficient(drink):
           print(f"Time to feed the machine! It'll cost you ${drink.cost}.")
           if do_payment.make_payment(drink.cost):
               cf.make_coffee(drink)

        print("Nice try, but that’s not gonna work. Give it another shot!")
