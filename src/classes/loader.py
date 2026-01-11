# plik: src/utils/loader.py
import pygame
import os

def load_image(path, alpha=True):
    full_path = os.path.join("assets", path)
    image = pygame.image.load(full_path)
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
        
    return image
