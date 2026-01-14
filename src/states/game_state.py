import pygame
import src.config as c
from src.classes.deck import Deck

class GameState:
    def __init__(self, game):
        self.game = game
        self.run_btn_rect = pygame.Rect(int(45 * c.SCALE), int(170 * c.SCALE), int(85 * c.SCALE), int(35 * c.SCALE))
        self.player_hp = 20
        self.deck = Deck(self.game.assets)
        self.deck.shuffle()
        self.run_count = 2
        self._can_run()
        self.room_cards = []
        self.room_cards_slots = [(c.pos_x, c.pos_y), (c.pos_x + c.gap, c.pos_y), (c.pos_x + (c.gap * 2), c.pos_y), (c.pos_x + (c.gap * 3), c.pos_y)]
        self._refill_room

    def _refill_room(self):

        cards_needed = 4 - len(self.room_cards)
        
        for i in range(cards_needed):
            if self.deck.hml() > 0:
                new_card = self.deck.draw() 
                
                slot_index = len(self.room_cards) 
                target_x, target_y = self.room_cards_slots[slot_index]
                
                new_card = pygame.Rect(target_x, target_y, c.CARD_WIDTH, c.CARD_HEIGHT)
                
                self.room_cards.append(new_card)
            else:
                break

    def _can_run(self):
        if self.run_count >= 2:
            self.can_run = True
        else:
            self.can_run = False
        if self.deck.draw():
            self.run_count += 1
        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and not self.game.game_over:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"
            if event.key == pygame.K_0:                                                                     #loophole
                self.run_count += 1    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.run_btn_rect.collidepoint(self.mouse_pos) and self.can_run:
                self.can_run = False
                self.run_count = 0
            

    def update(self):
        self.mouse_pos = self.game.mouse_pos
        self._can_run()

    def draw(self, screen):
        bg_image = self.game.assets.get_frame("bg", self.player_hp)
        screen.blit(bg_image, (0, 0))

        btn_frame_idx = 1 if self.can_run else 0
        btn_image = self.game.assets.get_frame("button", btn_frame_idx)
        screen.blit(btn_image, (0, 0))

    def handle_card_interactions(self):
        pass
    

