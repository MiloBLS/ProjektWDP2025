import pygame
import src.config as c

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        pygame.display.set_caption("Scoundrel")
        self.clock = pygame.time.Clock()
        self.game_timer = 0
        self.running = True
        self.game_over = False
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
                    if self.game_state == "MENU":
                        self.game_state = "GAME"
                    else:
                        self.game_state = "MENU"
    def _update(self):
        pass
    def _draw(self):
        pygame.display.flip()