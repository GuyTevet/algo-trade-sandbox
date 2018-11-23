import numpy as np
import os
import csv
from copy import copy

class DataLoader(object):

    """
    load csv file to train/test dictionaries
    """

    def __init__(self,data_path):
        self.data_path = data_path
        self.test_size = 200 # HARD CODED - do not change!
        self.train_dict = {}
        self.test_dict = {}

    def load_data(self):

        num_stocks = 0
        num_dates = 0

        self.train_dict = {
            'num_stocks': num_stocks,
            'num_dates': num_dates,
            'close': np.empty([num_stocks,num_dates], dtype=np.float32),
            'open': np.empty([num_stocks, num_dates], dtype=np.float32),
            'high': np.empty([num_stocks, num_dates], dtype=np.float32),
            'low': np.empty([num_stocks, num_dates], dtype=np.float32),
            'volume': np.empty([num_stocks, num_dates], dtype=np.float32)
        }

        self.test_dict = copy(self.train_dict)

        return



    # def splitData(self,splitList):
    #
    #     splitDicts = [dict()] * len(splitList)
    #
    # def getDailyData(self,dayIdx):
    #
    #     nameList = sorted(self.data.keys())
    #     closeList =

    # def getNamesDates(self):
    #
    #     names = []
    #     dates = []
    #
    #     with open(self.dataPath,'r') as f:
    #         reader = csv.DictReader(f)
    #
    #         for row in reader:
    #             if row['Name'] not in names:
    #                 names.append(row['Name'])
    #             if row['date'] not in dates:
    #                 dates.append(row['date'])
    #
    #     # sort
    #     names = sorted(names)
    #
    #
    #     return names, dates
    #
    # def getData(self):
    #
    #     data = {}
    #
    #     with open(self.dataPath,'r') as f:
    #         reader = csv.DictReader(f)
    #
    #         for row in reader:
    #
    #             newStock = False
    #             name = row['Name']
    #             del row['Name']
    #
    #             # add name if new
    #             if name not in data.keys():
    #                 data[name] = {}
    #                 newStock = True
    #
    #             # add data
    #             for key in row.keys():
    #                 if newStock:
    #                     data[name][key] = [row[key]]
    #                 else:
    #                     data[name][key].append(row[key])
    #
    #     # split to train/test
    #     totalSize = len(data[name][key])
    #     trainSize = totalSize - self.testSize
    #     # TODO
    #
    #     return data

# D = DataLoader('./data/all_stocks_5yr.csv')
# data = D.getData()
