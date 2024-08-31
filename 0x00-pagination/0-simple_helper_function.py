#!/usr/bin/python3
"""Index Function that return the starting index an ending index"""
from typing import Tuple


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
