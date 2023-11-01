from django.test import SimpleTestCase
from rest_framework.test import APIClient
from django.urls import reverse


def fibonacci_url(n):
    return reverse('fibonacci', kwargs={'n': n})


class FibonacciIntegrationTest(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_valid_fibonacci_request(self):
        response = self.client.get(fibonacci_url(7))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "13\n")

    def test_invalid_fibonacci_request(self):
        response = self.client.get(fibonacci_url(1001))
        self.assertEqual(response.status_code, 400)
