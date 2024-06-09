
from random import randint


#----------------------------------------------

class card():
    def __init__(self, suit, number) -> None:
        self.suit = suit
        self.number = str(number)
        try:
            self.value = int(number)
        except ValueError:
            if self.number == 'A':
                self.value = 11
            else:
                self.value = 10

#----------------------------------------------

class deck():
    def __init__(self) -> None:
        self.cards = []

#-----------

    def add_card(self, card):
        self.cards.append(card)
        
#-----------

    def deal_card(self, hand):
        hand.add_card(self.cards.pop(randint(0, len(self.cards)-1)))

#-----------
    
    def display_hand(self) -> int:
        total = 0
        for card in self.cards:
            total += card.value
            print(f'{card.number} of {card.suit}')
        print(total)
        return(total)

#----------------------------------------------

class hand():
    def __init__(self, deck) -> None:
        self.deck = deck
        self.cards = []
        self.ace_count = 0
        self.total = 0
        self.converted_aces = 0

#-----------------

    def add_card(self, card):
        self.cards.append(card)
        if card.number == 'A':
            self. ace_count += 1
        self.total += card.value
        while self.total > 21 and self.ace_count > self.converted_aces:
            self.total -= 10
            self.converted_aces += 1

#-----------------

    def clear(self):
        return_cards = (self.cards)
        for card in self.cards:
            self.deck.add_card(card)
        self.cards = []
        self.ace_count = 0
        self.total = 0
        self.converted_aces = 0
        
#-----------------

    def display_hand(self) -> int:
        for card in self.cards:
            print(f'{card.number} of {card.suit}')
        print(f'Total: {self.total}\n')
        
        return(self.total)

#-----------------

    def display_dealer_hand(self) -> int:
        total = 0
        converted_aces  = 0
        for card in self.cards:
            total += card.value
            if self.cards.index(card) == 1:
                print('Face Down')
            else:
                print(f'{card.number} of {card.suit}')
        while total > 21 and self.ace_count > converted_aces:
            total -= 10
            converted_aces += 1
        return(total)
    
#-----------------------------------------------















