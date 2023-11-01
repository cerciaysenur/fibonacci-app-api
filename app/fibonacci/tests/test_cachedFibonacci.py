from django.test import TestCase
from unittest.mock import Mock
from fibonacci.utils.cachedFibonacci import CachedFibonacci


class TestCachedFibonacci(TestCase):

    def setUp(self):
        self.calculator_mock = Mock()
        self.cache_mock = Mock()
        self.cached_fib = CachedFibonacci(
            self.calculator_mock,
            self.cache_mock
        )

    def test_calculate_returns_cached_value(self):
        self.cache_mock.get.return_value = "21"

        result = self.cached_fib.calculate(8)
        self.assertEqual(result, 21)
        self.calculator_mock.calculate.assert_not_called()

    def test_calculate_calculates_and_caches_value(self):
        self.cache_mock.get.return_value = None
        self.calculator_mock.calculate.return_value = 21

        result = self.cached_fib.calculate(8)
        self.assertEqual(result, 21)
        self.cache_mock.set.assert_called_once_with("fib_8", 21)
