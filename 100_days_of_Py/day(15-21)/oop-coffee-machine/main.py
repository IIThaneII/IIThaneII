from unicodedata import name
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()
run = True
while run:
    order_name = input(f"What is your drink({menu.get_items()})? ")
    if order_name == "report":
        make_coffee.report()
        money.report()
    elif order_name == "off":
        run = False
    else:
        drink = menu.find_drink(order_name)
        if make_coffee.is_resource_sufficient(drink) == False:
            print("The resoures isn't sufficient!")
            continue
        else:
            accept = money.make_payment(drink.cost)
            if accept == False:
                continue
            else:
                make_coffee.make_coffee(drink)