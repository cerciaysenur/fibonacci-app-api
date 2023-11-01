from fibonacci.utils.fibonacciCalculator import FibonacciCalculator
from fibonacci.cache.cache_interface import CacheInterface


class CachedFibonacci:

    def __init__(self, calculator: FibonacciCalculator, cache: CacheInterface):
        self.calculator = calculator
        self.cache = cache

    def calculate(self, n: int):
        cached_value = self.cache.get(f"fib_{n}")
        if cached_value:
            return int(cached_value)

        value = self.calculator.calculate(n)
        self.cache.set(f"fib_{n}", value)
        return value
