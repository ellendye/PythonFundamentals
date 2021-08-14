from classes.deck import Deck
import random

bicycle = Deck()

player_one = []
player_two = []

game_start = input('HELLO Player 1! Are you ready to play war? ')

def play_hand():
    if len(player_one) < 1:
        print("PLAYER 2 IS THE WINNER!")
    if len(player_two) < 1: 
        print("PLAYER 1 IS THE WINNER!")
    print(f'Player one: {player_one[0]}')
    print(f'Player two: {player_two[0]}')
    if player_one[0].value > player_two[0].value:
        print("PLAYER ONE WINS HAND!")
        winner_card_one = player_one.pop(0)
        winner_card_two = player_two.pop(0)
        player_one.append(winner_card_one)
        player_one.append(winner_card_two)
    elif player_two[0].value > player_one[0].value:
        print("PLAYER TWO WINS HAND")
        winner_card_one = player_one.pop(0)
        winner_card_two = player_two.pop(0)
        player_two.append(winner_card_one)
        player_two.append(winner_card_two)
    else: 
        print("IT'S WAR!!")
        print("Each player, lay down your next three cards and flip over the third!")
        print(f'Player one: {player_one[0+3]}')
        print(f'Player two: {player_two[0+3]}')
        if player_one[0+3].value > player_two[0+3].value:
            print("PLAYER ONE GETS THE HAND!")
            player_one.pop(0)
            player_one.pop(0+1)
            player_one.pop(0+2)
            player_one.pop(0+3)
            player_two.pop(0)
            player_two.pop(0+1)
            player_two.pop(0+2)
            player_two.pop(0+3)
            player_one.append(player_one[0])
            player_one.append(player_two[0])
            player_one.append(player_one[0+1])
            player_one.append(player_two[0+1])
            player_one.append(player_one[0+2])
            player_one.append(player_two[0+2])
            player_one.append(player_one[0+3])
            player_one.append(player_two[0+3])
        elif player_two[0+3].value > player_two[0+3].value:
            print("PLAYER TWO GETS THE HAND!")
            player_one.pop(0)
            player_one.pop(0+1)
            player_one.pop(0+2)
            player_one.pop(0+3)
            player_two.pop(0)
            player_two.pop(0+1)
            player_two.pop(0+2)
            player_two.pop(0+3)
            player_two.append(player_one[0])
            player_two.append(player_two[0])
            player_two.append(player_one[0+1])
            player_two.append(player_two[0+1])
            player_two.append(player_one[0+2])
            player_two.append(player_two[0+2])
            player_two.append(player_one[0+3])
            player_two.append(player_two[0+3])
        else: 
            print("no one gets any cards because i'm lazy")
            player_one.pop(0)
            player_one.pop(0+1)
            player_one.pop(0+2)
            player_one.pop(0+3)
            player_two.pop(0)
            player_two.pop(0+1)
            player_two.pop(0+2)
            player_two.pop(0+3)
    return player_one, player_two

if game_start.lower() == 'yes':
    print("GAME ON")
    for i in range(26):
        player_one.append(bicycle.draw_card())
        player_two.append(bicycle.draw_card())
    print('Hands have been dealt')

    play = input('Are you ready? ')

    if play.lower() == 'yes':
        play_hand()
        losing_hand = player_one
        while 0 < len(losing_hand):
            input('\npress enter for the next hand!\n')
            play_hand()
            if len(player_one) > len(player_two):
                losing_hand = player_two
            else: 
                losing_hand = player_one
            print(f'1st person length {len(player_one)}, 2nd person length {len(player_two)}')
        print(f'{losing_hand} YOU LOSE!')


elif game_start.lower() == 'no':
    print("OK, maybe later.")








# from classes.deck import Deck
# import random

# bicycle = Deck()

# player_one = []
# player_two = []

# game_start = input('HELLO Player 1! Are you ready to play war? ')

# if game_start.lower() == 'yes':
#     print("GAME ON")
#     for i in range(26):
#         player_one.append(bicycle.draw_card())
#         player_two.append(bicycle.draw_card())
#     print(player_one)
#     print(player_two)
#     print('Hands have been dealt')
#     play = input('Are you ready? ')
#     if play.lower() == 'yes':
#         play_hand()
#     winning_hand = len(player_one)
#     for cards in range(winning_hand):
#         input('\nPress enter when you are ready to go\n')
#         if len(player_one) < 1:
#             print("PLAYER 2 IS THE WINNER!")
#         if len(player_two) < 1: 
#             print("PLAYER 1 IS THE WINNER!")
#         print(f'Player one: {player_one[cards]}')
#         print(f'Player two: {player_two[cards]}')
#         if player_one[cards].value > player_two[cards].value:
#             print("PLAYER ONE WINS HAND!")
#             winner_card_one = player_one.pop(cards)
#             winner_card_two = player_two.pop(cards)
#             player_one.append(winner_card_one)
#             player_one.append(winner_card_two)
#         elif player_two[cards].value > player_one[cards].value:
#             print("PLAYER TWO WINS HAND")
#             winner_card_one = player_one.pop(cards)
#             winner_card_two = player_two.pop(cards)
#             player_two.append(winner_card_one)
#             player_two.append(winner_card_two)
#         else: 
#             print("IT'S WAR!!")
#             print("Each player, lay down your next three cards and flip over the third!")
#             print(f'Player one: {player_one[cards+3]}')
#             print(f'Player two: {player_two[cards+3]}')
#             if player_one[cards+3].value > player_two[cards+3].value:
#                 print("PLAYER ONE GETS THE HAND!")
#                 player_one.pop(cards)
#                 player_one.pop(cards+1)
#                 player_one.pop(cards+2)
#                 player_one.pop(cards+3)
#                 player_two.pop(cards)
#                 player_two.pop(cards+1)
#                 player_two.pop(cards+2)
#                 player_two.pop(cards+3)
#                 player_one.append(player_one[cards])
#                 player_one.append(player_two[cards])
#                 player_one.append(player_one[cards+1])
#                 player_one.append(player_two[cards+1])
#                 player_one.append(player_one[cards+2])
#                 player_one.append(player_two[cards+2])
#                 player_one.append(player_one[cards+3])
#                 player_one.append(player_two[cards+3])
#             elif player_two[cards+3].value > player_two[cards+3].value:
#                 print("PLAYER TWO GETS THE HAND!")
#                 player_one.pop(cards)
#                 player_one.pop(cards+1)
#                 player_one.pop(cards+2)
#                 player_one.pop(cards+3)
#                 player_two.pop(cards)
#                 player_two.pop(cards+1)
#                 player_two.pop(cards+2)
#                 player_two.pop(cards+3)
#                 player_two.append(player_one[cards])
#                 player_two.append(player_two[cards])
#                 player_two.append(player_one[cards+1])
#                 player_two.append(player_two[cards+1])
#                 player_two.append(player_one[cards+2])
#                 player_two.append(player_two[cards+2])
#                 player_two.append(player_one[cards+3])
#                 player_two.append(player_two[cards+3])
#         if len(player_one) > len(player_two):
#             winning_hand = len(player_one)
#             print('am i in here')
#         else: 
#             winning_hand = len(player_two)
#             print('or am i in here?')
#         print(f'1 {len(player_one)} 2 {len(player_two)}')