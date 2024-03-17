# remember, in Python classes are easier to use than Java.
#
import math
from math import nan
from math import *

class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.currentMsg = ""
        self.stored_value = 0.0
        self.trigUnitMode='degrees'     #my code

    def switchUnitsMode(self, uMode = 'none'):  #my code
        if uMode == 'none':
            if self.trigUnitMode =='degrees':
                self.trigUnitMode  = 'radians'
            else:
                self.trigUnitMode = 'degrees'
        else:
            self.trigUnitMode=uMode

    def getTrigUnitMode(self):
        return self.trigUnitMode
    def __str__(self):
        return str(self.currentValue)

    def set_value(self): # chris' code
            try:
                if self.currentValue == 0.0:
                    x = float(input("Enter a number:"))
                    self.currentValue = x
            except ValueError:
                print("Please enter a number")
                self.set_value()




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
        self.currentValue = x * y

    def div(self, x, y):
        try:
            value = x / y
            self.currentValue = value
        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'DIV BY ZERO'

    def square(self, x):   #my code
        self.currentValue = x*x
        return self.currentValue

    def square_root(self, x):  #my code
        self.currentValue=math.sqrt(x)
        return self.currentValue

    def factorial(self, x):
        self.currentValue = math.factorial(x)
        return self.currentValue

    def common_log(self, x):
        try:
            self.currentValue = math.log10(x)
        except ValueError:
            if x <= 0:
                self.currentValue = None
                self.currentMsg = 'NEG NUM ERROR'

    def inverse_common_log(self, x):
        self.currentValue = math.pow(10, x)

    def multiplicative_inverse(self):
        try:
            self.currentValue = 1 / self
        except ZeroDivisionError:
            if self == 0:
                self.currentValue = None
                self.currentMsg = 'DIV BY ZERO'

    def inverse_of_number(self):
        try:
            if self != 0:
                self.currentValue = abs(self)
        except ValueError:
            if self == 0:
                self.currentValue = None
                self.currentMsg = 'ZERO INVALID'

    def save_to_memory(self):
        self.stored_value = self.currentValue

    def reset_memory(self):
        self.stored_value = 0.0

    def recall_from_memory(self):
        self.currentValue = self.stored_value

# add lots more methods to this calculator class.
