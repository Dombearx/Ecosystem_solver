import random
from consts import BOARD_SIZE, HOLES
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
                self.board[(x, y)] = random.choice(CARDS)(x, y)

    def score(self):
        used_cards = {}
        score = 0
        for card in self.board.values():
            score += card.score(self.board, used_cards)
            used_cards[card.card_type] = 1

        for holes, hole_score in HOLES.items():
            if len(used_cards.items()) >= holes:
                score += hole_score

        return score

    def mutate(self):
        pos_x = random.choice(range(BOARD_SIZE[0]))
        pos_y = random.choice(range(BOARD_SIZE[1]))
        new_card = random.choice(CARDS)(*self.board[(pos_x, pos_y)].pos)
        self.board[(pos_x, pos_y)] = new_card

    def __str__(self):
        result = ""
        for row in range(BOARD_SIZE[0]):
            for column in range(BOARD_SIZE[1]):
                card = self.board[(row, column)]
                tmp = str(card).ljust(8) + " - " + str(card.last_score).rjust(2)
                tmp = tmp.ljust(15)
                result += tmp + " "
            result += "\n"

        return result
