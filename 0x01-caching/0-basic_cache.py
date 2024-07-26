#!/usr/bin/env python3
''' Basic_cache '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        ''' Add an item to the cache '''
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key from the cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
