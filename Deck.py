from Card import Card
from random import shuffle

#keeping specifics at higher levels lets code be more reusable and extensible

class Deck:
    #attributes should be accessible to entire Deck class,
    #which is why they are defined outside methods
    #dictionary uses a key/value pair
    #within the face_names attribute, a dictionary is defined, giving the face name
    #of a card in string form as the key, and the value for that face name as the
    #value part of that pair
    face_names = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
    '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

    #the suit_names attribute is defined using four values, which are the
    #unicode values for spades, hearts, clubs, and diamonds
    #escape symbol is used before u so that Python knows I'm sending it in unicode
    suit_names = ('\u2660', '\u2665', '\u2666', '\u2663')

    #this method is giving instructions for when a new Deck is made
    #in this specific class, if we didn't use init, we would get a Deck with no cards
    def __init__(self):
        #when you access through self, you are accessing the face names and suit
        #names of an actual deck
        #sets up instructions for when you want to make a deck
        #make_deck is local scope, but it can see things happening at the Deck
        #global level, which in this instance includes make_deck defined in method below
        self.deck = self.make_deck(self.face_names, self.suit_names)

    #this method is giving us the ability to make a deck consisting of individual cards
    #using the arguments face_names and suit_names
    #use self here so that we can access it off of an actual deck
    def make_deck(self, face_names, suit_names):
        #deck gets defined as an empty list
        deck = []
        #computer goes to the first item in the suit_names list defined above - spades, for example.
        #in the second nested for loop, it retrieves, one by one using the items method,
        #the face and value for each spade card until it runs out of spade cards.
        #It instantiates a new card with these values and after creation, adds that card to the deck list using
        #the append list method ~ Append is a method that belongs to list ~
        #Then it goes back up to the top for loop and evaluates the next item in suit_names,
        #which might be hearts, for example. It retrieves the face and value pair for each heart card.
        #It repeats this process for all the items in suit_name and all the face value pairs within each suit.
        #When it runs out of cards to make, it goes outside both for loops and sees the return statement which
        #causes it to return an entire deck made up of those already-made individual card objects. This particular module will
        #list the cards in sequential order based on the original definitions, because the shuffle_deck
        #method using random is used in a different method to shuffle the deck.
        for suit_name in suit_names:
            #calling items method on face_names returns a key and a value
            for face, value in face_names.items():
                #make or "instanstiate" a new card with current suit, and rank and value
                new_card = Card(suit_name, face, value)
                #add card to deck list
                deck.append(new_card)
        #after the above for loops are exhausted, send back the newly created deck list
        return deck

    #This deck is in order, but we can easily shuffle it.
    def shuffle_deck(self):
        shuffle(self.deck)
