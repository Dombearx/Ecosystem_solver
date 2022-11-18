import pytest

from cards import *
from utils import board_creator


class TestRabbit:
    data = [
        (board_creator([[Rabbit]]), (0, 0), 1),
        (board_creator([[Rabbit, Rabbit], [Rabbit, Rabbit]]), (0, 0), 1),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_rabbit_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestWolf:
    data = [
        (board_creator([[Wolf]]), (0, 0), 4),
        (board_creator([[Wolf, Wolf]]), (0, 0), 8),
        (board_creator([[Wolf, Rabbit]]), (0, 0), 4),
        (board_creator([[Wolf, Rabbit], [Wolf, Wolf]]), (0, 0), 12),
        (board_creator([[Wolf, Wolf], [Wolf, Wolf]]), (0, 0), 12),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_wolf_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestMeadow:
    data = [
        (board_creator([[Meadow]]), (0, 0), 0),
        (board_creator([[Meadow, Wolf]]), (0, 0), 0),
        (board_creator([[Meadow, Meadow]]), (0, 0), 3),
        (board_creator([[Meadow, Meadow], [Meadow, Wolf]]), (0, 0), 6),
        (board_creator([[Meadow, Meadow], [Meadow, Meadow]]), (0, 0), 10),
        (board_creator([[Meadow, Meadow], [Meadow, Wolf], [Meadow, Meadow]]), (0, 0), 15),
        (board_creator([[Meadow, Meadow], [Meadow, Meadow], [Meadow, Meadow]]), (0, 0), 15),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_meadow_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestDeer:
    data = [
        (board_creator([[Deer]]), (0, 0), 4),
        (board_creator([[Deer, Deer]]), (0, 0), 6),
        (board_creator([[Deer, Wolf]]), (0, 0), 4),
        (board_creator([[Deer, Meadow], [Meadow, Deer]]), (0, 0), 8),
        (board_creator([[Deer, Deer], [Deer, Deer]]), (0, 0), 8),
        (board_creator([[Deer, Deer, Deer], [Meadow, Wolf], [Meadow, Meadow]]), (0, 0), 8),
        (board_creator([[Deer, Meadow], [Meadow, Deer], [Meadow, Meadow, Deer]]), (0, 0), 12),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_deer_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score
