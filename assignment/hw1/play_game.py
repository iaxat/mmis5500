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
    # this function will take 2 parameters, user score and the dealer score
    def if_wins(self, user_score, dealer_score):
        if user_score > 21:
            # the condition when user exceeds the value of 21
            print("User Loses, Dealer Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        elif dealer_score > 21:
            # the condition when dealer score is more than 21
            print("Dealer Loses, User Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        elif user_score <= dealer_score:
            # the condition when user is equal or less than dealer
            print("User Loses, Dealer Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)
        else:
            # in any other case the user will win
            print("User Wins")
            print("Dealer Score:", dealer_score)
            print("User Score:", user_score)

    # this is the main function of this program which has all the application
    # in this function all the other functions will be used
    def play_game(self):
        # dealer score is generated here as random rumber from 17 to 23
        dealer_score = random.randint(17, 23)
        user_score = 0
        # user score is initialized here as 0 which will be later on used in the user score update function

        print("\n\n\t\tStarting the game of BlackJack (21)")
        print("\n\n\t\tKindly do not waste all your money :-P")
        print("")
        print("\n\n\t\t\t\tInitial Deck without Shuffle")
        self.d.print_deck()
        # this function is derived from the object of the class DeckOfCards
        # this function will use the function to print the deck of cards from the object
        # this will print the card deck without shuffle
        print("\n\t\t----------------------------------------")
        print("\t\t\t\tDeck to be shuffled")
        self.d.shuffle_deck()
        # this function will shuffle the deck of cards
        # this function has been derived from the class DeckOfCards
        # the object d is used to access all these function
        # import allows these functions to be used here
        print("\n\t\t\t\tDeck Shuffled")
        print("\t\t----------------------------------------\n")
        self.d.print_deck()
        # this function will allow the program to print the deck after shuffle
        # will show that the deck has been shuffled properly
        # different arrangements and order is expected after using shuffle
        print("\n")

        # i is used for the index of the deck of cards that would be access for giving it to user
        # i is initialized with 0 such the 1st index value can be selected
        i = 0
        # usercard here is the variable that will store the value of the function getithcard
        # self.d.get here is used as a getter function
        # without using a getter we can access value but to keep in mind if the value name changes
        # getter function extracts the value from the object of DeckOfCards class and is stored in user_card
        user_card = self.d.get_ith_card(i)
        # this will print the value of the face and suit of the cards in the terminal for the user to see
        print("1st Card:", user_card.face, "of", user_card.suit)
        # the print function here provides the print to terminal for the face and suit user got
        # this function here will print the 1st card that it given to the user when the game starts
        user_score = self.update_user_score(user_score, user_card.face)
        # this variable user score is initialized with 0
        # here the user score is updated
        # the function update_user_score is used such that the card face can be used for updating the user score
        # the parameter user score as 0 is also provided to function to initialize the value

        # i is used for the index of the deck of cards that would be access for giving it to user
        # i is added with 1 as the 2nd card is given to user such the 2nd index value can be selected
        i += 1
        # usercard here is the variable that will store the value of the function getithcard
        # self.d.get here is used as a getter function
        # without using a getter we can access value but to keep in mind if the value name changes
        # getter function extracts the value from the object of DeckOfCards class and is stored in user_card
        user_card = self.d.get_ith_card(i)
        # this will print the value of the face and suit of the cards in the terminal for the user to see
        print("2nd Card:", user_card.face, "of", user_card.suit)
        # the print function here provides the print to terminal for the face and suit user got
        # this function here will print the 2nd card that it given to the user when the game starts
        user_score = self.update_user_score(user_score, user_card.face)
        # this variable user score is initialized with 0
        # here the user score is updated
        # the function update_user_score is used such that the card face can be used for updating the user score
        # the parameter user score as 0 is also provided to function to initialize the value

        # i is used for the index of the deck of cards that would be access for giving it to user
        # i is added with 1 as the 2nd card is given to user such the while loop can go on with the 3rd position
        # this i is very important as it makes the while loop run accurate
        # this i+=1 will put the index on 3rd position and provide user to select option for a hit
        i += 1
        # the while here will check for the conditions to satisfy for the continue hit situation
        # while loop here will check if scores are within boundaries to ask for another hit
        while (
            user_score <= 21
            and dealer_score <= 21
            and input("Do you want to continue hit(y/n): ") == "y"
        ):
            # dealer score here is randomized with each while loop
            # dealer score has been randomized initially as well
            # dealer score has been randomized here cuz the user is getting chance to change value so should the dealer
            dealer_score = random.randint(17, 23)
            user_card = self.d.get_ith_card(i)
            # this user_card here is used to get the new hit for the user when the user selects y
            # this new card will be displayed in the terminal
            # this print shows the new card user got on going for a hit
            print("Hit Card:", user_card.face, "of", user_card.suit)
            # this user_score is used for updating the user score on getting a new hit
            # update function for user score is called here with the intialized value and the card face
            user_score = self.update_user_score(user_score, user_card.face)
            # user score update is necessary as the while loop has conditions to check score after each card user gets
            # i here is used for moving to a new index
            # i will be in the end such that the index is moved only after all the function are performed well
            i += 1

        # this if_wins function will decide who won the game
        # the if wins has been defined in the file above
        # this function has 2 parameters user_score and dealer_score
        # this function call  has been kept out of the while loop such after all hits and loop work it can decide who won
        self.if_wins(user_score, dealer_score)


# start_mission here creates a object for the PlayGame class present in here
start_mission = PlayGame()
start_mission.play_again()
# once the object is made, the function is called for running the program
# when this program is run the first time this is where it all starts

# all the functions have been kept separate from each other such that it is easy to read understand and proves the point of class and objects
