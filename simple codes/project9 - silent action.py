import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the silent action program.")
bids = {}

def highest_bid(bid_dictionary):
  max_bid = 0
  winner = ""
  for bid in bid_dictionary:
    bid_amount = bid_dictionary[bid]
    print(type(bid_amount))
    if bid_amount > max_bid:
      max_bid = bid_amount #host the amount of bid
      winner = bid #host the name
  print(f"The winner is {winner} with a bid of {max_bid}$")

while True:
    key = input("what is your name?: ")
    value = int(input("what's your bid?: $"))
    bids[key] = value
    more_keys = input("Are there any other bidders? Type yes or no: ").lower()
    
    if more_keys == 'no':
        break
    else:
        clear()
highest_bid(bids)
