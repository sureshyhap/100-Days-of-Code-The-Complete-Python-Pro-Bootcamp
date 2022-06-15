import art, game_data, random

def choose_random(data):
  """Chooses a random element from the data."""
  return random.choice(data)

def print_data(profile):
  """Prints a formatted string based on the input profile dictionary."""
  print(f'{profile["name"]}, a {profile["description"]}, from {profile["country"]}.')

is_correct = True
score = 0
profile_b = None
while is_correct:
  print(art.logo)
  if is_correct and score > 0:
    print(f"You're right! Current score : {score}")
  print("Compare A: ", end="")
  if profile_b:
    profile_a = profile_b
  else:
    profile_a = choose_random(game_data.data)
  print_data(profile_a)
  print(art.vs)
  print("Against B: ", end="")
  profile_b = choose_random(game_data.data)
  while profile_a == profile_b:
    profile_b = choose_random(data)  
  print_data(profile_b)
  
  choice = input("Who has more followers? Type 'A' or 'B'").upper()
  if choice == "A" and profile_a["follower_count"] >= profile_b["follower_count"]:
    is_correct = True
    score += 1
  elif choice == "B" and profile_b["follower_count"] >= profile_a["follower_count"]:
    is_correct = True
    score += 1
  else:
    is_correct = False
    print(f"Sorry, that's wrong. Final score: {score}")