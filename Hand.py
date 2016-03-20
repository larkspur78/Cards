class Hand():

    def __init__(self):
        self.cards = []


    def hand_value(self):
        hand_value = 0
        for card in self.cards:
            hand_value += card.value
        return hand_value
