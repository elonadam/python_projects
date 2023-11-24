# day 16/ 100 , implementation of a coffee machine by object-oriented programming

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1 print report
# TODO 2 Check resources
# TODO 3 process coins|
# TODO 4 check transaction
# TODO 5 make coffee

my_money_machine = MoneyMachine()  # create object of class MoneyMachine
my_coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:

    options = menu.get_items()
    user_choice = input(f"What would you like? {options}")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        my_money_machine.report()  # its like car.speed()
        my_coffee_maker.report()
    else:
        coffee = menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(coffee):
            print(f"cost of {coffee.name} is: {coffee.cost}")
            if my_money_machine.make_payment(coffee.cost):
                my_coffee_maker.make_coffee(coffee)

