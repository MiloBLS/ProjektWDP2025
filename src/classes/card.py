import pygame

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def set_img(self, img):
        self.img = img
    def get_img(self):
        return self.img
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def get_rect(self):
        return self.img.get_rect()