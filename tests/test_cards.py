import pytest

from cards import *
from utils import board_creator


class TestRabbit:
    data = [
        (board_creator([[Rabbit]]), (0, 0), 1),

        (board_creator([[Rabbit, Rabbit],
                        [Rabbit, Rabbit]]), (0, 0), 1),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_rabbit_class(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestWolf:
    data = [
        (board_creator([[Wolf]]), (0, 0), 4),

        (board_creator([[Wolf, Wolf]]), (0, 0), 8),

        (board_creator([[Wolf, Rabbit]]), (0, 0), 4),

        (board_creator([[Wolf, Rabbit],
                        [Wolf, Wolf]]), (0, 0), 12),

        (board_creator([[Wolf, Wolf],
                        [Wolf, Wolf]]), (0, 0), 12),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_wolf_class(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score
