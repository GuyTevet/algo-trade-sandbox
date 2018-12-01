import numpy as np
import os
import csv
from copy import copy
from tempfile import NamedTemporaryFile
import shutil
import matplotlib.pyplot as plt
import random

class DataLoader(object):

    """
    load csv file to train/test dictionaries
    """

    def __init__(self,data_path):
        self.data_path = data_path
        self.total_size = -1
        self.test_size = 200 # HARD CODED - do not change!
        self.train_size = -1
        self.train_dict = {}
        self.test_dict = {}

    def csv_hole_filler(self):

        print('DataLoader - csv_hole_filler...')

        holes = 0
        temp_file_path = NamedTemporaryFile(delete=False).name

        with open(self.data_path, 'r') as csv_file:
            with open(temp_file_path, 'r+') as temp_file:
                reader = csv.reader(csv_file)
                writer = csv.writer(temp_file, lineterminator='\n')

                prev_row = None

                for row in reader:
                    for i in range(len(row)):
                        if row[i] == '' or row[i] == ' ':
                            holes += 1
                            row[i] = prev_row[i]

                    writer.writerow(row)
                    prev_row = copy(row)

        shutil.move(temp_file.name, self.data_path)
        print('DataLoader - csv_hole_filler found [{}] holes'.format(holes))

    def load_data(self):

        data = {}

        self.csv_hole_filler()

        with open(self.data_path,'r') as f:
            reader = csv.DictReader(f)

            for row in reader:

                new_stock = False
                name = row['Name']
                del row['Name']

                # add name if new
                if name not in data.keys():
                    data[name] = {}
                    new_stock = True

                # add data
                for key in row.keys():
                    try:
                        val = float(row[key])
                    except:
                        val = row[key]

                    if new_stock:
                        data[name][key] = [val]
                    else:
                        data[name][key].append(val)

        # create train/test dicts
        self.total_size = max([len(data[name]['date']) for name in data.keys()])
        self.train_size = self.total_size - self.test_size

        incorrect_data_keys = []
        for name in data.keys():
            if not self.total_size == len(data[name]['date']):
                incorrect_data_keys.append(name)

        for name in incorrect_data_keys:
            del data[name]

        stock_names = sorted(data.keys())
        num_stocks = len(stock_names)

        self.train_dict = {
            'num_stocks': num_stocks,
            'num_dates': self.train_size,
            'stock_names': stock_names,
            # 'close': np.empty([num_stocks, self.total_size], dtype=np.float32),
            # 'open': np.empty([num_stocks, self.total_size], dtype=np.float32),
            # 'high': np.empty([num_stocks, self.total_size], dtype=np.float32),
            # 'low': np.empty([num_stocks, self.total_size], dtype=np.float32),
            # 'volume': np.empty([num_stocks, self.total_size], dtype=np.float32)
        }

        self.test_dict = copy(self.train_dict)
        self.test_dict['num_dates'] = self.test_size

        table_names = copy(reader.fieldnames)
        table_names.remove('Name')
        table_names.remove('date')

        # add dict tables
        for table in table_names:
            self.train_dict[table] = np.empty([num_stocks, self.train_size], dtype=np.float32)
            self.test_dict[table] = np.empty([num_stocks, self.test_size], dtype=np.float32)

            for stock_i, name in enumerate(stock_names):
                self.train_dict[table][stock_i] = data[name][table][:self.train_size]
                self.test_dict[table][stock_i] = data[name][table][-self.test_size:]

        return

    def debug_plot(self, num_plots = 20, type='train'):

        debug_dir = os.path.join('.','debug')

        if not os.path.exists(debug_dir):
            os.mkdir(debug_dir)

        if type == 'train':
            data = self.train_dict
        elif type == 'test':
            data = self.test_dict

        for stock_i in random.sample(range(data['num_stocks']), num_plots):

            name = '{0}-{1}'.format(data['stock_names'][stock_i], type)

            plt.figure(figsize=(20,10))
            plt.title(name)
            keys = ['open','close','high','low']
            lines = []
            for key in keys:
                l, = plt.plot(np.arange(data['num_dates']),data[key][stock_i], linewidth=.4)
                lines.append(l)
            plt.legend(lines, keys)
            plt.savefig(os.path.join(debug_dir,name + '.png'))

        return


if __name__ == '__main__':

    # Test
    D = DataLoader(os.path.join('.','data','all_stocks_5yr.csv'))
    D.load_data()
    D.debug_plot()
    D.debug_plot(type='test')

