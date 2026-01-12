from src.classes.spritesheet import SpriteSheet
import config as c

bg_sheet = SpriteSheet("assets/ui/background.png")
menu_sheet = SpriteSheet("assets/ui/menu.png")
button_sheet = SpriteSheet("assets/ui/menu.png")
pik_sheet = SpriteSheet("assets/cards/karta_basic_as")
karo_sheet = SpriteSheet("assets/cards/karta_basic_karo")
kier_sheet = SpriteSheet("assets/cards/karta_basic_kier")
trefl_sheet = SpriteSheet("assets/cards/karta_basic_trefl")
cbg_sheet = SpriteSheet("assets/cards/card_back.png")
cbgh_sheet = SpriteSheet("assets/cards/card_back_highlight.png")

bg_frames = {}
menu_frames = {}
button_frames = {}
pik_frames = {}
karo_frames = {}
kier_frames = {}
trefl_frames = {}
cbg_frames = {}
cbgh_frames = {}

for frame_index in range(21):
    image = bg_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
    bg_frames[frame_index] = image

for frame_index in range(5):
    image = menu_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
    menu_frames[frame_index] = image

for frame_index in range(2):
    image_button = button_sheet.get_image(frame_index, c.S_WIDTH, c.S_HEIGHT, (0,0,0))
    image_cbg = cbg_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    image_cbgh = cbgh_sheet.get_image(frame_index,c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    button_frames[frame_index] = image_button
    cbg_frames[frame_index] = image_cbg
    cbgh_frames[frame_index] = image_cbgh

for frame_index in range(13):
    image_pik = pik_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    image_trefl = trefl_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    pik_frames[frame_index] = image_pik
    trefl_frames[frame_index] = image_trefl

for frame_index in range(9):
    image_kier = kier_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    image_karo = karo_sheet.get_image(frame_index, c.CARD_WIDTH, c.CARD_HEIGHT, (0,0,0))
    kier_frames[frame_index]= image_kier
    karo_frames[frame_index]= image_karo