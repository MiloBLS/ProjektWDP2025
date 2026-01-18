import pygame
import src.config as c

class SettingsState:
    def __init__(self, game):
        self.game = game
        self.one_rect = pygame.Rect(int(304 * c.SCALE), int(143 * c.SCALE), int(29 * c.SCALE), int(21 * c.SCALE))
        self.two_rect = pygame.Rect(int(352 * c.SCALE), int(143 * c.SCALE), int(33 * c.SCALE), int(21 * c.SCALE))
        self.four_rect = pygame.Rect(int(400 * c.SCALE), int(143 * c.SCALE), int(39 * c.SCALE), int(21 * c.SCALE))



    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.current_frame_index == 0:
                    c.current_speed_index = 0
                if self.current_frame_index == 1:
                    c.current_speed_index = 1
                if self.current_frame_index == 2:
                    c.current_speed_index = 2


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.one_rect.collidepoint(self.mouse_pos) or c.current_speed_index == 0:
            self.current_frame_index = 0
        if self.two_rect.collidepoint(self.mouse_pos) or c.current_speed_index == 1:
            self.current_frame_index = 1
        if self.four_rect.collidepoint(self.mouse_pos) or c.current_speed_index == 2:
            self.current_frame_index = 2

    def draw(self, screen):
        bg = self.game.assets.get_frame("settings", self.current_frame_index)
        screen.blit(bg, (0, 0))