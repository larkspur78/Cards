#represents a standard playing card
class Card:
    #this is what happens when you initialize a new card
    #self refers to the actual occurence of a card, such as "the Hannah version of a human"
    #suit-name, face-name and value give me the ability to set values on a card when it is created
    def __init__(self, suit_name, face_name, value):
        #says to set the value suit_name to be the value that we called suit_name in the init
        self.suit_name = suit_name
        #uses self(referring to actual occurence of a card), attached to a given name .face_name,
        #which is then assigned the value of face_name(from the line defining the initializion of face_name)
        self.face_name = face_name
        self.value = value

    def __repr__(self):
        #.format lets us format strings conveniently with placeholders.
        #this repr method allows us to override the listing of card objects in
        #memory location form and instead see them represented in face_name and suit_name format
        #curly brackets are built into this particular string formatting using .format.
        return "{}{}".format(self.face_name, self.suit_name)
