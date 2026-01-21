import pygame
import src.config as c

class ScoresState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("assets/fonts/alagard.ttf", int(16 * c.SCALE))
        self.scores = []
        self.load_scores()

        self.menu_rect = pygame.Rect(int(58 * c.SCALE), int(291 * c.SCALE), int(80 * c.SCALE), int(22 * c.SCALE))
        self.clear_rect = pygame.Rect(int(480 * c.SCALE), int(269 * c.SCALE), int(118 * c.SCALE), int(56 * c.SCALE))

    def load_scores(self):                                              #Funkcja odzcytująca dane z pliku scores.txt
        self.scores = []
        with open("src/scores.txt", "r") as f:
            lines = f.readlines()
            sorted_scores = []
            for line in lines:
                if ":" in line:
                    name, score = line.strip().split(":", 1)
                    sorted_scores.append((name.strip(), int(score.strip())))

            sorted_scores.sort(key=lambda x: x[1], reverse=True)
            self.scores = sorted_scores[:8]
        f.close()

    def clear_scores(self):                                             #Funkcja czyszcząca dane 
        with open("src/scores.txt", "w") as f:
            f.write("")
        self.load_scores()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.current_frame_index == 1:
                    self.game.current_state = "MENU"
                elif self.current_frame_index == 2:
                    self.clear_scores()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"
                

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.menu_rect.collidepoint(self.mouse_pos):
            self.current_frame_index = 1
        elif self.clear_rect.collidepoint(self.mouse_pos):
            self.current_frame_index = 2
        else:
            self.current_frame_index = 0

    def draw(self, screen):
        image = self.game.assets.get_frame("scores", self.current_frame_index)
        screen.blit(image, (0, 0))

        start_y = int(135 * c.SCALE)
        line_height = int(25 * c.SCALE)

        for i, (name, score) in enumerate(self.scores):
            color = (255, 255, 255)
            if i == 0: color = (255, 215, 0)
            elif i == 1: color = (192, 192, 192)
            elif i == 2: color = (205, 127, 50)

            text = f"{i+1}. {name}: {score}"
            score_surf = self.font.render(text, True, color)
            score_rect = score_surf.get_rect(center=(c.WIDTH // 2, start_y + i * line_height))
            screen.blit(score_surf, score_rect)