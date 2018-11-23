from dataLoader import DataLoader


class TraderSimulation(object):
    def __init__(self, traders_dict, data_path):
        self._traders = traders_dict
        self._data_loader = DataLoader(data_path)
        self._data_loader.load_data()
        pass

    def get_prediction(self, prediction_day):
        history_dict = {}
        prediction_dict = {}
        for trader_name, trader in self._traders:
            prediction_dict[trader_name] = trader.prediction(history_dict)

        return prediction_dict

