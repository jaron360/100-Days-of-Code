import random

print("Welcome to BlackJack!")

#list of cards to choose from
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards_random = random.sample(cards, 2)
random_card = random.sample(cards, 1)
#get the sum of 2 values which user started with

#ask the user if they want to play black jack
play_game = input("Do you want to play a game of BlackJack? Type 'yes' or 'no' ").lower()

while play_game == "yes":
    current_score = sum(user_cards_random)
    # print the current cards and sum of current cards to user
    print(f"Your Cards: {user_cards_random}. Current Score: {current_score}")
    while current_score <= 21:
        another_card = input("type 'y' to get another card and 'n' to pass ")
        if another_card == "y":
            pick_new_card = random.choice(cards)
            user_cards_random.append(pick_new_card)
            print(user_cards_random)
            current_score = sum(user_cards_random)
            print(f"Your Cards: {user_cards_random}. Current Score: {current_score}")
        else:
            print(f"your score is: {current_score}")
            exit()
    else:
        print("Game over, computer wins! Score went above 21.")
        exit()




