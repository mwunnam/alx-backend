#!/usr/bin/python3
''' Caching with Least Recently Used '''


from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' using the LRU Algorithm '''

    def __init__(self):
        ''' Initiazing the cache '''
        super().__init__()
        self.order = []

    def put(self, key: str, item: Any) -> None:
        '''
        Adding an item to the cache
        Args:
            key (str): The key to add the item
            item (Any): The itme to be added
        Return:
            None
        '''
        if key is None or item is None:
            return None

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            print(f'DISCARD: {lru_key}')
            del self.cache_data[lru_key]

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        '''
        To get the item by using a key
        Args:
            key (str): The key used to get the item
        '''
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
