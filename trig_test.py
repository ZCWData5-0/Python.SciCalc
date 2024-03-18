import unittest
from calculator import Calculator
from calculator import *
import sys


class TestStringMethods(unittest.TestCase):

    def test_sin(self):
        c = Calculator()
        # given
        expected = 0.9092974268256817
        # when
        c.set_value(2)

        actual = c.get_sin(c.currentValue)
        # then
        self.assertEqual(expected, actual)  # changed function to test numbers - chris

    def test_cos(self):
        c = Calculator()
        # given
        expected = -0.4161468365471424
        # when
        c.set_value(2)

        actual = c.get_cos(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_tan(self):
        c = Calculator()
        # given
        expected = -2.185039863261519
        # when
        c.set_value(2)

        actual = c.get_tan(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_asin(self):
        c = Calculator()
        # given
        expected = 1.5707963267948966
        # when
        c.set_value(1)

        actual = c.get_asin(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_acos(self):
        c = Calculator()
        # given
        expected = 2
        # when
        c.set_value(-0.4161468365471424)

        actual = c.get_acos(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_atan(self):
        c = Calculator()
        # given
        expected = 1.1071487177940906
        # when
        c.set_value(2)

        actual = c.get_atan(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_nat_log(self):
        c = Calculator()
        # given
        expected = 0.6931471805599453
        # when
        c.set_value(2)

        actual = c.nat_log(c.currentValue)
        # then
        self.assertEqual(expected, actual)

    def test_in_nat_log(self):
        c = Calculator()
        # given
        expected = 7.38905609893065
        # when
        c.set_value(2)

        actual = c.in_nat_log(c.currentValue)
        # then
        self.assertEqual(expected, actual)