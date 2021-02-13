# Game function
# HW 1
#  Python MIS5500
# Blackjack

from assignment.hw1.DeckOfCards import DeckOfCards
import os
import sys
__import__ (DeckOfCards)



class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()


    # def deal_cards(self):


    def play_game(self):
        print('Starting the game of BlackJack (21)')
        print('Kindly do not waste all your money :-P')
        print('')
        print('Initial Deck without Shuffle')
        self.d.print_deck()
        print('----------------------------------------')
        print('Deck to be shuffled')





play = PlayGame()
print(play.play_game())