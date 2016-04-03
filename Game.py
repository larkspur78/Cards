from Hand import Hand
from Deck import Deck

class Game:

    def __init__(self):
        #created a list of hands objects
        self.hands = self.players()
        #created an object of type Deck
        self.blackjack_deck = Deck()


    def players(self):
        number_players = int(input("How many players? "))
        #assign hands the value of an empty list
        #this list is not filled until we get to deal_hand
        hands = []
        #for the number_players obtained from user input
        for hand in range(number_players):
            #when you need a collection of objects of the same type,
            #the program will look similar to this. In this case, we need
            #a list of hands
            hands.append(Hand())
        return hands


    def deal_hand(self):
        #for each hand/player in the number of hands/players
        for current_hand in self.hands:
            #calling the pop method on the list of cards called deck that is an
            #attribute of blackjack_deck
            #the popped cards are appended to the cards list of the list we are
            #currently on in the for loop
            current_hand.cards.append(self.blackjack_deck.deck.pop())
            current_hand.cards.append(self.blackjack_deck.deck.pop())

#instantiate a game and call it blackjack
#instantiation is done using a Class ~ blueprint of an object ~
blackjack = Game()
#call deal_hand function on instantiated blackjack game
blackjack.deal_hand()
#for each item in the list blackjack.hands
for x in blackjack.hands:
    #assign the variable player_num the value of
    #call index method on x in reference to the list blackjack.hands ~ which returns value of index of x in list of blackjack.hands ~
    #because this would normally be returned starting at 0, we will adjust by adding one
    player_num = blackjack.hands.index(x) + 1
    print("Player {player} has the following cards: ".format(player=player_num))
    #go through each card ~y~ in player x's hand
    for y in x.cards:
        print(y)
    #outside the for loop, call the hand_value method on the object Hand x
    print(x.hand_value())
    choice = input("Player {player}, would you like to draw another card?  ".format(player=player_num))

    if choice.lower() == "yes":
        #now blackjack knows what itself is, so we can just call blackjack instead
        #of self.blackjack. Now instead of calling current_hand we can refer to x,
        #which is the actual index of each blackjack hand
        x.cards.append(blackjack.blackjack_deck.deck.pop())
    print(x.hand_value())
