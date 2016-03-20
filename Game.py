from Hand import Hand
from Deck import Deck

class Game:

    def __init__(self):
        self.hands = self.players()
        self.deck = Deck()


    def players(self):
        number_players = int(input("How many players? "))
        hands = []
        for hand in range(number_players):
            hands.append(Hand())
        return hands


    def deal_hand(self):
        for i in self.hands:
            i.cards.append(self.deck.deck.pop())
            i.cards.append(self.deck.deck.pop())



blackjack = Game()
blackjack.deal_hand()
for x in blackjack.hands:
    player_num = blackjack.hands.index(x) + 1
    print("Player {player} has the following cards: ".format(player=player_num))
    for y in x.cards:
        print(y)
    #     hand_value += y.value
    print(x.hand_value())
    choice = input("Player {player}, would you like to draw another card?  ".format(player=player_num))
    if choice.lower() == "yes":
        x.cards.append(blackjack.deck.deck.pop())
    print(x.hand_value())
