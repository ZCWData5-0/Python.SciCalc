# remember, in Python classes are easier to use than Java.
#
import math
from math import nan


class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.trigUnitMode='degrees'
        self.memVal = 0.0      #my code

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

    def clear(self):
        self.currentValue = 0.0

    def value(self):
        return self.currentValue


    def getMemVal(self):
        return self.memVal

    def setValue(self,x):
        self.currentValue = x
        #return self.currentValue



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

    def calculateSquare(self, x):   #my code
        self.currentValue= x * x
        return self.currentValue

    def calculateSquareRroot(self, x):  #my code
        self.currentValue=math.sqrt(x)
        return self.currentValue

    def calculateFactorial(self, x):
        self.currentValue = math.factorial(x)
        return self.currentValue

    def calculateExponent(self, b, p):
        self.currentValue = b**p
        return self.currentValue

    def memoryAdd(self, x, y):
        self.memVal = x + y
        return self.memVal

    def memorySub(self , x,y):
        self.memVal = x -y
        return self.memVal

    def recallMemory(self):
        return self.memVal


    def clearMemory(self):
        self.memVal = 0.0
# add lots more methods to this calculator class.
