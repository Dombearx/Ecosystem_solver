from __future__ import annotations

from abc import ABC, abstractmethod
from utils import CardType, WOLVES, MEADOWS, BOARD_SIZE
from typing import List, Dict


class Card(ABC):

    def __init__(self, x: int, y: int, card_type: CardType):
        self.last_score = None
        self.pos = (x, y)
        self.card_type = card_type

    @abstractmethod
    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        return 0

    def score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        self.last_score = self.calculate_score(board, used_cards)
        return self.last_score

    def __repr__(self) -> str:
        return self.card_type.name


class Rabbit(Card):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.RABBIT)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        return 1


class Wolf(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.WOLF)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        if CardType.WOLF not in used_cards.keys():
            wolf_count = sum([1 for card in board if card.card_type == CardType.WOLF])

            for wolfs, score in WOLVES.items():
                if wolf_count >= wolfs:
                    return score

        return 0


class Meadow(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.MEADOW)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        if CardType.MEADOW not in used_cards.keys():
            meadow_count = sum([1 for card in board if card.card_type == CardType.MEADOW])

            for meadows, score in MEADOWS.items():
                if meadow_count >= meadows:
                    return score

        return 0


class Deer(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.DEER)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        if CardType.DEER not in used_cards.keys():
            deers = [card for card in board if card.card_type == CardType.DEER]
            rows = {}
            columns = {}
            for x in range(BOARD_SIZE[0]):
                for y in range(BOARD_SIZE[1]):
                    for deer in deers:
                        if deer.pos == (x, y):
                            rows[x] = 1
                            columns[y] = 1
            return (sum(rows.values()) + sum(columns.values())) * 2

        return 0