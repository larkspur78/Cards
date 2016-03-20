from Card import Card
from random import shuffle


class Deck:
    face_names = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
    '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    suit_names = ('\u2660', '\u2665', '\u2666', '\u2663')

    def __init__(self):
        self.deck = self.make_deck(self.face_names, self.suit_names)


    def make_deck(self, face_names, suit_names):
        deck = []
        for suit_name in suit_names:
            for face, value in face_names.items():
                #make a new card with current suit and rank
                new_card = Card(suit_name, face, value)
                #add card to deck list
                deck.append(new_card)
        return deck

    #This deck is in order, but we can easily shuffle it.
    def shuffle_deck(self):
        shuffle(self.deck)
