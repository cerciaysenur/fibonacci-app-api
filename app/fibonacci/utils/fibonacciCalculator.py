class FibonacciCalculator:
    def calculate(self, n: int):
        if n <= 1:
            return n
        else:
            return self.calculate(n-1) + self.calculate(n-2)
