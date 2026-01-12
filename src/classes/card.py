from src.classes.assetmanager import pik_frames, trefl_frames, karo_frames, kier_frames

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self._setimg()
    def _setimg(self):
        if self.suit == "pik":
            self.img = pik_frames[self.value]
        elif self.suit == "trefl":
            self.img = trefl_frames[self.value]
        elif self.suit == "kier":
            self.img = kier_frames[self.value]
        elif self.suit == "karo":
            self.img = karo_frames[self.value]
    def getimg(self):
        return self.img
    def getsuit(self):
        return self.suit
    def getvalue(self):
        return self.value