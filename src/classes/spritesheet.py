import pygame
import src.config as c

class SpriteSheet():
    def __init__(self, source, isalpha = False):
        self.source = source
        self.isalpha = isalpha
        self._load()
    def _load(self):
        if self.isalpha:
            self.sheet = pygame.image.load(self.source).convert_alpha()
        else:
            self.sheet = pygame.image.load(self.source).convert()

    def get_image(self, frame, width, height, color, scale = c.SCALE):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet,(0, 0),((frame*width), 0, width, height))
        image.set_colorkey(color)

        new_width = int(width * scale)
        new_height = int(height * scale)

        image = pygame.transform.scale(image, (new_width, new_height))

        return image