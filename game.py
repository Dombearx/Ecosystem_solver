from utils import HOLES
import random
from cards import *

CARDS = (
    Rabbit,
    Fish,
    Fox,
    Bear,
    # Dragonfly,
    Bee,
    Eagle,
    Wolf,
    Deer,
    River,
    Meadow,
)


class Board:
    def __init__(self):
        self.board = {}
        for x in range(BOARD_SIZE[0]):
            for y in range(BOARD_SIZE[1]):
                self.board[(x, y)] = (random.choice(CARDS)(x, y))

    def score(self):
        used_cards = {}
        score = 0
        for card in self.board.values():
            score += card.score(self.board, used_cards)
            used_cards[card.card_type] = 1

        for holes, hole_score in HOLES.items():
            if len(used_cards.items()) >= holes:
                score += hole_score

        print(score)

    def mutate(self):
        pos_x = random.choice(range(BOARD_SIZE[0]))
        pos_y = random.choice(range(BOARD_SIZE[1]))
        new_card = random.choice(CARDS)(*self.board[(pos_x, pos_y)].pos)
        self.board[(pos_x, pos_y)] = new_card

    def __str__(self):
        result = ""
        for idx, card in enumerate(self.board.values()):
            tmp = str(card) + " - " + str(card.last_score)
            tmp = tmp.ljust(10)
            result += tmp + " "
            if (idx + 1) % BOARD_SIZE[0] == 0:
                result += "\n"

        return result
