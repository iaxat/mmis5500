from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards

# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()

    def play_game(self):
        first_game = 0
        user_card_arr = []
        user_score = 0
        dealer_score = 0

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

        user_card = self.d.deck[0]
        print('1st Card:',user_card.face,'of',user_card.suit)
        user_card_arr.append(user_card)
        
        if first_game == 0:
            user_card = self.d.deck[1]
            print('2nd Card:',user_card.face,'of',user_card.suit)
            user_card_arr.append(user_card)
            first_game = 1
        else:
            pass
        
        

        while (continue_hit = input('Do you want to continue hit(y/n): ')) == 'y':
            for i in deck:
                user_card = self.d.deck[i+2]

        
        




play = PlayGame()
play.play_game()