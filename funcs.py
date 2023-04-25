import random

options= ('rock', 'paper','scissors')

def choose_player():
    option= input('Rock, paper or scissors?: ')
    option_lower= option.lower()
    print('Your option is', option_lower)
    return option_lower

def choose_computer():
    option_index= random.randint(0,2)
    computer_option= options[option_index]
    print('The computer option is', computer_option)
    return computer_option

def game(player, computer):

    if player == computer:
        print('You have tied this round!')

    elif player>computer:
        return True
    
    else:
        return False

def convert(player, computer):

    if player== options[0] and computer== options[2]:
        player_number= 3
        computer_number= 2

    elif player== options[2] and computer== options[0]:
        player_number= 2
        computer_number= 3

    else:
        player_number= convert2(player)
        computer_number= convert2(computer)

    return player_number, computer_number

def convert2(option):

    if option == options[0]:
        option_number= 0

    elif option == options[1]:
        option_number= 1

    else:
        option_number= 2

    return option_number