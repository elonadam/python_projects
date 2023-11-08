# 5/ 100 days of coding, Password Generator Project
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passw = []
final_pass = ""
for i in range (1,nr_letters + 1):
  passw.append(random.choice(letters))

for j in range (1, nr_numbers + 1):
  passw.append(random.choice(numbers))

for k in range (1, nr_symbols + 1):
  passw.append(random.choice(symbols))

random.shuffle(passw) #Order of characters randomised:

for i in range (0, len(passw)): #back to string
  final_pass += passw[i]
  
print(f"Your password is: " + final_pass)
