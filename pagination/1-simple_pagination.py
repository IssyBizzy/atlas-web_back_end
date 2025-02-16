#!/usr/bin/env python3
"""This module returns a database by a given
page size """
import csv
import math
from typing import List
pg = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the page and returns it with page info"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        result = self.dataset()
        start_index, end_index = pg(page, page_size)
        if start_index >= len(result):
            return []
        return result[start_index:end_index]
