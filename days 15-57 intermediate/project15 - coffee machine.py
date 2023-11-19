# 15/100 days of coding, coffee machine script 

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
            "coffee": 24,
            "milk": 150,

        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,

        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0,
}


def money_bot(coffee_data):
    """responsible to deal with the money issues"""
    price = coffee_data["cost"]  # Extract the price good, to check the type
    print(f"The price of {user_choice} is ${price}")
    print("Please insert coins.")

    # get user input for coins
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many quarters?"))
    pennies = int(input("How many pennies?"))

    # calculate the total amount and change
    total_amount = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters
    change = round(total_amount - price, 2)

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    else:
        resources["money"] += price  # Add money to machine's resources
        return change


def stats(coffee_data):
    """Update resources after making a coffee"""
    used_ingredients = coffee_data['ingredients']
    for ingredient, amount in used_ingredients.items():
        resources[ingredient] -= amount


def report(curr_resources):
    """Print a report of current resources"""
    print("Current Resources:")
    for resource, amount in curr_resources.items():
        if resource == 'money':
            print(f"{resource.capitalize()}: ${amount}")
        else:
            print(f"{resource.capitalize()}: {amount}{'ml' if 'milk' in str(resource) else 'g'}")

while True:
    user_choice = input("What would you like to drink? (espresso / latte / cappuccino): ").lower()
    if user_choice == 'off':  # shut down the machine
        break

    if user_choice == 'report':
        report(resources)
        continue

    if user_choice not in MENU:
        print("Invalid choice. Please select a valid option.")
        continue

    coffee_type = MENU[user_choice]
    enough_ingredients = True

    # check if there is enough resources
    for ingredient, amount in coffee_type['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry not enough {ingredient} to make {user_choice}.")
            enough_ingredients = False
    if not enough_ingredients or (change := money_bot(coffee_type)) == -1:  # transaction failed duo money or resources
        continue  # This will lead to a new loop
    else:
        stats(coffee_type)
        print(f"Here is ${change} in change.")
        print(f"here is your {user_choice}. Enjoy!")


