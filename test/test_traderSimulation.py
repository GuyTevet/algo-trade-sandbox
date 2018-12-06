import os
from unittest import TestCase

from test.mocks.traderMock import TraderMock
from traderSimulation import TraderSimulation


class TestTraderSimulation(TestCase):
    def test_get_prediction_5_stocks_10_days(self):
        trader = TraderMock()
        data_path = os.path.join('.', 'data', '5_stocks_10_days.csv')
        trader_simulation = TraderSimulation({trader.name: trader}, data_path, first_train_day=1, test_size=1)
        results = trader_simulation.get_prediction(8)
        assert trader.name in results, format(trader.name, 'should be in the results')
        assert len(results.keys()) == 1, 'Number of traders should be 1'
        assert len(results[trader.name]) == 5, 'Number of predicted stocks should be 5'
