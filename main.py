import game



if __name__ == '__main__':

    live_game = game.game()
    live_game.start_game()
    play_again = 'y'
    while play_again == 'y':
        game_not_over = live_game.deal()
        while game_not_over:
            live_game.show_game()
            game_not_over = live_game.get_player_action()
        play_again = input('Would you like to play again?\n(y/n): ')
        print()



