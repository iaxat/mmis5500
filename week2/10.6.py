# Section 10.6

import random

class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    
class DeckOfCards():
    def __init__(self, deck=[]):
        self.deck = deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            print(card.face,'of',card.suit)


suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
faces = ['2','3','4','5','6','7','8','9','10','Jack','King','Queen','Ace']

cards = []
for suit in suits:
    for face in faces:
        cards.append(Card(suit,face))

# object
deck = DeckOfCards(cards)

deck.print_deck()

deck.shuffle_deck()
deck.print_deck()