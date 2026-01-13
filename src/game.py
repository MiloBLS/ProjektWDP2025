import pygame
import src.config as c
from src.classes.assetmanager import AssetManager
# from src.states.state_machine import StateMachine
# from src.states.menu_state import MenuState
# from src.states.game_state import GameState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        pygame.display.set_caption("Scoundrel")
        self.clock = pygame.time.Clock()
        self.game_timer = 0
        self.running = True
        self.game_over = False
        self.assets = AssetManager()
        self.assets.load_content()
        self.game_state = "MENU"
        self.player_hp = 20
        self._state_machine()

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self._state_machine()
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
        mouse_pos = pygame.mouse.get_pos()

    def _draw(self):
        self.screen.blit(self.assets.get_frame(self.klatka[0], self.klatka[1]))

        pygame.display.flip()

    def _state_machine(self):
        if self.game_state == "MENU":
            self.klatka = ("menu", 0)

        elif self.game_state == "GAME":
            self.klatka = ("bg", self.player_hp)

