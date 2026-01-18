import pygame
import src.config as c

class MenuState:
    def __init__(self, game):
        self.game = game
        self.current_frame_index = 0
        
        self.btn_start = pygame.Rect(int(210 * c.SCALE), int(140 * c.SCALE), int(220 * c.SCALE), int(35 * c.SCALE))
        self.btn_settings = pygame.Rect(int(235 * c.SCALE), int(190 * c.SCALE), int(165 * c.SCALE), int(35 * c.SCALE))
        self.btn_scores = pygame.Rect(int(265 * c.SCALE), int(240 * c.SCALE), int(110 * c.SCALE), int(35 * c.SCALE))
        self.btn_quit = pygame.Rect(int(275 * c.SCALE), int(290 * c.SCALE), int(85 * c.SCALE), int(35 * c.SCALE))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.current_frame_index == 1:
                    self.game.current_state = "GAME"
                elif self.current_frame_index == 2:
                    self.game.current_state = "SETTINGS"
                elif self.current_frame_index == 3:
                    self.game.scores_state.load_scores()
                    self.game.current_state = "SCORES"
                elif self.current_frame_index == 4:
                    self.game.running = False

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.btn_start.collidepoint(self.mouse_pos):
            self.current_frame_index = 1
        elif self.btn_settings.collidepoint(self.mouse_pos):
            self.current_frame_index = 2
        elif self.btn_scores.collidepoint(self.mouse_pos):
            self.current_frame_index = 3
        elif self.btn_quit.collidepoint(self.mouse_pos):
            self.current_frame_index = 4
        else:
            self.current_frame_index = 0

    def draw(self, screen):
        image = self.game.assets.get_frame("menu", self.current_frame_index)
        screen.blit(image, (0, 0))

        