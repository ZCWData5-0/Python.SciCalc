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

    def set_value(self, user_in): # chris' code
        try:
            self.currentValue = float(user_in)
                 # x = float(input("Enter a number:"))
               # self.currentValue = x
        except ValueError:
                self.set_value(input("please enter a number"))

    # def set_value(self): # chris' code
    #        try:
     #           if self.currentValue == 0.0:
      #              x = float(input("Enter a number:"))
       #             self.currentValue = x
        #    except ValueError:
         #       print("Please enter a number")
          #      self.set_value()




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

    def square(self):   #my code
        self.currentValue = self.currentValue * self.currentValue

    def square_root(self, x):  #my code
        self.currentValue=math.sqrt(x)
        return self.currentValue

    def factorial(self, x):
        if self.currentValue >=0:
            self.currentValue = math.factorial(x)
            return self.currentValue
        else:
            for i in range(int(self.currentValue)+1, 1):
                self.currentValue *= float(i)

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
                self.currentValue = self.currentValue - (self.currentValue * 2) #couldn't get this to work -chris abs(self)
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

    def get_sin(self, x):
        sin(x)
        self.current_value = x

    def get_cos(self, x):
        cos(x)
        self.current_value = x

    def get_tan(self, x):
        tan(x)
        self.current_value = x

    def get_asin(self, x):
        asin(x)
        self.current_value = x

    def get_acos(self, x):
        acos(x)
        self.current_value = x

    def get_atan(self, x):
        atan(x)
        self.current_value = x

    def nat_log(self, x):
        log(x)
        self.currentValue = x

    def in_nat_log(self,x):
        exp(x)
        self.currentValue= x


# add lots more methods to this calculator class.
