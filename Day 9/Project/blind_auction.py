from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bidder_profiles = {}
more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidder_profiles[name] = bid;
  more_bidders_str = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if more_bidders_str == "yes":
    clear()
  if more_bidders_str == "no":
    more_bidders = False
max_bid = 0
max_bidder = ""
for bidder, bid in bidder_profiles.items():
  if bid > max_bid:
    max_bid = bid
    max_bidder = bidder
print(f"The winner is {max_bidder} with a bid of ${max_bid}.")