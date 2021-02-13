import random
import time
import timeit
import numpy as np



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



# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()


    # def deal_cards(self,deck):





    def play_game(self):
        print('')
        print('')
        print('\t\tStarting the game of BlackJack (21)')
        print('\t\tKindly do not waste all your money :-P')
        print('')
        print('\t\t\t\tInitial Deck without Shuffle')
        self.d.print_deck()
        print('')
        print('\t\t----------------------------------------')
        print('\t\t\t\tDeck to be shuffled')
        self.d.shuffle_deck()
        print('')
        print('\t\t\t\tDeck Shuffled')
        print('\t\t----------------------------------------')
        self.d.print_deck()
        print('')


play = PlayGame()
play.play_game()