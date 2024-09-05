#!/usr/bin/env python3
"""LIFO Cache System"""
from typing import Any
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system based o Last in First out"""
    def __init__(self):
        """Class initialization"""
        super().__init__()
        self.cache_order = []

    def put(self, key: str, item: Any) -> None:
        """
        Adding an item to the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.cache_order.pop(-2)
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')

    def get(self, key: str) -> Any:
        """Getting an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
