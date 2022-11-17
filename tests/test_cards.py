import pytest

from cards import Rabbit


class TestRabbit:

    rabbit_data = [
        ([Rabbit(0, 0)], (0, 0), 1),
        ([Rabbit(0, 0), Rabbit(0, 0)], (0, 0), 1),
        ([Rabbit(0, 0), Rabbit(0, 1)], (0, 0), 1),
    ]

    @pytest.mark.parametrize("board, pos, score", rabbit_data)
    def test_rabbit_class(self, board, pos, score):
        main_card = None
        for card in board:
            if card.pos == pos:
                main_card = card
                break

        assert main_card is not None
        assert main_card.score(board, {}) == score
