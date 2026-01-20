import pygame
import src.config as c
from src.classes.deck import Deck

class GameState:
    def __init__(self, game):
        self.game = game
        self.run_btn_rect = pygame.Rect(int(45 * c.SCALE), int(170 * c.SCALE), int(85 * c.SCALE), int(35 * c.SCALE))
        self.wepaon_button_rect = pygame.Rect(int(48 * c.SCALE), int(317 * c.SCALE), int(79 *c.SCALE), int(31 *c.SCALE))
        self.player_hp = 20
        self.current_weapon = 0
        self.last_monster_value = 0
        self.monsters = 0
        self.cards_played_this_turn = 0

        self.deck = Deck(self.game.assets)
        self.deck_rect = pygame.Rect(c.deck_pos_x, c.pos_y, int(c.CARD_WIDTH * c.SCALE), int(c.CARD_HEIGHT * c.SCALE))
        self.deck.shuffle()

        self.can_run = True
        self.healed = False
        self.hand = False
        

        self.room_cards = []
        self.room_cards_slots = [(c.pos_x, c.pos_y), (c.pos_x + c.gap, c.pos_y), (c.pos_x + (c.gap * 2), c.pos_y), (c.pos_x + (c.gap * 3), c.pos_y)]
        self._refill_room()

        self.discard_pile = []
        self.weapon = []
        self.monsters_pile = []

    def _refill_room(self):
        self.can_run = True
        self.healed = False
        self.cards_played_this_turn = 0

        for card in self.room_cards:
            target_x, target_y = self.room_cards_slots[0]
            card.move_to(target_x, target_y)

        cards_needed = 4 - len(self.room_cards)

        if cards_needed > 0 and self.deck.hml() > 0:
            self.draw_anim_timer = 1 * c.FPS

        for i in range(cards_needed):
            if self.deck.hml() > 0:
                new_card = self.deck.draw() 
                if new_card is not None:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.current_state = "MENU"
            if event.key == pygame.K_0:                                                                     #do testowania
                self.player_hp = 20
            if event.key == pygame.K_9:
                self.can_run = True                                                                         #do testowania
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.run_btn_rect.collidepoint(self.mouse_pos) and self.can_run and self.cards_played_this_turn == 0:
                self.deck.run(self.room_cards)
                self.room_cards.clear()
                self._refill_room()
                self.can_run = False
            if self.wepaon_button_rect.collidepoint(self.mouse_pos):
                if self.hand:
                    self.hand = False
                else:
                    self.hand = True
        self.handle_card_interactions(event)

    def update(self):
        self.mouse_pos = self.game.mouse_pos

        if self.draw_anim_timer > 0:
            self.draw_anim_timer -= 1

        for card in self.room_cards:
            card.update()

        for card in self.weapon:
            card.update()
        
        for card in self.monsters_pile:
            card.update()
            
        for card in self.discard_pile:
            card.update()

        if self.player_hp <= 0:
            self.calculate_score_and_end_game()
        else:
            for card in self.room_cards:
                suit = card.get_suit()
                if suit in ["trefl", "pik"]:
                    break
                else:
                    for card in self.deck.cards:
                        suit = card.get_suit()
                        if suit in ["trefl", "pik"]:
                            break
                        else:
                            self.calculate_score_and_end_game()
            
                    

    def draw(self, screen):
        bg_image = self.game.assets.get_frame("bg", max(0,self.player_hp))
        screen.blit(bg_image, (0, 0))

        btn_frame_idx = 1 if self.can_run and self.cards_played_this_turn == 0 else 0
        btn_image = self.game.assets.get_frame("button", btn_frame_idx)
        screen.blit(btn_image, (0, 0))

        weapon_button_idx = 1 if self.hand else 0
        wepaon_button_image = self.game.assets.get_frame("weapon_button", weapon_button_idx)
        screen.blit(wepaon_button_image, (0, 0))

        if self.deck.hml() > 0:
            if self.draw_anim_timer > 0:
                 screen.blit(self.game.assets.get_frame("cbgh", 1), self.deck_rect)
            else:
                 screen.blit(self.game.assets.get_frame("cbg", 0), self.deck_rect)


        for card in self.room_cards:
            img = card.get_img()
            screen.blit(img, card.rect)
            # pygame.draw.rect(screen, (255, 0, 0), card, 1)                             test hitbox kart
        for card in self.discard_pile:
            img = card.get_img()
            screen.blit(img, card.rect)
        for card in self.monsters_pile:
            img = card.get_img()
            screen.blit(img, card.rect)
        for card in self.weapon:
            img = card.get_img()
            screen.blit(img, card.rect)

    def handle_card_interactions(self, event):
        clicked_card = None
        
        for card in self.room_cards:
            if card.rect.collidepoint(self.mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked_card = card
                        break
        
        if clicked_card:
            suit = clicked_card.get_suit()
            card_value = clicked_card.get_value() + 2 
            
            if suit == "kier":
                if self.healed == False:
                    if self.player_hp + card_value > 20:
                        card_value = card_value - ((self.player_hp + card_value) - 20)
                        self.player_hp += card_value
                    else:
                        self.player_hp += card_value
                    self.healed = True
                    self.discard_pile.append(clicked_card)
                    clicked_card.move_to(int(c.pos_x + (3 * c.gap)), c.bottom_pos_y)
                else:
                    self.discard_pile.append(clicked_card)
                    clicked_card.move_to(int(c.pos_x + (3 * c.gap)), c.bottom_pos_y)

            elif suit == "karo":
                for card in self.weapon:
                    self.discard_pile.append(card)
                for card in self.monsters_pile:
                    self.discard_pile.append(card)
                if len(self.discard_pile) > 0:
                    for card in self.discard_pile:
                        card.move_to(int(c.pos_x + (3 * c.gap)), c.bottom_pos_y)
                self.weapon.clear()
                self.monsters_pile.clear()
                self.current_weapon = card_value
                self.last_monster_value = 0
                self.monsters = 0
                self.weapon.append(clicked_card)
                for card in self.weapon:
                    card.move_to(int(c.pos_x), c.bottom_pos_y)

            elif suit in ["trefl", "pik"]:
                damage = 0
                
                if self.hand == False:
                    can_use_weapon = (self.current_weapon > 0) and (self.last_monster_value == 0 or card_value <= self.last_monster_value)
                    
                    if can_use_weapon:
                        damage = card_value - self.current_weapon
                        if damage < 0:
                            damage = 0
                        self.last_monster_value = card_value

                        self.monsters_pile.append(clicked_card)
                        offset_x = (len(self.monsters_pile) - 1) * 50
                        target_x = int(c.pos_x + c.gap + offset_x)
                        clicked_card.move_to(target_x, c.bottom_pos_y)
                    else:
                        damage = card_value
                        self.discard_pile.append(clicked_card)
                        clicked_card.move_to(int(c.pos_x + (3 * c.gap)), c.bottom_pos_y)
                else:
                        damage = card_value
                        self.discard_pile.append(clicked_card)
                        clicked_card.move_to(int(c.pos_x + (3 * c.gap)), c.bottom_pos_y)

                
                
                self.player_hp -= damage
                self.monsters += 1

            self.room_cards.remove(clicked_card)
            self.cards_played_this_turn += 1
            
            self.can_run = False

            if len(self.room_cards) <= 1:
                self._refill_room()
    
    def calculate_score_and_end_game(self):
        if self.player_hp <= 0:
            monsters_strength_left = 0
            
            for card in self.deck.cards:
                suit = card.get_suit()
                if suit in ["trefl", "pik"]:
                    monsters_strength_left += (card.get_value() + 2)

            for card in self.room_cards:
                suit = card.get_suit()
                if suit in ["trefl", "pik"]:
                    monsters_strength_left += (card.get_value() + 2)


            final_score = self.player_hp - monsters_strength_left
            
            self.game.game_over_state.set_score(final_score)
            self.game.current_state = "GAME_OVER"

        else:
            potions_left = 0

            for card in self.room_cards:
                suit = card.get_suit()
                if suit == "kier":
                    potions_left += (card.get_value() + 2)
                
            final_score = self.player_hp + potions_left

            self.game.game_over_state.set_score(final_score)
            self.game.current_state = "GAME_OVER"