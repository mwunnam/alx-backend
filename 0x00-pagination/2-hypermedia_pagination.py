#!/usr/bin/env python3
"""Index Function that return the starting index an ending index"""
from typing import Tuple
import csv
import math
from typing import List
from typing import Dict
from typing import Any


def index_range(page: int, page_size: int) -> tuple:
    '''
    Function to calculate the start and end of a pagenation
    Args:
        page (int): The current page number
        page_size (int): The number of items per page
    return:
        tuple: A tuple containing the start and the end indexes
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset
        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: A List of rows corresponding to the data.
        """
        assert isinstance(page, int), "page must be an integer"
        assert page > 0, "Page must greater than 0"

        assert isinstance(page_size, int), "Page must be an integer"
        assert page_size > 0, "Page size must be an interger"

        start_index, end_index = index_range(page, page_size)

        data = self.dataset()
        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination information
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
