#!/usr/bin/python3
''' FIFOCache '''


from base_caching import BaseCaching
from typing import Any


class FIFOCache(BaseCaching):
    ''' Caching with FIFO '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key: str, item: Any) -> None:
        ''' Adding item to the cache
        Args:
            key (str): The key for item
            item (any): The item of cache
        Return:
            Returns none
        '''
        if key is None or item is None:
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            print(f'DISCARD: {first_key}')
            del self.cache_data[first_key]

        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        '''
        Getting item from the cache by the key
        Args:
            Key (str): The key that will be used to get the item
        Returns:
            The cached item or None if key is not found
        '''
        if key is None or Key not in self.cache_data:
            return None
        return self.cache_data[key]
