

from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards

# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()

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
        user_card = self.d.deal_card(1)
        print(user_card.face,'of',user_card.suit)


play = PlayGame()
play.play_game()