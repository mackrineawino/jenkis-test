import unittest
from addition import add_numbers, subtraction

class TestAddNumbers(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(3, 2)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtraction(3, 2)
        self.assertEqual(result, 1)
    