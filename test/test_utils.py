import os
from unittest import TestCase

from dataLoader import DataLoader
from utils import value_matrix2gain_matrix


class TestUtils(TestCase):
    def test_value_matrix2gain_matrix_print_result(self):
        data_path = os.path.join('.', 'data', '5_stocks_10_days.csv')
        data_loader = DataLoader(data_path)
        data_loader.load_data()
        close_matrix = data_loader.train_dict['close']
        gain_matrix = value_matrix2gain_matrix(close_matrix)
        print(gain_matrix)
