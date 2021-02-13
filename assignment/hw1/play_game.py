import random

from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards



# Class to play game
class PlayGame():
    def __init__(self):
        self.d = DeckOfCards()

    def play_again(self):
        play_again = 'y'
        while play_again == 'y':
            play = PlayGame()
            play.play_game()
            print('Thank you for Playing\n\n')
            play_again = input('Want to play again?(y/n):')

    def update_user_score(self, user_score, user_card_face):
        user_card_arr = []
        face_value_special = ['Jack', 'King', 'Queen']
        if user_card_face in face_value_special:
            user_score+=10
        elif user_card_face == 'Ace':
            user_score+=11
        else:
            user_score += int(user_card_face)
        print('User Score:',user_score)
        return user_score



    def if_wins(self,user_score,dealer_score):
        if user_score>21:
            print('User Loses, Dealer Wins')
            print('Dealer Score:', dealer_score)
            print('User Score:', user_score)
        elif dealer_score>21:
            print('Dealer Loses, User Wins')
            print('Dealer Score:', dealer_score)
            print('User Score:', user_score)
        elif user_score<=dealer_score:
            print('User Loses, Dealer Wins')
            print('Dealer Score:', dealer_score)
            print('User Score:', user_score)
        else:
            print('User Wins')
            print('Dealer Score:', dealer_score)
            print('User Score:', user_score)
            


    def play_game(self):
        dealer_score = random.randint(17,23)
        user_score = 0

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

        i = 0
        user_card = self.d.get_ith_card(i)
        print('1st Card:',user_card.face,'of',user_card.suit)
        user_score = self.update_user_score(user_score,user_card.face)
        

        i += 1
        user_card = self.d.get_ith_card(i)
        print('2nd Card:',user_card.face,'of',user_card.suit)
        user_score = self.update_user_score(user_score,user_card.face)
        

        i += 1
        while user_score<=21 and dealer_score<=21 and input('Do you want to continue hit(y/n): ') == 'y':
            dealer_score = random.randint(17,23)
            user_card = self.d.get_ith_card(i)
                
            print('Hit Card:',user_card.face,'of',user_card.suit)
            user_score = self.update_user_score(user_score,user_card.face)
            i+=1
        self.if_wins(user_score,dealer_score)


start_mission = PlayGame()
start_mission.play_again()