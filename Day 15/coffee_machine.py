import info

menu = info.MENU


def get_selection():
    """Gets a choice of menu item from the user. Valid choices include
       those displayed for 'report'."""
    return input("What would you like? (espresso, latte, cappuccino): ")


def display_resources(resources, money):
    """Displays remaining resources."""
    print(f"There is {resources['water']}mL of water left.")
    print(f"There is {resources['milk']}mL of milk left.")
    print(f"There is {resources['coffee']}g of coffee left.")
    print("${:.2f}".format(money))


def check_resources(choice, resources):
    """Checks if enough resources to dispense choice."""
    for ingredient, amount in menu[choice]["ingredients"].items():
        if resources[ingredient] < amount:
            return ingredient


def calculate_amount(coins):
    """Calculates the monetary value of a set of coins."""
    sum_money = 0
    for value, amount in coins.items():
        sum_money += (value * amount)
    return sum_money


def calculate_change(inserted_amount, cost):
    """Calculates change from inserted amount and cost of menu item."""
    return inserted_amount - cost


def handle_money_inserted(choice):
    """Handles money exchange for item."""
    cost = menu[choice]["cost"]
    remaining = cost
    total_inserted_money = 0
    while remaining > 0:
        if total_inserted_money > 0:
            print("Please insert at least ${:.2f} more.".format(remaining))
        print("Please insert coins.")
        coins = {}
        coins[0.25] = int(input("How many quarters?: "))
        coins[0.10] = int(input("How many dimes?: "))
        coins[0.05] = int(input("How many nickels?: "))
        coins[0.01] = int(input("How many pennies?: "))
        inserted_money = calculate_amount(coins)
        total_inserted_money += inserted_money
        remaining -= inserted_money
    change = calculate_change(total_inserted_money, cost)
    # net_amount should equal cost
    net_amount = total_inserted_money - change
    return net_amount, change


def dispense_item(choice, resources):
    """Removes ingredients from resources and gives the user the menu item."""
    net_received, change = handle_money_inserted(choice)
    for resource in resources:
        resources[resource] -= menu[choice]["ingredients"].get(resource, 0)
    print(f"Here is your {choice}!")
    if change > 0:
        print("Here is your change: ${:.2f}.".format(change))
    return net_received


def print_error(message):
    """Prints an error message."""
    print(message)


def parse_choice(choice, resources, money):
    """Analyzes choice of menu item."""
    if choice == "report":
        display_resources(resources, money)
    elif choice == "espresso" or \
        choice == "latte" or \
        choice == "cappuccino":
        missing = check_resources(choice, resources)
        if not missing:
            money_received = dispense_item(choice, resources)
            return money + money_received
        else:
            print_error(f"Not enough {missing}.")
    else:
        print_error("Incorrect choice.")
        exit(0)


def main():
    resources = info.resources
    money = 0
    should_continue = "yes"
    while should_continue == "yes":
        choice = get_selection()
        result = parse_choice(choice, resources, money)
        if result:
            money = result
        else:
            continue
        should_continue = input("Buy something else? 'yes' or 'no' ")
    print("Thank you come again.")


if __name__ == "__main__":
    main()
