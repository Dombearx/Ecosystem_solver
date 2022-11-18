from game import Board


def main():
    board = Board()
    board.score()
    print(board)
    board.mutate()

    population_size = 0
    population = [Board() for _ in range(population_size)]


if __name__ == "__main__":
    main()
