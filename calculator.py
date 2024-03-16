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
        self.currentValue = x * y
        #raise NotImplementedError

    def div(self, x, y):
        self.currentValue = x / y
        #raise NotImplementedError

    def clear(self, x, y):
        self.delete(0, 999)
        #youtube code was: txtDisplay.delete(0, END)

    def clear_all(self, x, y):
        #clear text display (TEST THIS!)
        self.delete(0, 999)
        #youtube code was: txtDisplay.delete(0, END)

        #reinitialize all variables
        #global first_number, second_number, Operation, Final_answer
        #first_number = 0
        #second_number = 0
        #Operation = 0
        #Final_answer = 0

# add lots more methods to this calculator class.
