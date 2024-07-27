#!/usr/bin/python3
''' LIFO Caching '''


from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    ''' Caching system with LIFO eviction '''

    def __init__(self):
        ''' Initialize the cache '''
        super().__init__()
        self.order = []

    def put(self, key: str, item: Any) -> None:
        '''
        Adding an item by key using the FIFo eviction
        Args:
            key (str): The key to be used
            item (Any): The Item to be retrived
        Return:
            None
        '''
        if key is None or item is None:
            return None

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            print(f'DISCARD: {last_key}')
            del self.cache_data[last_key]

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        '''
        Getting an item from the cache by key
        Args:
            key (str): The key to the item to be retrieved
        Returns (Any):
            The item in the key or None if the key does not exist
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
