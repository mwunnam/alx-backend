#!/usr/bin/python3
''' Caching with Least Recently Used '''


from typing import Any
from base_caching import BaseCaching


class LRUcache(BaseCaching):
    ''' using the LRU Algorithm '''

    def __init__(self):
        ''' Initiazing the cache '''
        super().__init__()

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

        if len(self.cache.data) >= BaseCaching.Max_ITEMS:
            #discard the lease resent used key
            print(f'DISCARD: {lru_key)')


