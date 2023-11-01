from unittest import mock
from django.test import SimpleTestCase
from fibonacci.cache.redis_cache import RedisCache


class TestRedisCache(SimpleTestCase):

    def setUp(self):
        self.redis_mock = mock.MagicMock()
        self.redis_strict_mock = mock.MagicMock(return_value=self.redis_mock)
        self.patcher = mock.patch('redis.StrictRedis', self.redis_strict_mock)
        self.patcher.start()
        self.redis_cache = RedisCache()

    def tearDown(self):
        self.patcher.stop()

    def test_set_value_in_cache(self):
        key = "test_key"
        value = "test_value"
        timeout = 300

        self.redis_cache.set(key, value, timeout)

        self.redis_mock.set.assert_called_with(key, value, ex=timeout)

    def test_get_value_from_cache(self):
        key = "test_key"
        cached_value = "test_value"

        self.redis_mock.get.return_value = cached_value

        result = self.redis_cache.get(key)

        self.redis_mock.get.assert_called_with(key)
        self.assertEqual(result, cached_value)
