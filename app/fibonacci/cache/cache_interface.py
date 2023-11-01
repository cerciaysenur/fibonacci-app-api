from abc import ABC, abstractmethod


class CacheInterface(ABC):

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value: any, timeout: int = None):
        pass
