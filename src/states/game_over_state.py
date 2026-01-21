import pygame
import src.config as c
from src.states.game_state import GameState

class GameOverState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("assets/fonts/alagard.ttf", int(16 * c.SCALE * 2))
        
        self.player_name = ""
        self.input_active = False

        self.frame_idx = 0
        self.input_frame = 0

        self.input_rect = pygame.Rect(int(203 * c.SCALE), int(200 * c.SCALE), int(233 * c.SCALE), int(45 * c.SCALE))
        self.btn_retry_rect = pygame.Rect(int(40 * c.SCALE), int(260 * c.SCALE), int(261 * c.SCALE), int(27 * c.SCALE))
        self.btn_save_rect = pygame.Rect(int(412 * c.SCALE), int(261 * c.SCALE), int(189 * c.SCALE), int(27 * c.SCALE))
        
        self.score = 0
        self.score_saved = False

    def set_score(self, score):                         #Funkcja używana przy zakańczanu rogrywki w game state
        self.score = score
        self.score_saved = False
        self.player_name = ""

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(self.mouse_pos):
                self.input_active = True
            else:
                self.input_active = False
            
            if self.frame_idx == 1:
                self.game.game_state = GameState(self.game)
                self.game.current_state = "GAME"
            elif self.frame_idx == 2:
                self.save_score()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"
            if self.input_active and not self.score_saved:
                if event.key == pygame.K_RETURN:
                    self.save_score()
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    if len(self.player_name) < 15:
                        self.player_name += event.unicode

    def save_score(self):                                           #Funkcja zapisująca wynik do pliku scores.txt
        if self.player_name.strip() == "":
            return    
        else:
            with open("src/scores.txt", "a") as f:
                f.write(f"{self.player_name}: {self.score}\n")
                f.close()

            self.score_saved = True

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.btn_retry_rect.collidepoint(self.mouse_pos):
            self.frame_idx = 1
        elif self.btn_save_rect.collidepoint(self.mouse_pos) and not self.score_saved:
            self.frame_idx = 2
        else:
            self.frame_idx = 0
        
        if self.input_active:
            self.input_frame = 1
        else:
            self.input_frame = 0

    def draw(self, screen):
        bg = self.game.assets.get_frame("game_over", self.frame_idx)
        screen.blit(bg, (0,0))

        bt = self.game.assets.get_frame("input", self.input_frame)
        screen.blit(bt, (0,0))
        
        text_score = self.font.render(f"{self.score}", True, (255, 255, 255))
        screen.blit(text_score, (int(312 * c.SCALE), int(150 * c.SCALE)))

        
        txt_surface = self.font.render(self.player_name, True, (255, 255, 255))
        screen.blit(txt_surface, (self.input_rect.x + int(10 * c.SCALE), self.input_rect.y + int(10 * c.SCALE)))
        
        if not self.score_saved and self.player_name.strip() == "":
            hint = self.font.render("Wpisz nazwe:", True, (150, 150, 150))
            screen.blit(hint, (self.input_rect.x + int(10 * c.SCALE), self.input_rect.y + int(10 * c.SCALE)))
        if self.score_saved:
            saved_msg = self.font.render("Zapisano!", True, (0, 255, 0))
            screen.blit(saved_msg, (self.btn_save_rect.x, self.btn_save_rect.y + int(30 * c.SCALE)))


