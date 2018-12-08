from dataLoader import DataLoader
from utils import value_matrix2gain_matrix
import numpy as np


class TraderSimulation(object):
    def __init__(self, traders_dict, data_path, first_train_day=200, test_size=200):
        self._traders = traders_dict
        self._data_loader = DataLoader(data_path)

        # Testability seed, we don't want test size 200 if the entire collection is 10 records
        self._data_loader.test_size = test_size
        self._data_loader.load_data()
        self._first_train_day = first_train_day

    def get_prediction(self, prediction_day):
        # Avoid loading the table again to memory if parameters are invalid
        if prediction_day > self._data_loader.train_dict['num_dates'] - 1:
            raise ValueError('prediction_day have to be smaller than num_days - 1')

        history_dict = self._data_loader.train_dict.copy()
        history_dict['num_dates'] = prediction_day - 1
        for k in self._data_loader.data_columns:
            history_dict[k] = history_dict[k][:, :prediction_day - 1]

        prediction_dict = {}
        for trader_name, trader in self._traders.items():
            prediction_dict[trader_name] = trader.predict(history_dict)

        return prediction_dict

    def calculate_gain(self, prediction_dict, value_matrix):
        """
        Calculate how much each trader has gained compared to the actual results
        :param prediction_dict: key: trader name, value: prediction for each stock
        :param value_matrix: stock's values the day before the prediction and the
        day of the prediction
        """
        gain_matrix = np.squeeze(value_matrix2gain_matrix(value_matrix))
        traders_gain_dict = {}
        for trader_name in prediction_dict.keys():
            traders_gain_dict[trader_name] = np.dot(gain_matrix, prediction_dict[trader_name])

        return traders_gain_dict
