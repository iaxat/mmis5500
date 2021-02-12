# Section 10.6

import random

class Card():
    def __init__(self, suit, face) -> None:
        self.suit = suit
        self.face = face

    
class DeckOfCards():
    def __init__(self, deck) -> None:
        self.deck = deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            print(card.face,'of',card.suit)


