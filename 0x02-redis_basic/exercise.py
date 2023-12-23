#!/usr/bin/python3
''' Cache class'''
import redis
from uuid import uuid4
from typing import Optional, Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' Counts the number of times '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper function '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Store history '''
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper function '''
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    ''' Replay history function '''
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    ''' Cache class '''
    def __init__(self):
        ''' Initialize the cache '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_str(self, key: str) -> str:
        ''' Get string from cache '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''Get int from cache '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
