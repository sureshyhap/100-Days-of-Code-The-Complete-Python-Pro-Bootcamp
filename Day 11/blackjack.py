import art, random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_hand():
    hand = []
    for i in range(2):
        hand.append(random.choice(deck))
    return hand

def deal_card(hand):
    hand.append(random.choice(deck))

def check_busted(hand):
    if sum(hand) > 21:
        changed_hand = False
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                changed_hand = True
                break
        if changed_hand:
            return check_busted(hand)
        return True
    else:
        return False
    
def display_hands(player_hand, computer_hand):
    print(f"\tYour cards: {player_hand}, current score {sum(player_hand)}")
    print(f"\tComputer's first card: {computer_hand[0]}")

def print_end_game_state(player_hand, computer_hand):
    print(f"\tYour final hand: {player_hand}, final score {sum(player_hand)}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

def main():
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    while wants_to_play == 'y':
        game_over = False
        print(art.logo)
        player_hand = deal_hand()
        computer_hand = deal_hand()
        display_hands(player_hand, computer_hand)
        wants_to_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while wants_to_hit == 'y':
            deal_card(player_hand)
            if check_busted(player_hand):
                print_end_game_state(player_hand, computer_hand)
                print("You busted, Computer wins!")
                game_over = True
                break
            display_hands(player_hand, computer_hand)
            wants_to_hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if game_over:
            wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            continue
        player_sum = sum(player_hand)
        computer_sum = sum(computer_hand)
        while computer_sum < 17:
            deal_card(computer_hand)
            if check_busted(computer_hand):
                print_end_game_state(player_hand, computer_hand)            
                print("Opponent went over, You win!")
                game_over = True
                break
            computer_sum = sum(computer_hand)
        if game_over:
            wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            continue
        if computer_sum == player_sum:
            print_end_game_state(player_hand, computer_hand)
            print("It's a tie")
            game_over = True
            wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            continue
        elif computer_sum > player_sum:
            print_end_game_state(player_hand, computer_hand)
            print("Computer has higher hand, Computer wins!")
            game_over = True
            wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        else:
            print_end_game_state(player_hand, computer_hand)
            print("You have a higher hand, You win!")
            game_over = True
            wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if __name__ == "__main__":
    main()
