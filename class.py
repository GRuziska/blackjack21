#https://inventwithpython.com/bigbookpython/project4.html

from random import shuffle

class Card:
#
    def __init__(self, value, suit):
        self.suit = suit
        if value in 'JQK':
            self.value = '10'
        elif value in 'A':
            self.value = '11'
        else:
            self.value = value
#
    def get_rank(self):
        return self.value
    
    def get_suit(self):
        return self.suit
#    
    def __eq__(self, other_card: object):
        return self.value == other_card.value and self.suit == other_card.suit
    
    def __lt__(self, other_card):
        return self.value < other_card.value
    
    def __le__(self, other_card):
        return self.value <= other_card.value

    def __gt__(self, other_card):
        return self.value > other_card.value
    
    def __ge__(self, other_card):
        return self.value >= other_card.value
#
    def __repr__(self) -> str:
       return f'Card({self.value} {self.suit})'

    def __str__(self) -> str:
        return f'{self.value}{self.suit}'

class DeckCards:
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    values = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self):
        self.deck = list()
        for suit in DeckCards.suits:
            for value in DeckCards.values:
                self.deck.append(Card(value, suit))

    def shuffle_deck(self):
        shuffle(self.deck)

    def distribute_cards(self):
        return self.deck.pop()
    
    def __len__(self):
        return len(self.deck_52)
    
    def __eq__(self, other_deck):
        return self.deck_52 == other_deck.deck_52

    def __repr__(self):
        return f'Deck ({self.deck_52})'

    def __str__(self) -> str:
        pass
#
class Hand:
    def __init__(self, player_id):
        self.player_ID = player_id
        self.player_hand = list()

    def add_card(self, card):
        self.player_hand.append(card)

    def show_hand(self):
        print(self.player_ID, end=' ')
        for card in self.player_hand:
            print(card, end=' ')
        print()
    