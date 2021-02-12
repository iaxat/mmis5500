# Zoom Class Session Week 2
# Monday
import sys

import 


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