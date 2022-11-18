def board_creator(human_board):
    board = {}

    for row_id, row in enumerate(human_board):
        for column_id, card in enumerate(row):
            board[(row_id, column_id)] = card(row_id, column_id)

    return board
