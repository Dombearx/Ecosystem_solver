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


class TestBee:
    data = [
        (board_creator([[Bee]]), (0, 0), 0),
        (board_creator([[Bee, Deer]]), (0, 0), 0),
        (board_creator([[Bee, Meadow]]), (0, 0), 3),
        (board_creator([[Bee, Meadow, Bee]]), (0, 0), 3),
        (board_creator([[Meadow, Bee, Meadow]]), (0, 1), 6),
        (board_creator([[Bee, Meadow], [Meadow, Bee]]), (0, 0), 6)
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_bee_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestRiver:
    data = [
        (board_creator([[River]]), (0, 0), 0),
        (board_creator([[River, River]]), (0, 0), 0),
        (board_creator([[River, River, River]]), (0, 0), 5),
        (board_creator([[River], [River], [River]]), (0, 0), 5),
        (board_creator([[River, Meadow, River], [River, Meadow, River]]), (0, 0), 0),
        (board_creator([[River, Meadow, River], [River, River, River]]), (0, 0), 8),
        (board_creator([[River, Meadow, Meadow], [River, River, River], [River, Meadow, Meadow]]), (0, 0), 8),
        (board_creator([[River, Meadow, Meadow], [River, River, Meadow], [River, Meadow, Meadow]]), (0, 0), 5),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_river_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestFish:
    data = [
        (board_creator([[Fish]]), (0, 0), 0),
        (board_creator([[Fish, River]]), (0, 0), 2),
        (board_creator([[River, Fish, River]]), (0, 1), 4),
        (board_creator([[River, Fish, Dragonfly]]), (0, 1), 4),
        (board_creator([[Dragonfly, Fish, Dragonfly]]), (0, 1), 4),
        (board_creator([[Dragonfly, Fish, Dragonfly], [Dragonfly, Fish, Dragonfly]]), (0, 1), 4),
        (board_creator([[Dragonfly, Fish, Dragonfly], [Dragonfly, River, Dragonfly]]), (0, 1), 6),
        (board_creator([[Meadow, Fish, Meadow], [Meadow, Wolf, Meadow]]), (0, 1), 0)
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_fish_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestBear:
    data = [
        (board_creator([[Bear]]), (0, 0), 0),
        (board_creator([[Bear, Fish]]), (0, 0), 2),
        (board_creator([[Fish, Bear, Fish]]), (0, 1), 4),
        (board_creator([[Fish, Bear, Bee]]), (0, 1), 4),
        (board_creator([[Bee, Bear, Bee]]), (0, 1), 4),
        (board_creator([[Bee, Bear, Bee], [Bee, Bear, Bee]]), (0, 1), 4),
        (board_creator([[Bee, Bear, Bee], [Bee, Fish, Bee]]), (0, 1), 6),
        (board_creator([[Meadow, Bear, Meadow], [Meadow, Wolf, Meadow]]), (0, 1), 0)
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_bear_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestDragonfly:
    data = [
        (board_creator([[Dragonfly]]), (0, 0), 0),
        (board_creator([[Dragonfly, River]]), (0, 0), 1),
        (board_creator([[Dragonfly, River, River]]), (0, 0), 2),
        (board_creator([[Dragonfly, River], [Meadow, River]]), (0, 0), 2),
        (board_creator([[River, River], [Dragonfly, River], [Meadow, River]]), (1, 0), 4),
        (board_creator([[River, Meadow], [River, River], [Dragonfly, River]]), (1, 0), 4),
        (board_creator([[River, River], [River, River], [Meadow, Dragonfly]]), (2, 1), 4),
        (board_creator([[River, Dragonfly, River]]), (0, 1), 2),
        (board_creator([[River, Dragonfly, River], [Meadow, River, River]]), (0, 1), 4),
        (board_creator([[River, Dragonfly, Meadow], [River, River, River], [River, Meadow, Meadow]]), (0, 1), 5),
        (board_creator([[Meadow, River, Meadow], [River, River, River], [Meadow, River, Meadow], [Meadow, Dragonfly, Meadow]]), (3, 1), 3),
        (board_creator([[Meadow, River, Meadow, Meadow], [River, River, River, River], [Meadow, River, Meadow, Meadow], [Meadow, Dragonfly, Meadow, Meadow]]), (3, 1), 4),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_dragonfly_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestEagle:
    data = [
        (board_creator([[Eagle]]), (0, 0), 0),
        (board_creator([[Eagle, Fish]]), (0, 0), 2),
        (board_creator([[Fish, Eagle, Fish]]), (0, 1), 4),
        (board_creator([[Fish, Eagle, Rabbit]]), (0, 1), 4),
        (board_creator([[Rabbit, Eagle, Rabbit]]), (0, 1), 4),
        (board_creator([[Rabbit, Eagle, Rabbit], [Rabbit, Bear, Rabbit]]), (0, 1), 8),
        (board_creator([[Rabbit, Eagle, Rabbit], [Rabbit, Fish, Rabbit]]), (0, 1), 10),
        (board_creator([[Meadow, Eagle, Meadow], [Meadow, Wolf, Meadow]]), (0, 1), 0),
        (board_creator([[Meadow, Eagle, Meadow], [Fish, Wolf, Rabbit]]), (0, 1), 4),
        (board_creator([[Eagle, Meadow, Fish]]), (0, 0), 2),
        (board_creator([[Eagle, Meadow, Fish], [Meadow, Meadow, Fish]]), (0, 0), 2),
        (board_creator([[Eagle, Meadow, Fish], [Meadow, Fish, Fish]]), (0, 0), 4),
        (board_creator([[Eagle, Meadow, Fish], [Fish, Meadow, Fish]]), (0, 0), 4),
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_eagle_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score


class TestFox:
    data = [
        (board_creator([[Fox]]), (0, 0), 3),
        (board_creator([[Fox, Bear]]), (0, 0), 0),
        (board_creator([[Fox, Wolf]]), (0, 0), 0),
        (board_creator([[Fox, Meadow, Wolf]]), (0, 0), 3),
        (board_creator([[Meadow, Fox, Wolf]]), (0, 1), 0),
        (board_creator([[Bear, Fox, Meadow]]), (0, 1), 0),
        (board_creator([[Bear, Fox, Wolf]]), (0, 1), 0),
        (board_creator([[Fox, Meadow], [Wolf, Meadow]]), (0, 0), 0),
        (board_creator([[Fox, Meadow], [Bear, Meadow]]), (0, 0), 0),
        (board_creator([[Fox, Meadow], [Meadow, Bear]]), (0, 0), 3)
    ]

    @pytest.mark.parametrize("board, pos, score", data)
    def test_eagle_score(self, board, pos, score):
        main_card = board[pos]

        assert main_card is not None
        assert main_card.score(board, {}) == score