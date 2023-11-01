from rest_framework import serializers


class FibonacciSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=0, max_value=1000)
