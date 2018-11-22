import numpy as np
import os
import csv
from copy import copy

class DataLoader(object):

    """
    load csv file to train/test dictionaries
    """

    def __init__(self,dataPath):
        self.dataPath = dataPath
        self.testSize = 200 # HARD CODED - do not change!

    def getData(self):

        data = {}

        with open(self.dataPath,'r') as f:
            reader = csv.DictReader(f)

            for row in reader:

                newStock = False
                name = row['Name']
                del row['Name']

                # add name if new
                if name not in data.keys():
                    data[name] = {}
                    newStock = True

                # add data
                for key in row.keys():
                    if newStock:
                        data[name][key] = [row[key]]
                    else:
                        data[name][key].append(row[key])

        # split to train/test
        totalSize = len(data[name][key])
        trainSize = totalSize - self.testSize
        # TODO

        return data

# D = DataLoader('./data/all_stocks_5yr.csv')
# data = D.getData()
