from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

selection_menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
while True:
    choice = input(f"What would you like to have? ({selection_menu.get_items()}) ")
    if choice == "exit":
        break
    if choice == "report":
        coffee.report()
        money.report()
        continue
    menu_item = selection_menu.find_drink(choice)
    if menu_item:
        if coffee.is_resource_sufficient(menu_item):
            if money.make_payment(menu_item.cost):
                coffee.make_coffee(menu_item)
    else:
        print("Incorrect choice")
