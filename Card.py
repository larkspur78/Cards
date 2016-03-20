class Card:
#represents a standard playing card

    def __init__(self, suit_name, face_name, value):
        self.suit_name = suit_name
        self.face_name = face_name
        self.value = value

    def __repr__(self):
        return "{}{}".format(self.face_name, self.suit_name)
