import os
import pygame

pygame.display.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
screen_width = info.current_w

SCALE = screen_width // 640

if SCALE < 1:
    SCALE = 1

WIDTH = int(640 * SCALE)
HEIGHT = int(360 * SCALE)
FPS = 60

CARD_WIDTH = 128 
CARD_HEIGHT = 128 
S_WIDTH = 640
S_HEIGHT = 360

pos_x = int(192 * SCALE)
pos_y = int(32 * SCALE)
gap = int(29 * SCALE)