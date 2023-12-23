#!/usr/bin/python3
''' Cache class'''
import redis
from uuid import uuid4
from typing import Optional, Union


class Cache:
    '''
        Cache class.
    '''
    def __init__(self):
        '''
            Initialize the cache.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            Store data in the cache.
        '''
        uniqueKey = str(uuid4())
        self._redis.set(uniqueKey, data)
        return uniqueKey
