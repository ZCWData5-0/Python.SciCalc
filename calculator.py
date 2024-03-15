# remember, in Python classes are easier to use than Java.
#
from math import nan


class Calculator:

    def __init__(self):
        self.currentValue = 0.0

    def __str__(self):
        return str(self.currentValue)

    def clear(self):
        self.currentValue = 0.0

    def value(self):
        return self.currentValue

    # evaluation routines
    def add(self, x, y):
        self.currentValue = x + y

    def sub(self, x, y):
        self.currentValue = x - y

    def mul(self, x, y):
        raise NotImplementedError

    def div(self, x, y):
        raise NotImplementedError


# add lots more methods to this calculator class.
