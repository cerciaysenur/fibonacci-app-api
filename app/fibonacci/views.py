from rest_framework.views import APIView
from fibonacci.utils.fibonacciCalculator import FibonacciCalculator
from fibonacci.cache.redis_cache import RedisCache
from fibonacci.serializers import FibonacciSerializer
from fibonacci.utils.cachedFibonacci import CachedFibonacci
from django.http import HttpResponse


class FibonacciView(APIView):
    def get(self, request, n):
        serializer = FibonacciSerializer(data={'n': n})
        if serializer.is_valid():
            n = serializer.validated_data['n']
            fib_calculator = FibonacciCalculator()
            cache_instance = RedisCache()
            cached_fib = CachedFibonacci(
                calculator=fib_calculator,
                cache=cache_instance
            )
            result = cached_fib.calculate(n)
            return HttpResponse(str(result) + "\n")
        return HttpResponse(serializer.errors, status=400)
