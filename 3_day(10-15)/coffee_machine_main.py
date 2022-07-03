from coffee_machine_data import resources, MENU
resources["money"] = 0.0
for ingre in resources:
    resources[ingre] = float(resources[ingre])

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def cf_choose():
    cf = input("What would you like? (espresso/latte/cappuccino): ")
    return cf

# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
def secret_off():
    print("Exited")
    quit()

# TODO 3: Print report.
def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))

# TODO 4: Check resources sufficient?
def check_resoures(cf):
    if resources["water"] < float(MENU[f"{cf}"]["ingredients"]["water"]):
        print("Sorry there is not enough water.")
        return True
    elif resources["coffee"] < float(MENU[f"{cf}"]["ingredients"]["coffee"]):
        print("Sorry there is not enough coffee.")
        return True
    elif resources["milk"] < float(MENU[f"{cf}"]["ingredients"]["milk"]):
        print("Sorry there is not enough milk.")
        return True
    else:
        return True

# TODO 5: Process coins.
def coins():
    print("Please insert coins.")
    quaters = float(input("How many quaters?: "))
    dimes = float(input("How many dimes?: "))
    nickless = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    money_input = quaters*0.25 + dimes*0.1 + nickless*0.05 + pennies*0.01
    return money_input

# TODO 6: Check transaction successful?
def bill_check(money, coffee):
    if money >= float(MENU[f"{coffee}"]["cost"]):
        change = money - float(MENU[f"{coffee}"]["cost"])
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 7: Make Coffee.
def make_cf(cf):
    resources["water"] -= int(MENU[f"{cf}"]["ingredients"]["water"])
    resources["milk"] -= int(MENU[f"{cf}"]["ingredients"]["milk"])
    resources["coffee"] -= int(MENU[f"{cf}"]["ingredients"]["coffee"])
    resources["money"] += float(MENU[f"{cf}"]["cost"])

# TODO 8: Main
def main():
    run = True
    while run:
        cf = cf_choose()
        if cf == "off":
            secret_off()
        if cf == "report":
            report()
            cf = cf_choose()
        money_input = coins()
        run = bill_check(money_input, cf)
        run = check_resoures(cf)
        if run == True:
            make_cf(cf)


main()

