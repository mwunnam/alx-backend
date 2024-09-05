#!/usr/bin/evn python3
"""Basic Caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching system that inherits from BaseCaching
       it has no limit
    """

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return None

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key, None)
