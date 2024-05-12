#11/100 days of coding, Blackjack game

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### My Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def give_card():
    '''Returns a random card from cards[] '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = cards[random.randint(0, 12)]
    return new_card


# print(logo)
def blackjack():

    print("\033[H\033[J", end="")
    #starting point, cards both to user and cpu, also sum of cards
    user_cards = [give_card(), give_card()]
    cpu_cards = [give_card()]
    user_cards_sum = sum(user_cards)
    cpu_cards_sum = sum(cpu_cards)

    print(f"Your current hand is: {user_cards}, Sum of your cards is {user_cards_sum}")
    print(f"Dealer first card is: {cpu_cards[0]}")

    while user_cards_sum < 21 and input("Do you wish to draw another card?: y/n \n") == 'y':
        user_cards.append(give_card())  #adds another card to user
        user_cards_sum = sum(user_cards)
        if 11 in user_cards and user_cards_sum > 21:
          user_cards.remove(11)
          user_cards.append(1) 
          user_cards_sum = sum(user_cards)
        print(f"Your current hand is: {user_cards}")
        print(f"Sum of your card is {user_cards_sum}")

    while cpu_cards_sum < 17:
        cpu_cards.append(give_card())  #adds another card to cpu
        cpu_cards_sum = sum(cpu_cards)
        if 11 in cpu_cards and cpu_cards_sum > 21:
          cpu_cards.remove(11)
          cpu_cards.append(1)
          cpu_cards_sum = sum(cpu_cards)

    print(f"Your final hand is: {user_cards} , Sum of your cards is {user_cards_sum}")
    print(f"Cpu final hand is: {cpu_cards} , sum of cpu cards is: {cpu_cards_sum}")

  #result section
    if user_cards_sum > 21:
        print("You lose ! , you have more then 21")
    elif cpu_cards_sum > 21:
        print("You win ! ,cpu has more then 21")
    elif user_cards_sum == cpu_cards_sum:
        print("It's a draw !")
    elif user_cards_sum == 21:
      print("You win with a Blackjack")
    elif cpu_cards_sum == 21:
      print("Cpu win with a Blackjack")
    elif user_cards_sum > cpu_cards_sum:
        print("You win ! , you scored more points then the dealer")
    
    else:
        print("You lose ! , dealer scored more points then you")
      
    if input("Do you want to play black-jack ? 'n' to exit, any other key to play: ") == 'n':
        exit
    else:
        blackjack()

print(logo) #recurtion for the game
if input("Do you want to play black-jack ? 'n' to exit, any other key to play: ") == 'n':
    exit
else:
    blackjack()
