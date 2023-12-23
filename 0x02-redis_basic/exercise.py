#!/usr/bin/python3
''' Cache class'''
import redis
from uuid import uuid4
from typing import Optional, Union, Callable


class Cache:
    ''' Cache class '''
    def __init__(self):
        ''' Initialize the cache '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in cache '''
        uniqueKey = str(uuid4())
        self._redis.set(uniqueKey, data)
        return uniqueKey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int,
                                                    float]:
        ''' Get data from cache '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
