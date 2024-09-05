#!/usr/bin/python3
"""LRU Caching System"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Least Recently used Caching system"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Adding to the caching"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.cache_order.pop(0)
            del self.cache_data[lru]
            print(f'DISCARD: {lru}')

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """Get item from the cache"""
        if key is None and key not in self.cache_data:
            return None

        if key in self.cache_order:
            self.cache_order.remove(key)
            self.cache_order.append(key)
        return self.cache_data.get(key)
