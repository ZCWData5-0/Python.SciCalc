# remember, in Python classes are easier to use than Java.
#
from math import nan


class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.currentMsg = ""

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
        self.currentValue = x * y

    def div(self, x, y):
        try:
            value = x / y
            self.currentValue = value
        except ZeroDivisionError:
            # TODO Make sure calling functions know how to handle a None value
            # TODO Consider logging the error, if a logger is defined
            self.currentValue = None
            self.currentMsg = "DIV BY ZERO"



# add lots more methods to this calculator class.
