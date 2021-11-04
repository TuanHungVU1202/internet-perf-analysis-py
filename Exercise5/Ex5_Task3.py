import pandas
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from fitter import Fitter, get_common_distributions, get_distributions

class Ex5_Task3:
    def plot(self):
        data_a, data_b, data_c = self.extract_data()

        # # 1. distr A
        # dist_a = plt.figure("A")
        # plt.title("A data")
        # plt.xlabel("Bins")
        # plt.ylabel("Frequency")
        # plt.hist(data_a, bins='auto')

        # # 2. distr b
        # dist_b = plt.figure("B")
        # plt.title("B data")
        # plt.xlabel("Bins")
        # plt.ylabel("Frequency")
        # plt.hist(data_b, bins='auto')

        # 3. distr c
        # dist_c = plt.figure("C")
        # plt.title("C data")
        # plt.xlabel("Bins")
        # plt.ylabel("Frequency")
        # plt.hist(np.log(data_c), bins='auto')

        plt.show()

    def extract_data(self):
        file_a = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_a.txt'
        file_b = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_b.txt'
        file_c = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_c.txt'
        data_a = pandas.read_csv(file_a, header=None)
        data_b = pandas.read_csv(file_b, header=None)
        data_c = pandas.read_csv(file_c, header=None)

        # f = Fitter(data_c,
        #            distributions=['gamma',
        #                           'lognorm',
        #                           "beta",
        #                           "burr",
        #                           "norm"])

        f = Fitter(data_a,
                   distributions=get_common_distributions())
        f.fit()
        print(f.summary())

        return data_a, data_b, data_c