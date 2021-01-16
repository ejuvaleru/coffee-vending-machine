import data

QUARTER = .25
DIME = .10
NICKEL = .05
PENNY = .01

machine_money = 0
total_money = 0
change = 0

def ask_for_money():
    """
    Ask to the user for entering his money divided in Quarter, Dime, Nickel an Penny.
    Then the method returns the sum of all the types of coins.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return (QUARTER * quarters) + (DIME * dimes) + (NICKEL * nickels) + (PENNY * pennies)


def ask_for_coffee():
    return input("What would you like? (espresso/latte/cappuccino): ")

def serve_coffee(coffee_type):
    """
    The bussines logic of the coffee vending machine.
    """
    global machine_money
    total_money = ask_for_money()
    coffee_cost = data.MENU[coffe_type]['cost']
    if total_money < coffee_cost:
        return print("Sorry that's not enough money. Money refunded.")
    change = (total_money - coffee_cost)
    machine_money += coffee_cost
    print(data.resources)
    for coffe_resource in data.MENU[coffe_type]['ingredients']:
        for resource in data.resources: 
            if resource == coffe_resource:
                current_amount_ingredient = data.resources[resource]
                amount_ingredient_needed = data.MENU[coffe_type]['ingredients'][coffe_resource]
                if (current_amount_ingredient - amount_ingredient_needed) < 0:
                    print(f"Sorry, there is not enough {resource}.")
                    print(f"${total_money} refunded.")
                    machine_money -= coffee_cost
                    return 
                else:
                    data.resources[resource] = current_amount_ingredient - amount_ingredient_needed
    print(data.resources)
    print(f"Take your ☕ {coffe_type}, enjoy!")
    print(f"Here is your ${round(change, 2)} dollars in change.")


def process_coffee(coffee_type):
    """
    Process the entry from the user to filter the type of coffe correctly.
    Also can it be used by the mainteners. ;)
    """
    ingredient = ''
    if coffee_type == 'off': exit()
    elif coffee_type == 'report':
        print("-----Report-----")
        for resource in data.resources:
            if resource == 'coffe': print(f"{resource.title()}: {data.resources[resource]} g")
            print(f"{resource.title()}: {data.resources[resource]} ml")
        print(f"Money: ${machine_money}")  
    elif coffee_type == 'espresso': serve_coffee(coffee_type)
    elif coffee_type == 'latte': serve_coffee(coffee_type)
    elif coffee_type == 'cappuccino': serve_coffee(coffee_type)
    else:
        print("Option doesn't exist, please try again.")
        process_coffee(ask_for_coffee())

# Coffee vending machine is always on, except when the admin turn off
while True:
    process_coffee(ask_for_coffee())