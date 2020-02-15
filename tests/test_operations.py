# python -m unittest tests.test_operations
import unittest
from src.arithmetic import Arithmetic

class TestArithmeticOperations(unittest.TestCase):

    def setUp(self):
        self.arith = Arithmetic(6,4)

    def test_addition(self):
        self.assertEqual(self.arith.addition(),10)

    def test_subtraction(self):
        self.assertEqual(self.arith.subtraction(),2)

    def test_multiplication(self):
        self.assertEqual(self.arith.multiplication(),24)

    def test_division(self):
        self.assertEqual(self.arith.division(),1.5)

if __name__ == "__main__":
    unittest.main()

