#!/usr/bin/env python3
"""a class that stores data in redis"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a particular function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"  # method.__qualname__inputs
        output_key = f"{method.__qualname__}:outputs"  # method.__qualname__outputs

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis, optionally converting it using a callable function.
        Args:
            key (str): The Redis key to retrieve.
            fn (Callable, optional): A function to convert the retrieved data.
            Defaults to None, meaning no conversion.
        Returns:
            Union[str, bytes, int, None]: The retrieved data, optionally converted.
        """
        # Retrieve the data from Redis
        data = self._redis.get(key)

        # If the data doesn't exist, return None
        if data is None:
            return None

        # If a conversion function is provided, apply it
        if fn:
            return fn(data)

        # If no function is provided, return the raw data
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis as a UTF-8 decoded string.
        Args:
            key (str): The Redis key to retrieve.
        Returns:
            Optional[str]: The decoded string, or None if the key doesn't exist.
        """
        result = self.get(key, fn=lambda d: d.decode("utf-8"))

        if isinstance(result, str) or result is None:
            return result
        raise ValueError(f"Expected str, got {type(result)}")

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis as an integer.
        Args:
            key (str): The Redis key to retrieve.
        Returns:
            Optional[int]: The integer value, or None if the key doesn't exist.
        """
        result = self.get(key, fn=int)

        if isinstance(result, int) or result is None:
            return result
        raise ValueError(f"Expected int, got {type(result)}")
