from src.classes.spritesheet import SpriteSheet
import src.config as c

class AssetManager:
    def __init__(self):
        self.bg_frames = {}
        self.menu_frames = {}
        self.button_frames = {}
        self.weapon_button_frames = {}
        self.pik_frames = {}
        self.karo_frames = {}
        self.kier_frames = {}
        self.trefl_frames = {}
        self.cbg_frames = {}
        self.cbgh_frames = {}
        self.game_over_frames = {}
        self.input_frames = {}
        self.scores_frames = {}

    def load_content(self):
        bg_sheet = SpriteSheet("assets/ui/background.png", False)
        menu_sheet = SpriteSheet("assets/ui/menu.png", False)
        button_sheet = SpriteSheet("assets/ui/button.png")
        weapon_button_sheet = SpriteSheet("assets/ui/weapon_button.png")
        pik_sheet = SpriteSheet("assets/cards/karta_basic_as.png")
        karo_sheet = SpriteSheet("assets/cards/karta_basic_karo.png")
        kier_sheet = SpriteSheet("assets/cards/karta_basic_kier.png")
        trefl_sheet = SpriteSheet("assets/cards/karta_basic_trefl.png")
        cbg_sheet = SpriteSheet("assets/cards/card_back.png")
        cbgh_sheet = SpriteSheet("assets/cards/card_back_highlight.png")
        game_over_sheet = SpriteSheet("assets/ui/game_over_screen.png", False)
        input_sheet = SpriteSheet("assets/ui/input.png")
        scores_sheet = SpriteSheet("assets/ui/scores.png")

        for frame_index in range(21):
            self.bg_frames[frame_index] = bg_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT)

        for frame_index in range(5):
            self.menu_frames[frame_index] = menu_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT)

        for frame_index in range(2):
            image_button = button_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
            image_weapon_button = weapon_button_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
            image_cbg = cbg_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            image_cbgh = cbgh_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            image_input = input_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
            self.button_frames[frame_index] = image_button
            self.weapon_button_frames[frame_index] = image_weapon_button
            self.cbg_frames[frame_index] = image_cbg
            self.cbgh_frames[frame_index] = image_cbgh
            self.input_frames[frame_index] = image_input

        for frame_index in range(13):
            image_pik = pik_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            image_trefl = trefl_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            self.pik_frames[frame_index] = image_pik
            self.trefl_frames[frame_index] = image_trefl

        for frame_index in range(9):
            image_kier = kier_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            image_karo = karo_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (255,0,255))
            self.kier_frames[frame_index] = image_kier
            self.karo_frames[frame_index] = image_karo

        for frame_index in range(3):
            image_game_over = game_over_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT)
            image_scores = scores_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT)
            self.game_over_frames[frame_index] = image_game_over
            self.scores_frames[frame_index] = image_scores
            
    def get_frame(self, name, value):
        frames = getattr(self, f"{name}_frames")
        return frames.get(value)
