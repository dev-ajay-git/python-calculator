from src.calculator import Calculator  # Update import to match the directory structure

import unittest

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == '__main__':
    unittest.main()

