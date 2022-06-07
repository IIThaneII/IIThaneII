###############🚨 Blackjack Project 👇#####################

import blackjack_art
import random
import os
def clear(): return os.system('cls')

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    computer_hand = []

    def sum_of_list(l):
        total = 0
        for val in l:
            total = total + val
        return total

    def computer_cards():
        c_first_card = random.choice(cards)
        computer_hand.append(c_first_card)
        sum_of_list(computer_hand)
        while sum_of_list(computer_hand) < 17:
            new_card = random.choice(cards)
            if new_card == 11 and sum_of_list(computer_hand) < 11:
                computer_hand.append(new_card)
            elif new_card == 11 and sum_of_list(computer_hand) > 10:
                computer_hand.append(1)
            else:
                computer_hand.append(new_card)
        return c_first_card

    def player_first_hand():
        player_hand.append(random.choice(cards))
        new_card = random.choice(cards)
        if new_card == 11 and sum_of_list(player_hand) < 11:
            player_hand.append(new_card)
        elif new_card == 11 and sum_of_list(player_hand) > 10:
            player_hand.append(1)
        else:
            player_hand.append(new_card)

    def win_loose(a, b):
        if (a > 21 and b > 21) or (a == b):
            print("It's a draw!")
        elif (a <= 21 and a > b) or (a <= 21 and b > 21):
            print("You win!")
        else:
            print("You loose!")

    def main():
        player_first_hand()
        c_first_card = computer_cards()
        print(blackjack_art.logo)
        print("             Welcome to the blackjack game!".upper())
        print(f"Your cards: {player_hand}, current score: {sum_of_list(player_hand)}")
        print(f"Computer's first card: {c_first_card}")
        draw = True
        while draw:
            draw_card = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == "y" and sum_of_list(player_hand) < 22:
                player_hand.append(random.choice(cards))
                print(
                    f"Your cards: {player_hand}, current score: {sum_of_list(player_hand)}")
                print(f"Computer's first card: {c_first_card}")
                if sum_of_list(player_hand) > 21:
                    draw = False
            elif draw_card == "n" or sum_of_list(player_hand) > 21:
                draw = False
        print(f"Your cards: {player_hand}, current score: {sum_of_list(player_hand)}")
        print(f"Computer's final hand: {computer_hand}, final score: {sum_of_list(computer_hand)}")
        win_loose(sum_of_list(player_hand), sum_of_list(computer_hand))
    main()
