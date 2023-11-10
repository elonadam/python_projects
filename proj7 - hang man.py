logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

import random

word_list = ["python", "baboon", "camel", "penguin","elephant", "lion", "tiger", "bear", "giraffe", "zebra", "monkey", "rabbit", "horse", "snake", "turtle", "penguin", "koala", "kangaroo", "dolphin", "shark"]
lives = 6  #for letter guesses
not_dead = not_completed = True
chosen_word = random.choice(word_list)
blank_word = list(len(chosen_word) * '_')
print(logo + "\nCan you guess the animal?")

while not_dead and not_completed:
    count = 0
    guess_right = False  #check if at least one letter was guessed
    guess = input("Guess a letter:\n").lower()
    if guess in blank_word:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if letter == guess:
            blank_word[count] = guess
            guess_right = True
            print("Great! " + stages[lives])
        count += 1

    if not guess_right:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life." + stages[lives])

    print(blank_word, "\n")

    if '_' not in blank_word:
        print("you Won ! you saved him !")
        not_completed = False
    elif not lives:
        print("Oh no he died ! the word was" , chosen_word)
        not_dead = False
