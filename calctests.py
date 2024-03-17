import unittest
from lydias_calculator import Calculator
import sys

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        c.add(3,3)
        self.assertEqual(c.currentValue, 6)

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
        c.common_log(100)
        self.assertEqual(c.currentValue, 2)

    def test_common_log_max(self):
        c = Calculator()
        c.common_log(sys.maxsize)
        self.assertEqual(c.currentValue, sys.maxsize)

    def test_common_log_none(self):
        c = Calculator()
        self.assertEqual(c.common_log(0), None)

    def test_inverse_common_log_zero(self):
        c = Calculator()
        self.assertEqual(c.inverse_common_log(0), 1)

    def test_inverse_common_log_one(self):
        c = Calculator()
        self.assertEqual(c.common_log(1), 10)

    def test_inverse_common_log_max(self):
        c = Calculator()
        self.assertEqual(c.common_log(sys.maxsize), sys.maxsize)

    def test_multiplicative_inverse_of_a_number_five(self):
        c = Calculator()
        self.assertEqual(c.common_log(5), 0.2)

    def test_multiplicative_inverse_of_a_number_zero(self):
        c = Calculator()
        self.assertEqual(c.common_log(0), None)

    def test_multiplicative_inverse_of_a_number_negative(self):
        c = Calculator()
        self.assertEqual(c.common_log(-5), -0.2)

    def test_inverse_of_a_number_five(self):
        c = Calculator()
        self.assertEqual(c.common_log(5), -5)

    def test_inverse_of_a_number_negative_five(self):
        c = Calculator()
        self.assertEqual(c.common_log(-5), 5)

    def test_inverse_of_a_number_zero(self):
        c = Calculator()
        self.assertEqual(c.common_log(0), None)

    def test_save_to_memory(self):
        c = Calculator()
        c.add(2,2)
        c.save_to_memory()
        self.assertEqual(c.stored_value,4)

    def test_reset_memory(self):
        c = Calculator()
        c.add(2,2)
        c.save_to_memory()
        c.reset_memory()
        self.assertEqual(c.stored_value,0)

    def test_recall_from_memory(self):
        c = Calculator()
        c.add(2, 2)
        c.save_to_memory()
        c.add(5, 5)
        c.recall_from_memory()
        self.assertEqual(c.currentValue, 4)


if __name__ == '__main__':
    unittest.main()
