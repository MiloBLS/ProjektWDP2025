class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.img = None
    def set_img(self, img):
        self.img = img
    def get_img(self):
        return self.img
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value