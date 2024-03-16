import unittest
from lydias_calculator import Calculator
import sys

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(c.add(3, 3), 6)

    def test_add2(self):
        c = Calculator()
        self.assertEqual(c.add(12, -10), 2)

    def test_add3(self):
        c = Calculator()
        self.assertEqual(c.add(5, 8), 13)

    def test_sub(self):
        c = Calculator()
        self.assertEqual(c.sub(9, 3), 6)

    def test_common_log(self):
        c = Calculator()
        self.assertEqual(c.common_log(100), 2)

    def test_common_log_max(self):
        c = Calculator()
        self.assertEqual(c.common_log(sys.maxsize), sys.maxsize)

    def test_common_log_none(self):
        c = Calculator()
        self.assertEqual(c.common_log(0), None)

    def inverse_common_log_zero(self):
        c = Calculator()
        self.assertEqual(c.common_log(0), 1)

    def inverse_common_log_one(self):
        c = Calculator()
        self.assertEqual(c.common_log(1), 10)

    def inverse_common_log_max(self):
        c = Calculator()
        self.assertEqual(c.common_log(sys.maxsize), sys.maxsize)


if __name__ == '__main__':
    unittest.main()
