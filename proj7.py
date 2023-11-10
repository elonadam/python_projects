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

word_list = ["python", "baboon", "camel", "penguin", "zebra"]
lives = 6  #for letter guesses
not_dead = not_completed = True
chosen_word = random.choice(word_list)
blank_word = list(len(chosen_word) * '_')
print("Welcom to 'hang man' can you guess the name of the animal ?")
print(blank_word, stages[-1])

while not_dead and not_completed:
    count = 0
    guess_right = False  #true if at least one letter was guessed
    guess = input("Guess a letter:\n").lower()

    for letter in chosen_word:
        if letter == guess:
            blank_word[count] = guess
            guess_right = True
            print("Great! " + stages[lives])
        count += 1

    if not guess_right:
        lives -= 1
        print("\nWrong! try again " + stages[lives])

    print(blank_word, "\n")

    if '_' not in blank_word:
        print("you Won ! you saved him !")
        not_completed = False
    elif not lives:
        print("Oh no he died !")
        not_dead = False
