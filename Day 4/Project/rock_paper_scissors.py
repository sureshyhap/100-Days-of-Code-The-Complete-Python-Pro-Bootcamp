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

#Write your code below this line 👇
hands = ["rock", "paper", "scissors"]
hands_displayed = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
player_hand = hands[player_choice]
player_hand_displayed = hands_displayed[player_choice]
  
computer_choice = random.randint(0, 2)
computer_hand = hands[computer_choice]
computer_hand_displayed = hands_displayed[computer_choice]

winner = None

if player_hand == "rock":
  if computer_hand == "rock":
    pass
  elif computer_hand == "paper":
    winner = "computer"
  elif computer_hand == "scissors":
    winner = "player"
elif player_hand == "paper":
  if computer_hand == "rock":
    winner = "player"
  elif computer_hand == "paper":
    pass
  elif computer_hand == "scissors":
    winner = "computer"
elif player_hand == "scissors":
  if computer_hand == "rock":
    winner = "computer"
  elif computer_hand == "paper":
    winner = "player"
  elif computer_hand == "scissors":
    pass

print(f"Player chose:\n{player_hand_displayed}")
print(f"Computer chose:\n{computer_hand_displayed}")

if winner == "player":
  print("You win!")
elif winner == "computer":
  print("You lose!")
elif not winner:
  print("Draw!")