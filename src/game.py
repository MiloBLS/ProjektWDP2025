import pygame
import src.config as c
from src.classes.assetmanager import AssetManager
from src.states.menu_state import MenuState
from src.states.game_state import GameState
from src.states.game_over_state import GameOverState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Scoundrel")
        self.clock = pygame.time.Clock()
        self.game_timer = 0
        self.running = True
        self.assets = AssetManager()
        self.assets.load_content()
        self.current_state = "MENU"
        self.menu_state = MenuState(self)
        self.game_state = GameState(self)
        self.game_over_state = GameOverState(self)
        

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
            
            if self.current_state == "MENU":
                self.menu_state.handle_events(event)
            
            elif self.current_state == "GAME":
                self.game_state.handle_events(event)

            elif self.current_state == "GAME_OVER":
                self.game_over_state.handle_events(event)

    def _update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.current_state == "MENU":
            self.menu_state.update()
            
        elif self.current_state == "GAME":
            self.game_state.update()

        elif self.current_state == "GAME_OVER":
            self.game_over_state.update()

    def _draw(self):
        if self.current_state == "MENU":
            self.menu_state.draw(self.screen)

        if self.current_state == "GAME":
            self.game_state.draw(self.screen)

        elif self.current_state == "GAME_OVER":
            self.game_over_state.draw(self.screen)

        pygame.display.flip()


