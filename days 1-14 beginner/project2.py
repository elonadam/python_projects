# Second project during 100 days of coding challenge, it's a tip calculator 

print("Welcome to the tip calculator !\n")
bill_amount = input("What is the total bill ?\n")
percentage = input(
    "How much tip do you want to add? choose a number between 10-20\n")
people_count = input("How many persons was dinning ?\n")
result = int(bill_amount) * (int(percentage) /100 + 1 ) / int(people_count)
print(f"The amount to pay for each person is: {round(result, 2)} !\n Have a nice day !")
