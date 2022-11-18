def board_creator(cards):
    board = {}
    for pos, card in cards:
        board[pos] = card(*pos)

    return board
