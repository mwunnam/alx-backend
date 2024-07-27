#!/usr/bin/python3
''' Basic_cache '''


from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    def put(self, key: str, item: any) -> None:
        ''' Add an item to the cache '''
        if key is None and item is None:
            return None
        self.cache_data[key] = item

    def get(self, key: str) -> any:
        ''' Get an item by key from the cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
