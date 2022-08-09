from tkinter import OFF
from data import resources, MENU


# TODO: 4. Check resources sufficient?
def check_sufficient_ingredients(resource, drink):
    for ingredient in drink['ingredients']:

        if drink['ingredients'][ingredient] >= coffee_contents[ingredient]:
            print(f'Insufficient {ingredient}')
            return False
    return True


# TODO: 7. Make Coffee.
def make_coffee(resource, drink):

    for ingredient in drink['ingredients']:

        coffee_contents[ingredient] -= drink['ingredients'][ingredient]

        if ingredient == 'coffee':
            print(f"{ingredient}: {coffee_contents[ingredient]}g ")
        else:
            print(f"{ingredient}: {coffee_contents[ingredient]}ml ")


# TODO: 3. Print report.


def show_report():
    for item in coffee_contents:
        if item == 'coffee':
            print(f"{item.capitalize()}: {coffee_contents[item]}g")
        elif item == 'money':
            ''
        else:
            print(f"{item.capitalize()}: {coffee_contents[item]}ml")
    print(f"Money: ${coffee_contents['money']}")


# TODO: 5. Process coins.


def process_coins(drink):
    q = int(input("How many quarters?: ")) * 0.25
    d = int(input("How many dimes?: ")) * 0.10
    n = int(input("How many nickles?: ")) * 0.05
    p = int(input("How many pennies?: ")) * 0.01

    total_coins = round(q + d + n + p, 2)
    drink_cost = float(drink['cost'])
    print(f"Total Coins paid in: {total_coins}, Cost of drink: {drink_cost}")
    if drink_cost > total_coins:
        print(f"insufficient funds, refunding ${total_coins }")
        return False
    else:
        refund = round(total_coins - drink_cost, 2)
        print(f'Paid too much refunding ${refund}')
        coffee_contents['money'] += drink_cost
        return True


# TODO: 6. Check transaction successful?

coffee_on = True
coffee_contents = resources
while coffee_on == True:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    option = input("What would you like? (espresso/latte/cappuccino):")

    if option == 'report':
        show_report()
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.latte
    elif option == 'off':
        coffee_on = False
        print(f"You made ${coffee_contents['money']} today")
    else:
        chosen_drink = MENU[option]
        enough_ingredients = check_sufficient_ingredients(coffee_contents, chosen_drink)
        if enough_ingredients == True:
            correct_coins = process_coins(chosen_drink)

            if correct_coins == True:
                make_coffee(coffee_contents, chosen_drink)
                print(f"“Here is your {option}. Enjoy!”")
