# remember, in Python classes are easier to use than Java.
#
import math
from math import nan


class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.trigUnitMode='degrees'     #my code

    def switchUnitsMode(self, uMode = 'none'):  #my code
        if uMode == 'none':
            if self.trigUnitMode =='degrees':
                self.trigUnitMode  = 'radians'
            else:
                self.trigUnitMode = 'degrees'
        else:
            self.trigUnitMode=uMode

    def set_value(self):
        if self.currentValue == 0.0:
            x = float(input("Enter a value:"))
            self.currentValue = x

    def getTrigUnitMode(self):
        return self.trigUnitMode
    def __str__(self):
        return str(self.currentValue)

    def clear(self):
        self.currentValue = 0.0

    def value(self):
        return self.currentValue

    # evaluation routines
    def add(self, x, y):
        self.currentValue = x + y
        return self.currentValue

    def sub(self, x, y):
        self.currentValue = x - y

    def mul(self, x, y):
        raise NotImplementedError

    def div(self, x, y):
        raise NotImplementedError

    def square(self):   #my code
        self.currentValue*=self.currentValue
        return self.currentValue

    def square_root(self):  #my code
        self.currentValue=math.sqrt(self.currentValue)
        return self.currentValue

    def factorial(self):
        self.currentValue = math.factorial(self.currentValue)
        return self.currentValue


# add lots more methods to this calculator class.
