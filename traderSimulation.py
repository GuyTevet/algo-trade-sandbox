import os

from dataLoader import DataLoader
from trader import Trader


class TraderSimulation(object):
    def __init__(self, traders_dict, data_path, first_train_day=200, test_size=200):
        self._traders = traders_dict
        self._data_loader = DataLoader(data_path)
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


if __name__ == '__main__':
    traders_dic = {'base_trader': Trader()}
    data_path = os.path.join('.', 'data', 'all_stocks_5yr.csv')
    trader_simulation = TraderSimulation(traders_dic, data_path)
    predictions = trader_simulation.get_prediction(10)
    print(predictions)
