import card_classes
from time import sleep
import json


class game():
    
    def __init__(self) -> None:
        suits = ['spades', 'clubs', 'diamonds','hearts']
        numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.deck = card_classes.deck()
        self.dealer = card_classes.hand(self.deck)
        self.player_hand = card_classes.hand(self.deck)

        for suit in suits:
            for number in numbers:
                self.deck.add_card(card_classes.card(suit, number))

#--------------

    def start_game(self):

        self.player_id = input('Who is playing? ')

        try:
            with open('bank.json', 'r') as bank:
                player_dict = json.load(bank)
                if self.player_id in player_dict['accounts'].keys():
                    self.player_money = int(player_dict['accounts'][self.player_id])
                else:
                    self.player_money = 100

        except FileNotFoundError:
            with open('bank.json', 'w') as bank:
                new_json = {'accounts':{}}
                json.dump(new_json, bank)
            self.player_money = 100

#--------------

    def deal(self):

        print(f'{self.player_id} has {self.player_money}$')
        self.player_bet = int(input('How much would you like to bet? '))
        if self.player_bet > self.player_money:
            print(f'{self.player_id} only has {self.player_money}')
            return 0

        print()
        self.deck.deal_card(self.player_hand)
        self.deck.deal_card(self.dealer)
        self.deck.deal_card(self.player_hand)
        self.deck.deal_card(self.dealer)
        return 1

#---------------

    def show_game(self):

        print('Dealer:')
        self.dealer.display_dealer_hand()
        print()

        print('Player:')
        self.player_hand.display_hand()

#---------------

    def get_player_action(self):

        player_action = input('would you like to hit or stand?\n(h/s): ')

        if player_action == 'h':
            self.deck.deal_card(self.player_hand)

            if self.player_hand.total > 21:
                self.player_hand.display_hand()

                print('BUST! Sorry, you lose\n')
                self.player_money -= self.player_bet
                self.player_bet = 0
                self.update_account()
                self.dealer.clear()
                self.player_hand.clear()
                return 0
            
            return 1

        elif player_action == 's':
            self.finish_game()
            return 0
        else:
            print('invalid input -- please select \'h\' or \'s\'\n')
            return 1
        
 #-------------------

    def update_account(self):
        bank_dict = {}
        with open('bank.json', 'r+') as bank:
            bank_dict = json.load(bank)
        bank_dict['accounts'][self.player_id] = self.player_money
        with open('bank.json', 'r+') as bank:
            json.dump(bank_dict, bank)

#---------------

    def finish_game(self):

        player_total = self.player_hand.total

        self.player_hand.display_hand()
        print(f'Player stayed at {player_total}\n')

        
        while True:
            print('Dealer:')
            self.dealer.display_hand()

            sleep(1.5)
            dealer_total = self.dealer.total

            if dealer_total < 17:
                self.deck.deal_card(self.dealer)
                
                continue
            elif dealer_total > 21:
                print(f'Dealer BUST! - Everyone Wins\n')
                self.player_money += self.player_bet
                self.player_bet = 0
                break

            else:
                if player_total > dealer_total:
                    print(f'Player wins with {player_total}\n')
                    self.player_money += self.player_bet
                    self.player_bet = 0
                    break

                elif player_total < dealer_total:
                    print(f'Dealer wins with {dealer_total}\n')
                    self.player_money -= self.player_bet
                    self.player_bet = 0
                    break

                else:
                    print(f'Tie at {player_total}\nBet is pushed to next round\n')

                    break


        self.update_account()
        self.dealer.clear()
        self.player_hand.clear()
        print(f'new balance - {self.player_money}$\n')

#------------------------------------------------------------------------




        










