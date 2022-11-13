from enum import Enum


class CardType(Enum):
    RABBIT = "Rabbit"
    WOLF = "Wolf"
    MEADOW = "meadow"
    DEER = "Deer"
    BEE = "Bee"
    RIVER = "River"
    EAGLE = "Eagle"
    BEAR = "Bear"
    FISH = "Fish"
    DRAGONFLY = "Dragonfly"
    FOX = "Fox"

BOARD_SIZE = (5, 4)

WOLVES = {3: 12,
          2: 8,
          1: 4}

RIVERS = {4: 8,
          2: 5
          }

MEADOWS = {
    5: 15,
    4: 10,
    3: 6,
    2: 3
}