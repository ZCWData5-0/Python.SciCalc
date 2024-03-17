# remember, in Python classes are easier to use than Java.
#
import unittest.mock
import math

from math import nan

from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    # def __init__(self):
    #     self.currentValue = 0.0
    #     self.trigUnitMode='degrees'     #my code
    #
    # def switchUnitsMode(self, uMode = 'none'):  #my code
    #     if uMode == 'none':
    #         if self.trigUnitMode =='degrees':
    #             self.trigUnitMode  = 'radians'
    #         else:
    #             self.trigUnitMode = 'degrees'
    #     else:
    #         self.trigUnitMode=uMode
    #
    # def getTrigUnitMode(self):
    #     return self.trigUnitMode
    # def __str__(self):
    #     return str(self.currentValue)
    #
    # def clear(self):
    #     self.currentValue = 0.0
    #
    # def value(self):
    #     return self.currentValue
    #
    # # evaluation routines
    # def add(self, x, y):
    #     self.currentValue = x + y
    #     return self.currentValue
    #
    # def sub(self, x, y):
    #     self.currentValue = x - y
    #
    # def mul(self, x, y):
    #     raise NotImplementedError
    #
    # def div(self, x, y):
    #     raise NotImplementedError

    def test_calculateSquare(self):   #my code
        c = Calculator()
        self.assertEquals(c.calculateSquare(2), 4)

    def test_calculateSquareRoot(self):  #my code
        c = Calculator()
        self.assertEquals(c.calculateSquare(4), 16)

    def test_calculateFactorial(self):
        c = Calculator()
        self.assertEquals(c.calculateFactorial(4), 24)

    def test_calculateExponent(self):
        c = Calculator()
        self.assertEquals(c.calculateExponent(4, 3), 64)

    def test_memoryAdd(self):
        c = Calculator()
        self.assertEquals(c.memoryAdd(5,5),10)

    def test_memorySub(self):
        c = Calculator()
        self.assertEquals(c.memorySub(10,5),5)

    def test_recallMemory(self):
        c = Calculator()
        c.clearMemory()
        c.setValue(10)
        c.memoryAdd(c.getMemVal(), c.value())
        self.assertEquals(c.getMemVal(), 10)
        c.memoryAdd(c.getMemVal(), c.value())
        self.assertEquals(c.getMemVal(), 20)
        c.setValue(c.recallMemory())
        self.assertEquals(c.value(),20)
# add lots more methods to this calculator class.
