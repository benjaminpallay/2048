import random


def random_strategy(game):
    return random.choice("ldur")


def two_directions_strategy(game):

    opposites = {"r": "l", "l": "r", "u": "d", "d": "u"}
    default_direction = "r"
    second_direction = "d"
    order = [default_direction, second_direction, opposites[default_direction],
             opposites[second_direction]]
    allowed_directions = [dir for dir in "ldur" if game.allowed_move(dir)]

    for dir in order:
        if dir in allowed_directions:
            return dir