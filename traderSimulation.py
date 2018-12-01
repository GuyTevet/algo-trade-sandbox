import os

from dataLoader import DataLoader
from trader import Trader


class TraderSimulation(object):
    def __init__(self, traders_dict, data_path):
        self._traders = traders_dict
        self._data_loader = DataLoader(data_path)
        self._data_loader.load_data()
        pass

    def get_prediction(self, prediction_day):
        # fixme: Create function in data loader
        data_keys = ['close', 'open', 'high', 'low', 'volume']

        # Avoid loading the table again to memory if parameters are invalid
        if prediction_day > self._data_loader.train_dict['num_dates'] - 1:
            raise ValueError('prediction_day have to be smaller than num_days - 1')

        history_dict = self._data_loader.train_dict.copy()
        history_dict['num_dates'] = prediction_day - 1
        for k in data_keys:
            for s in history_dict['stock_names']:
                history_dict[k][s] = history_dict[k][s][:prediction_day - 1]

        prediction_dict = {}
        for trader_name, trader in self._traders:
            prediction_dict[trader_name] = trader.prediction(history_dict)

        return prediction_dict


if __name__ == '__main__':
    traders_dic = {'base_trader':Trader()}
    data_path = os.path.join('.','data','all_stocks_5yr.csv')
    trader_simulation = TraderSimulation(traders_dic, data_path)
    predictions = trader_simulation.get_prediction(10)
    print(predictions)


