

from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards

# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()

    def deal_cards(self):
        print('Dealing Cards to User')
        self.user_score = 0
        self.dealer_score = 0
        self.user_cards = []

    def play_game(self):
        print('\n\n\t\tStarting the game of BlackJack (21)')
        print('\n\n\t\tKindly do not waste all your money :-P')
        print('')
        print('\n\n\t\t\t\tInitial Deck without Shuffle')
        self.d.print_deck()
        print('\n\t\t----------------------------------------')
        print('\t\t\t\tDeck to be shuffled')
        self.d.shuffle_deck()
        print('\n\t\t\t\tDeck Shuffled')
        print('\t\t----------------------------------------\n')
        self.d.print_deck()
        # print(self.d.get_deck_array())

play = PlayGame()
play.play_game()