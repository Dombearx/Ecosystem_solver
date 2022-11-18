from __future__ import annotations

from abc import ABC, abstractmethod
from consts import WOLVES, MEADOWS, BOARD_SIZE, RIVERS
from typing import List, Dict, Tuple
from collections import defaultdict
from enum import Enum


class CardType(Enum):
    RABBIT = "Rabbit"
    WOLF = "Wolf"
    MEADOW = "meadow"
    DEER = "Deer"
    BEE = "Bee"
    RIVER = "River"
    EAGLE = "Eagle"
    BEAR = "Bear"
    FISH = "Fish"
    DRAGONFLY = "Dragonfly"
    FOX = "Fox"


class Card(ABC):
    def __init__(self, x: int, y: int, card_type: CardType):
        self.last_score = None
        self.pos = (x, y)
        self.card_type = card_type

    @abstractmethod
    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        return 0

    def score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        self.last_score = self.calculate_score(board, used_cards)
        return self.last_score

    def __repr__(self) -> str:
        return self.card_type.name


class Rabbit(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.RABBIT)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        return 1


class Wolf(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.WOLF)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        if CardType.WOLF not in used_cards.keys():
            wolf_count = sum(
                [1 for card in board.values() if card.card_type == CardType.WOLF]
            )

            for wolfs, score in WOLVES.items():
                if wolf_count >= wolfs:
                    return score

        return 0


class Meadow(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.MEADOW)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        if CardType.MEADOW not in used_cards.keys():
            meadow_count = sum(
                [1 for card in board.values() if card.card_type == CardType.MEADOW]
            )

            for meadows, score in MEADOWS.items():
                if meadow_count >= meadows:
                    return score

        return 0


class Deer(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.DEER)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        if CardType.DEER not in used_cards.keys():
            deers = [card for card in board.values() if card.card_type == CardType.DEER]
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

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        score = 0
        x, y = self.pos
        for card in board.values():
            if card.card_type == CardType.MEADOW:
                card_x, card_y = card.pos
                distance = abs(x - card_x) + abs(y - card_y)
                if distance <= 1:
                    score += 3

        return score


class River(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.RIVER)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        if CardType.RIVER not in used_cards.keys():
            rivers = [
                card for card in board.values() if card.card_type == CardType.RIVER
            ]
            longest_river = self.find_longest_river(rivers)

            for rivers, score in RIVERS.items():
                if longest_river >= rivers:
                    return score

        return 0

    def find_longest_river(self, rivers: List[Card]) -> int:
        if len(rivers) == 0:
            return 0
        graph = defaultdict(list)
        for river in rivers:
            for other_river in rivers:
                card_x, card_y = other_river.pos
                distance = abs(river.pos[0] - card_x) + abs(river.pos[1] - card_y)
                if distance == 1:
                    graph[river].append(other_river)
                    graph[other_river].append(river)

        all_paths = self.dfs(graph, rivers[0])
        if len(all_paths) == 0:
            return 1
        max_len = max(len(p) for p in all_paths)

        return max_len

    def dfs(self, graph, v, seen=None, path=None):
        if seen is None:
            seen = []
        if path is None:
            path = [v]

        seen.append(v)

        paths = []
        for t in graph[v]:
            if t not in seen:
                t_path = path + [t]
                paths.append(tuple(t_path))
                paths.extend(self.dfs(graph, t, seen[:], t_path))
        return paths


class Fish(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.FISH)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        score = 0
        x, y = self.pos
        for card in board.values():
            if card.card_type in (CardType.RIVER, CardType.DRAGONFLY):
                card_x, card_y = card.pos
                distance = abs(x - card_x) + abs(y - card_y)
                if distance <= 1:
                    score += 2

        return score


class Bear(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.BEAR)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        score = 0
        x, y = self.pos
        for card in board.values():
            if card.card_type in (CardType.BEE, CardType.FISH):
                card_x, card_y = card.pos
                distance = abs(x - card_x) + abs(y - card_y)
                if distance <= 1:
                    score += 2

        return score


class Dragonfly(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.DRAGONFLY)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        changes = (-1, 1)
        score = 0
        x, y = self.pos
        connected_rivers = []
        for change in changes:
            for card in board.values():
                if card.pos == (x + change, y):
                    if card.card_type == CardType.RIVER:
                        connected_rivers.append(card)
                if card.pos == (x, y + change):
                    if card.card_type == CardType.RIVER:
                        connected_rivers.append(card)

        raise NotImplementedError


class Eagle(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.EAGLE)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        score = 0
        x, y = self.pos
        for card in board.values():
            if card.card_type in (CardType.RABBIT, CardType.FISH):
                card_x, card_y = card.pos
                distance = abs(x - card_x) + abs(y - card_y)
                if distance <= 2:
                    score += 2

        return score


class Fox(Card):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, CardType.FOX)

    def calculate_score(
        self, board: Dict[Tuple[int, int], Card], used_cards: Dict[CardType, int]
    ) -> int:
        x, y = self.pos
        for card in board.values():
            if card.card_type in (CardType.WOLF, CardType.BEAR):
                card_x, card_y = card.pos
                distance = abs(x - card_x) + abs(y - card_y)
                if distance <= 1:
                    return 0

        return 3
