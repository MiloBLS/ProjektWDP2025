import pygame
import src.config as c

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        
    def get_image(self, frame, width, height, color, scale = c.SCALE):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet,(0, 0),((frame*width), 0, width, height))
        image = pygame.transform.scale(image, width* scale, height * scale)
        image.set_colorkey(color)

        return image