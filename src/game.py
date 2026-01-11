import pygame
import src.config as c
from src.classes.card import Card
from src.classes.spritesheet import SpriteSheet
from src.classes.loader import load_image

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        pygame.display.set_caption("Scoundrel")
        self.clock = pygame.time.Clock() #NIE WIEM CZY BĘDZIE POTRZEBNE
        self.game_timer = 0
        self.running = True
        self.card = Card() #NIE WIEM CZY BĘDZIE POTRZEBNE
        self.game_over = False
        #obrazki
        self.bg = SpriteSheet(load_image("ui/background.png", alpha = False))
        self.bg0 = self.bg.get_image(0, c.WIDTH, c.HEIGHT, (0,0,0))
    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(c.FPS)
        pygame.quit()
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.game_over:
                if event.key == pygame.K_ESCAPE:
                    game_state = "MENU"
    def _update(self):
        pass
    def _draw(self):
        self.screen.blit(self.bg0, (0, 0))