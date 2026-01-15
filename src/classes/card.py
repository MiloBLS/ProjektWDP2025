import pygame
import src.config as c

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.rect = None
        self.target_pos = None
        self.speed = c.speed
    def set_img(self, img):
        self.img = img
    def get_img(self):
        return self.img
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def move_to(self, x, y):
        self.target_pos = (x, y)
    def update(self):
        if self.rect and self.target_pos:
            target_x, target_y = self.target_pos

            dx = target_x - self.rect.x
            dy = target_y - self.rect.y

            if abs(dx) < self.speed and abs(dy) < self.speed:
                self.rect.x = target_x
                self.rect.y = target_y
                self.target_pos = None
            else:
                move_x = self.speed if dx > 0 else -self.speed
                move_y = self.speed if dy > 0 else -self.speed
            
                if abs(dx) < self.speed: move_x = 0
                if abs(dy) < self.speed: move_y = 0
                
                self.rect.x += move_x
                self.rect.y += move_y