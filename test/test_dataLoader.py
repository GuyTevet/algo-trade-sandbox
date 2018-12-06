import collections
import os
from unittest import TestCase

from dataLoader import DataLoader


class TestDataLoader(TestCase):
    def test_load_data_init_data_columns(self):
        data_path = os.path.join('.', 'data', '5_stocks_10_days.csv')
        data_loader = DataLoader(data_path)
        data_loader.load_data()
        assert collections.Counter(data_loader.data_columns) == collections.Counter(
            ['close', 'open', 'high', 'low', 'volume'])
