#day 4/100 , rock paper scissors game with ascii-art

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves_list = ["rock", "paper","scissors"]
ascii_art = [rock,paper,scissors]

# print(ascii_art[0],ascii_art[1],ascii_art[2] + "\n Welcome to Rock, Paper, Scissors!")
print("\n Welcome to Rock, Paper, Scissors!")
cpu_choice = random.randint(0,2)
user_move = input("choose rock, paper, or scissors\n").lower()

if user_move in moves_list:
  user_choice = moves_list.index(user_move)
else:
  user_choice = 1
  print("Invalid choice, take the rock I just threw on you")

user_choice = ascii_art[user_choice]
cpu_res = ascii_art[cpu_choice]

if cpu_res == user_choice:
  print(cpu_res + "\n" + user_choice +"\n It\'s a tie !")
  
elif cpu_res == rock and user_choice == paper:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice +"\n User Won !")
  
elif cpu_res == rock and user_choice == scissors:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice +"\n Computer Won !")
  
elif cpu_res == scissors and user_choice == paper:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice+"\n Computer Won !")

elif cpu_res == paper and user_choice == scissors:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice+"\n User Won !")
  
elif cpu_res == scissors and user_choice == rock:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice+"\n User Won !")

# elif cpu_res == paper and user_choice == rock:
else:
     print("cpu choose:\n" +cpu_res + "\nuser choose" + user_choice+"\n Computer Won !")
