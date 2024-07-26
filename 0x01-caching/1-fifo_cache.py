#!/usr/bin/python3
''' FIFOCache '''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' Caching with FIFO '''
    def __init__(self):
        super().__init__()
        self.order = []

    ''' Adding to the cache dictionary '''
    def put(self, key, item):
        if key is None or item is None:
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            print(f'DISCARD: {first_key}')
            self.cache_data.pop(first_key)

        if key in self.cache_data:
            self.order.remove(key)

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        ''' Getting the key '''
        if key is None or Key not in self.cache_data:
            return None

        return self.cache_data[key]
