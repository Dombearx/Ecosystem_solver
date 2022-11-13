from abc import ABC, abstractmethod
from utils import CardType


class Card(ABC):

    def __init__(self, x, y, type):
        self.last_score = None
        self.pos = (x, y)
        self.type = type

    @abstractmethod
    def calculate_score(self, board, used_cards):
        return 0

    def score(self, board, used_cards):
        self.last_score = self.calculate_score(board, used_cards)
        return self.last_score

    def __repr__(self):
        return self.type.name


class Rabbit(Card):

    def __init__(self, x, y):
        super().__init__(x, y, CardType.RABBIT)

    def calculate_score(self, board, used_cards):
        return 1
