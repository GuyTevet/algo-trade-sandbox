import numpy as np


class TraderMock(object):

    name = 'mock_trader'

    def __init__(self):
        pass


    def predict(self, history_dict):

        prediction = (1 / history_dict['num_stocks']) * np.ones(history_dict['num_stocks'],dtype=np.float32)

        return prediction

