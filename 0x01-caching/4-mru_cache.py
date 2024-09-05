#!/usr/bin/python3
"""MRU Caching System"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently used Caching system"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Adding to the caching"""
        if key is None or item is None:
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.cache_order.pop()
            del self.cache_data[mru]
            print(f'DISCARD: {mru}')

        self.cache_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.append(key)

        return self.cache_data.get(key, None)
