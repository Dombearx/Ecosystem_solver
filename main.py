from game import Board

def main():
    board = Board()
    board.score()
    print(board)
    board.mutate()

    population_size = 100
    num_of_changes = 10000
    population = [Board() for _ in range(population_size)]

    population_with_scores = [(individual, individual.score()) for individual in population]
    population_with_scores_sorted = sorted(population_with_scores, key=lambda tup: tup[1])

    for _ in range(num_of_changes):
        new_individual = Board()
        new_individual_with_score = (new_individual, -1)
        population_with_scores_sorted[0] = new_individual_with_score
        [individual.mutate for individual, _ in population_with_scores_sorted]
        population_with_scores = [(individual, individual.score()) for individual, _ in population_with_scores_sorted]
        population_with_scores_sorted = sorted(population_with_scores, key=lambda tup: tup[1])
        print(population_with_scores_sorted[-1])




if __name__ == "__main__":
    main()
