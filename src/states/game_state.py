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
        self.can_run = True
        self.deck_rect = pygame.Rect(c.deck_pos_x, c.pos_y, int(c.CARD_WIDTH * c.SCALE), int(c.CARD_HEIGHT * c.SCALE))
        
        self.room_cards = []
        self.room_cards_slots = [(c.pos_x, c.pos_y), (c.pos_x + c.gap, c.pos_y), (c.pos_x + (c.gap * 2), c.pos_y), (c.pos_x + (c.gap * 3), c.pos_y)]
        self._refill_room()

    def _refill_room(self):
        self.can_run = True

        cards_needed = 4 - len(self.room_cards)

        if cards_needed > 0 and self.deck.hml() > 0:
            self.draw_anim_timer = 1 * c.FPS

        for i in range(cards_needed):
            if self.deck.hml() > 0:
                new_card = self.deck.draw() 
                
                slot_index = len(self.room_cards) 
                target_x, target_y = self.room_cards_slots[slot_index]

                start_x = self.deck_rect.x
                start_y = self.deck_rect.y

                new_card.rect = pygame.Rect(start_x, start_y, int(c.CARD_WIDTH * c.SCALE), int(c.CARD_HEIGHT * c.SCALE))

                new_card.move_to(target_x, target_y)
                
                self.room_cards.append(new_card)
            else:
                break

        
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and not self.game.game_over:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"
            if event.key == pygame.K_0:                                                                     #loophole
                self.can_run = True 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.run_btn_rect.collidepoint(self.mouse_pos) and self.can_run:
                self.deck.run(self.room_cards)
                self._refill_room()
                self.can_run = False
            

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.draw_anim_timer > 0:
            self.draw_anim_timer -= 1

        for card in self.room_cards:
            card.update()


    def draw(self, screen):
        bg_image = self.game.assets.get_frame("bg", self.player_hp)
        screen.blit(bg_image, (0, 0))

        btn_frame_idx = 1 if self.can_run else 0
        btn_image = self.game.assets.get_frame("button", btn_frame_idx)
        screen.blit(btn_image, (0, 0))

        if self.deck.hml() > 0:                                                             #start
            if self.draw_anim_timer > 0:
                 screen.blit(self.game.assets.get_frame("cbgh", 1), self.deck_rect)
            else:
                 screen.blit(self.game.assets.get_frame("cbg", 0), self.deck_rect)
        else:
            pass                                                                            #stop

        for card in self.room_cards:
            img = card.get_img()
            screen.blit(img, card.rect)
            # pygame.draw.rect(screen, (255, 0, 0), card, 1)                                test hitbox kart n

        

    def handle_card_interactions(self):
        pass
    

