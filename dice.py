

from random import randint


class Dice:
    def __init__(self, num_of_sides=6):
        self.num_of_side = num_of_sides

    def roll(self):
        return randint(1, self.num_of_side)