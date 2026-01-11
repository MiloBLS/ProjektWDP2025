import pygame
import src.config as c

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
        
    def get_image(self, frame, width, height, color, scale = c.SCALE):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet,(0, 0),((frame*width), 0, width, height))
        image.set_colorkey(color)

        new_width = int(width * scale)
        new_height = int(height * scale)

        image = pygame.transform.scale(image, (new_width, new_height))

        return image