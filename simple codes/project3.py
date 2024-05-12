# no. 3 project, short "game" based on if\elif/else

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("you arived to the island and see there is two pathes one to the left and one to the right")
first_choice = input("which path you want to go ? choose left/right\n").lower()
if first_choice == "left":
  print("You walked into a den of wolves, GAME OVER")
elif first_choice == "right":
  print("Its now dark and you see a big cave infront of you and who knows whats inside")
  second_choice = input("Will you sleep in the cave or outside in the jungle ? choose cave/jungle\n").lower()
  if second_choice == "cave":
    print("A mighty bear was up for a mid-night snack, GAME OVER")
  elif second_choice == "jungle":
    print("You went to a walk this morning and saw a great castle with big 3 doors, red, yellow and black")
    third_choice = input("which door you choose to open ? choose red/yellow/black\n").lower()
    if third_choice == "red":
      print("you fell into endless hole in the ground GAME OVER")
    elif third_choice == "yellow":
      print("monkeys beat you to death GAME OVER")
    elif third_choice == "black":
      print("You have found the treasure !! YOU WIN")
    else:
      print("you typed wrong answer you DIED")
  else:
    print("you typed wrong answer you DIED")
else:
  print("you typed wrong answer you DIED")

