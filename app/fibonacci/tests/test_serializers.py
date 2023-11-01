from django.test import TestCase
from fibonacci.serializers import FibonacciSerializer


class FibonacciSerializerTestCase(TestCase):

    def test_valid_serializer(self):
        data = {"n": 5}
        serializer = FibonacciSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer_less_than_min_value(self):
        data = {"n": -1}
        serializer = FibonacciSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("n", serializer.errors)
        self.assertIn("Ensure this value is greater than or equal to 0.",
                      serializer.errors["n"]
                      )

    def test_invalid_serializer_greater_than_max_value(self):
        data = {"n": 1001}
        serializer = FibonacciSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("n", serializer.errors)
        self.assertIn("Ensure this value is less than or equal to 1000.",
                      serializer.errors["n"]
                      )
