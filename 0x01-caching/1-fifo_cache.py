#!/usr/bin/env python3
"""FIFO Caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching system"""
    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Adds a new to the cache system if there is space, if no space
        the first item in the dictionary is discarded to make room
        the item discarded is printed
        """

        if key is None or item is None:
            return None


        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.cache_order.pop(0)
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')
            self.cache_data[key] = item

        self.cache_order.append(key)

    def get(self, key):
        """
        Gets item from the cache system
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
