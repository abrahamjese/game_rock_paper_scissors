import os
import funcs as f

def main():

    rounds_player=0
    rounds_computer= 0
    rounds= 1

    while rounds_player<2 and rounds_computer<2:
        print('MARCADOR:')
        print('Player:', rounds_player,'Computer:', rounds_computer)
        print('ROUND', rounds ,'!:')
        player_option= f.choose_player()
        computer_option= f.choose_computer()
        player, computer= f.convert(player_option, computer_option)
        round= f.game(player, computer)

        if round== True:
            rounds_player+=1
            print('You win this round!')

        elif round== False:
            rounds_computer+=1
            print('Computer wins this round!')

        rounds+=1
        cont =input('Press any key to continue...')
        os.system('clear')
    
    if rounds_player==2:
        print('You win the game!...')
    else:
        print('Computer wins the game!...')


if __name__== '__main__':
    main()
