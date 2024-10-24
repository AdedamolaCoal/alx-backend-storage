#!/usr/bin/env python3
"""a class that stores data in redis"""

import redis
import uuid
from typing import Union


class Cache:
    """a class that stores data in redis"""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a randomly generated key.
        Args:
            data: The data to store, which can be of type str, bytes, int, or float.
        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
