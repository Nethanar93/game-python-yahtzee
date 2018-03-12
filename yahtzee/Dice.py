from random import randint

class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = randint(1, 7)

    def get_value(self):
        return self.value