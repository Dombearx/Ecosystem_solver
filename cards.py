from __future__ import annotations

from abc import ABC, abstractmethod
from utils import CardType, WOLVES, MEADOWS, BOARD_SIZE, RIVERS
from typing import List, Dict
from collections import defaultdict


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


class Bee(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.BEE)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        changes = (-1, 1)
        score = 0
        x, y = self.pos
        for change in changes:
            for card in board:
                if card.pos == (x + change, y):
                    if card.card_type == CardType.MEADOW:
                        score += 3
                if card.pos == (x, y + change):
                    if card.card_type == CardType.MEADOW:
                        score += 3

        return score


class River(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.RIVER)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        if CardType.RIVER not in used_cards.keys():
            rivers = [card for card in board if card.card_type == CardType.RIVER]
            longest_river = self.find_longest_river(rivers)

            for rivers, score in RIVERS.items():
                if longest_river >= rivers:
                    return score

        return 0

    def find_longest_river(self, rivers: List[Card]) -> int:
        longest_river = 0
        for river in rivers:
            pass
        raise NotImplementedError()


class Fish(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.FISH)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        changes = (-1, 1)
        score = 0
        x, y = self.pos
        for change in changes:
            for card in board:
                if card.pos == (x + change, y):
                    if card.card_type in (CardType.RIVER, CardType.DRAGONFLY):
                        score += 2
                if card.pos == (x, y + change):
                    if card.card_type in (CardType.RIVER, CardType.DRAGONFLY):
                        score += 2

        return score


class Bear(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.BEAR)

    def calculate_score(self, board: List[Card], used_cards: Dict[CardType, int]) -> int:
        changes = (-1, 1)
        score = 0
        x, y = self.pos
        for change in changes:
            for card in board:
                if card.pos == (x + change, y):
                    if card.card_type in (CardType.BEE, CardType.FISH):
                        score += 2
                if card.pos == (x, y + change):
                    if card.card_type in (CardType.BEE, CardType.FISH):
                        score += 2

        return score
