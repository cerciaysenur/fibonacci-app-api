import redis
from fibonacci.cache.cache_interface import CacheInterface


class RedisCache(CacheInterface):

    def __init__(self, host='redis', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: any, timeout: int = None):
        self.client.set(key, value, ex=timeout)
