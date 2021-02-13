

from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards

# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()

    def play_game(self):
        initial_game = 0
        user_card_arr = []

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
        print('\n')

        user_card = self.d.deal_card(0)
        print('1st Card',user_card.face,'of',user_card.suit)
        user_card_arr.append(user_card)
        
        if initial_game == 0:
            user_card = self.d.deal_card(1)
            print('2nd Card',user_card.face,'of',user_card.suit)
            user_card_arr.append(user_card)

play = PlayGame()
play.play_game()