
"""

Utility functions

"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from copy import copy


def gains2percents(array):
    ret = copy(array)
    ret -= 1.
    ret *= 100.
    return ret


def dump_bar_plot(matrix, trader_names, title, save_path, gather_factor=1):
    """

    :param matrix: (np.array) assuming dims [num_traders X num_days]
    :param trader_names: (list of strs)
    :param title: (str)
    :param save_path: (str)
    :param gather_factor: (int) number of diays in single bar
    :return:
    """

    # gather
    num_days = matrix.shape[1]
    num_bars = num_days // gather_factor
    bars_matrix = np.ones([matrix.shape[0],num_bars], dtype=np.float32)
    for i in range(num_bars):
        for j in range(gather_factor):
            bars_matrix[:,i] *= matrix[:, i * gather_factor + j]

    # convert to percents
    bars_matrix = gains2percents(bars_matrix)

    # plot
    df = pd.DataFrame(bars_matrix.T,columns=trader_names)
    df.plot(y=trader_names, kind="bar")
    if len(trader_names) < 2:
        df.plot(y=trader_names, kind="bar", legend=None)
    if num_bars > 50:
        plt.xticks([])
    plt.title(title)
    plt.savefig(save_path)
    return

def dump_video_plot():
    raise NotImplementedError()


def dump_csv(matrix, row_list, col_list, save_path):
    """

    :param matrix: (np array)
    :param row_list: (str list or None)
    :param col_list: (str list or None)
    :return:
    """
    df = pd.DataFrame(matrix, index=row_list, columns=col_list)
    df.to_csv(save_path)
    return


if __name__ == '__main__':

    # Test

    gain_matrix = np.clip(np.random.randn(4,200),a_min=-0.9,a_max=0.9)*0.02+1
    traders = ['a','b','c','d']

    dump_bar_plot(np.expand_dims(gain_matrix[0],axis=0),
                    trader_names=[traders[0]],
                    title='daily_gain_plot',
                    save_path=os.path.join('debug','daily_gain_plot.png'),
                    gather_factor=1)

    dump_bar_plot(gain_matrix,
                    trader_names=traders,
                    title='monthly_gain_plot',
                    save_path=os.path.join('debug','monthly_gain_plot.png'),
                    gather_factor=20)

    dump_csv(gain_matrix,
             row_list=traders,
             col_list=None,
             save_path=os.path.join('debug','daily_gain.csv'))