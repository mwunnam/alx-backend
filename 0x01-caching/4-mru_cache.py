#!/usr/bin/python3
"""MRU Caching System"""
from base_caching import BaseCaching


class LRUCaching(BaseCaching):
    """Most Recently used Caching system"""
    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
       """Adding to the caching"""
        if key is not None or item is not None:
            if key not in self.cache_order:
                self.cache_order.append(key)
            if key in self.cache_order:
                del self.cache_order[key]
                self.cache_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru = self.cache_order.pop()
                print(f'DISCARD: {mru}')
                del self.cache_data[mru]

        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache"""
        if key is not None and key is in self.cache_data:
            return self.cache_data.get(key, None)
