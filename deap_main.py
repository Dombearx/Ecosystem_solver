import random
from deap import creator, base, tools, algorithms
from game import Board
from typing import Tuple

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", Board, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", creator.Individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluate_individual(individual: Board) -> int:
    return individual.score()

def crossover(individual: Board, other: Board) -> Tuple[Board, Board]:
    other = individual.crossover(other)
    return individual, other

def mutate(individual: Board) -> Tuple[Board]:
    individual.mutate()
    return individual,

toolbox.register("evaluate", evaluate_individual)
toolbox.register("mate", crossover)
toolbox.register("mutate", mutate)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=300)

NGEN = 400
for gen in range(NGEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
top1 = tools.selBest(population, k=1)[0]
print(top1.fitness)