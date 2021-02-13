# This assignment is for MIS 5500 - Advance Python
# HW1 Blackjack

# import random is for the dealer's score which will be generated randomly 17 to 23
import random

# import in this section has been applied in a different method
# __init__.py has been created which can define as same folder as one module
from DeckOfCards import Card as Card
from DeckOfCards import DeckOfCards as DeckOfCards
# classes imported from the file DeckOfCards


# Class to play game
# the program starts here
class PlayGame:
    # this function is for initialization and making object for the class DeckOfClass
    # self makes usage available in all the files around the program
    def __init__(self):
        self.d = DeckOfCards()

    # this function will execute the program since the beginning
    # this will also ask the user for playing again
    def play_again(self):
        # play again value has been kept y such the loop works
        play_again = "y"
        while play_again == "y":
            # object creation of this class happens here
            play = PlayGame()
            # initiating the function from the object of this class happens here
            play.play_game()
            print("Thank you for Playing\n\n")
            # this section asks the user for playing again
            # if the user selects y then the while loop will check it and intiate the programs again
            # if the user selects n then the program will stop
            play_again = input("Want to play again?(y/n):")

    # this function has been created to update the user score as per the cards
    # this function updates the user score as per the special face cards
    def update_user_score(self, user_score, user_card_face):
        # face values like jack, king, queen and ace are defined in here
        face_value_special = ["Jack", "King", "Queen"]
        if user_card_face in face_value_special:
            # user card face value will check from the provided array for specific face
            user_score += 10
        elif user_card_face == "Ace":
            # since ace has a different value, it has been kept away
            user_score += 11
        else:
            # the last else is for face values which are all numbers
            # the user score is added for as per the face of the cards
            user_score += int(user_card_face)
        print("User Score:", user_score)
        return user_score
        # this function return the value of user score which can used in the function for comparison
        # matching with dealer score and putting out the value will be the work that happens because of the user score update

    # this function will check if user or dealer wins
    def if_wins(self, user_score, dealer_score):
        if user_score > 21:
            print("User Loses, Dealer Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        elif dealer_score > 21:
            print("Dealer Loses, User Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        elif user_score <= dealer_score:
            print("User Loses, Dealer Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        else:
            print("User Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)

    def play_game(self):
        dealer_score = random.randint(17, 23)
        user_score = 0

        print("\n\n\t\tStarting the game of BlackJack (21)")
        print("\n\n\t\tKindly do not waste all your money :-P")
        print("")
        print("\n\n\t\t\t\tInitial Deck without Shuffle")
        self.d.print_deck()
        print("\n\t\t----------------------------------------")
        print("\t\t\t\tDeck to be shuffled")
        self.d.shuffle_deck()
        print("\n\t\t\t\tDeck Shuffled")
        print("\t\t----------------------------------------\n")
        self.d.print_deck()
        print("\n")

        i = 0
        user_card = self.d.get_ith_card(i)
        print("1st Card:", user_card.face, "of", user_card.suit)
        user_score = self.update_user_score(user_score, user_card.face)

        i += 1
        user_card = self.d.get_ith_card(i)
        print("2nd Card:", user_card.face, "of", user_card.suit)
        user_score = self.update_user_score(user_score, user_card.face)

        i += 1
        while (
            user_score <= 21
            and dealer_score <= 21
            and input("Do you want to continue hit(y/n): ") == "y"
        ):
            dealer_score = random.randint(17, 23)
            user_card = self.d.get_ith_card(i)

            print("Hit Card:", user_card.face, "of", user_card.suit)
            user_score = self.update_user_score(user_score, user_card.face)
            i += 1
        self.if_wins(user_score, dealer_score)


start_mission = PlayGame()
start_mission.play_again()
