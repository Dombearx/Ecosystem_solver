import pytest

from cards import *
from utils import board_creator


class TestRabbit:
    data = [
        (board_creator([((0, 0), Rabbit)]), (0, 0), 1),
        (board_creator([((0, 0), Rabbit), ((0, 0), Rabbit)]), (0, 0), 1),
        (board_creator([((0, 0), Rabbit), ((0, 1), Rabbit)]), (0, 0), 1),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_rabbit_class(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestWolf:
    data = [
        (board_creator([((0, 0), Wolf)]), (0, 0), 4),
        (board_creator([((0, 0), Wolf), ((0, 0), Wolf)]), (0, 0), 4),
        (board_creator([((0, 0), Wolf), ((0, 1), Wolf)]), (0, 0), 8),
        (board_creator([((0, 0), Wolf), ((0, 1), Rabbit)]), (0, 0), 4),
        (board_creator([((0, 0), Wolf), ((0, 1), Rabbit), ((1, 0), Wolf), ((1, 1), Wolf)]), (0, 0), 12),
        (board_creator([((0, 0), Wolf), ((0, 1), Wolf), ((1, 0), Wolf), ((1, 1), Wolf)]), (0, 0), 12),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_wolf_class(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score
