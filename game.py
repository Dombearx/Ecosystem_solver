from utils import BOARD_SIZE
import random
from cards import *

CARDS = (
    Rabbit,
    Fish,
    Fox,
    Bear,
    Dragonfly,
    Bee,
    Eagle,
    Wolf,
    Deer,
    River,
    Meadow,
)


class Board:
    def __init__(self):
        self.board = []
        for x in range(BOARD_SIZE[0]):
            for y in range(BOARD_SIZE[1]):
                self.board.append(random.choice(CARDS)(x, y))

    def score(self):
        used_cards = {}
        score = 0
        for card in self.board:
            score += card.score(self.board, used_cards)
            used_cards[card.card_type] = 1

        print(score)

    def mutate(self):
        pos = random.choice(range(len(self.board)))
        new_card = random.choice(CARDS)(*self.board[pos].pos)
        self.board[pos] = new_card

    def __str__(self):
        result = ""
        for idx, card in enumerate(self.board):
            tmp = str(card) + " - " + str(card.last_score)
            tmp = tmp.ljust(10)
            result += tmp + " "
            if (idx + 1) % BOARD_SIZE[0] == 0:
                result += "\n"

        return result
