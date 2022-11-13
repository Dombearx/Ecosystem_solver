from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, x, y):
        self.last_score = None
        self.pos = (x, y)
        self.type = None

    @abstractmethod
    def calculate_score(self, board, used_cards):
        return 0

    def score(self, board, used_cards):
        self.last_score = self.calculate_score(board, used_cards)
        return self.last_score

    def __repr__(self):
        return self.type.name
