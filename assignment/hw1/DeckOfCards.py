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


class Get():
    def __init__(self) -> None:
        self.deck = DeckOfCards()

deckof = DeckOfCards()

get1 = Get()
print(get1)













# deck = DeckOfCards()
# print(deck)

# # Class to play game
# class Play_Game():
#     def __init__(self,deck) -> None:
#         self.deck = deck

#     def play_game(self):
#         # Creating a deck of cards
#         deck = DeckOfCards()

#         # shuffle the deck of cards


#         # 