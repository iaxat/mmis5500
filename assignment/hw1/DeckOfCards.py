import random

class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        
class DeckOfCards():
    def __init__(self):
        self.deck = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        
        for suit in suits:
            for face in faces:
                self.deck.append(Card(suit, face))
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
