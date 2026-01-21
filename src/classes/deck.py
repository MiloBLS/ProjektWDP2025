import random
from src.classes.card import Card

class Deck:
    def __init__(self, manager):
        self.manager = manager
        self.cards = []
        self._build()

    def _build(self):                                                           #Konstruuje talię kart
        suits = ["pik", "trefl", "kier", "karo"]

        for suit in suits:
            for value in range(13):
                if (suit == "kier" or suit == "karo") and value > 8:
                    continue

                new_card = Card(suit, value)
                card_image = self.manager.get_frame(suit, value)
                new_card.set_img(card_image)
                self.cards.append(new_card)

    def shuffle(self):                                                          #Tasuje karty
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
    def run(self, cards_to_run):
        for card in cards_to_run:
            self.cards.insert(0, card)

    def hml(self):                                                                #Zwraca ilość pozostałych kart w talii
        return len(self.cards)