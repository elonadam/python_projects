#14/100 high low game based on Instagram figures, who has more followers in millions

import random
from replit import clear
from day14data import logo, vs, data

def switch(target_data,target_num,source_data,source_num):
    '''switch between the values of 2 elements that each contains
        data and num'''
    target_num = source_num
    target_data = source_data
    source_num, source_data = random_input()
    if target_data == source_data:
      source_num, source_data = random_input()
    return f"[{target_data}]", target_num, f"[{source_data}]", source_num

def random_input():
    '''give random personality data'''

    #get random data from dictionary
    rnd_dictionary = data[random.randint(0, len(data) - 1)]

    #extract the num of followers
    followers_str = rnd_dictionary['follower_count']
    
    # Create a new list excluding the second integer element
    values_list = list(rnd_dictionary.values())
    del values_list[1]

    # Convert the values to strings and join them into a single string
    values_string = ', '.join(map(str, values_list))
    return followers_str , f"[{values_string}]"  #return two values as a tuple


print(logo)

#initilaized data
followers_a, compare_a = random_input()
compare_a, followers_a, compare_b, followers_b = switch(compare_a, followers_a, compare_a, followers_a)

guess = True #if the player got the wrong set to false
score = 0
while guess:

  print(f"Compare A: {compare_a}")
  print(vs)
  print(f"Compare B: {compare_b}")

  user_guess = input("Who has more followers in Instagram ? type 'A' or 'B': ").lower()

  if user_guess == 'a' and followers_a > followers_b:
      clear()
      print("\n\nyou right !\n")
      score += 1
      
  elif user_guess == 'a':
      print("Wrong !")
      guess = False

  elif user_guess == 'b' and followers_b > followers_a:
      clear()
      print("\n\nyou right !\n")
      score += 1
    
  else:
      print("Wrong !")
      guess = False

  #switch between the values
  compare_a, followers_a, compare_b, followers_b = switch(compare_a, followers_a, compare_b, followers_b)

print(f"you scored: {score}") 
