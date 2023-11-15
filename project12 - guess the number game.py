#12 / 100 days ... guess the number simple game


logo = '''
   ____    _   _U _____ u____   ____          _____   _   _ U _____ u      _   _      _   _  __  __    ____ U _____ u  ____     
U /"___|U |"|u| \| ___"|/ __"| / __"| u      |_ " _| |'| |'|\| ___"|/     | \ |"|  U |"|u| U|' \/ '|U | __")\| ___"|U |  _"\ u  
\| |  _ /\| |\| ||  _|"<\___ \<\___ \/         | |  /| |_| |\|  _|"      <|  \| |>  \| |\| \| |\/| |/\|  _ \/|  _|"  \| |_) |/  
 | |_| |  | |_| || |___ u___) |u___) |        /| |\ U|  _  |u| |___      U| |\  |u   | |_| || |  | |  | |_) || |___   |  _ <    
  \____| <<\___/ |_____||____/>|____/>>      u |_|U  |_| |_| |_____|      |_| \_|   <<\___/ |_|  |_|  |____/ |_____|  |_| \_\   
  _)(|_ (__) )(  <<   >> )(  (__)(  (__)     _// \\_ //   \\ <<   >>      ||   \\,-(__) )( <<,-,,-.  _|| \\_ <<   >>  //   \\_  
 (__)__)    (__)(__) (__(__)   (__)         (__) (__(_") ("_(__) (__)     (_")  (_/    (__) (./  \.)(__) (__(__) (__)(__)  (__) 

'''
import random
#Number Guessing Game Objectives:
def binary_search(target_num, input_num):
  if target_num == input_num:
    print(f"You Win ! the number indeed was {target_num}")
    return True
  elif input_num > target_num:
    print("Too High !\nGuess again")
  else:
    print("Too Low !\nGuess again")  

    
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print (logo)

random_num = random.randint(0,100)
print(f"psssst the secreat num is {random_num}")
print("Welcome to the Number Guessing Game !")
print("I'm thinking about a number between 1-100 can you guess it ?")

if input("choose difficulty 'easy' or 'hard':  ") == 'easy':
  attempts = 10
else:
  attempts = 5

true_answer = False

while(attempts and not true_answer):
  attempts -= 1
  user_guess = int(input("Make a guess:  "))
  answer = binary_search(random_num, user_guess)
print("You lose !") 








