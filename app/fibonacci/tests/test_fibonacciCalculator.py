from django.test import TestCase
from fibonacci.utils.fibonacciCalculator import FibonacciCalculator


class TestFibonacciCalculator(TestCase):

    def setUp(self):
        self.calculator = FibonacciCalculator()

    def test_calculate_valid_numbers(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (10, 55),
            (15, 610),
            (20, 6765)
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                actual = self.calculator.calculate(n)
                self.assertEqual(actual, expected)

    def test_calculate_for_maximum_recursion_depth(self):
        with self.assertRaises(RecursionError):
            self.calculator.calculate(3000)
