import unittest
from calculator import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):

    def test_add_numbers(self):
        result = add([1, 2, 3])
        self.assertEqual(result, 6)

    def test_subtract_numbers(self):
        result = subtract([50, 25, 5])
        self.assertEqual(result, 20)

    def test_multiply_numbers(self):
        result = multiply([2, 4, 8])
        self.assertEqual(result, 64)

    def test_divide_numbers(self):
        result = divide([20, 2, 5])
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
    


