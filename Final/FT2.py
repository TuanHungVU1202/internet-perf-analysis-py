import numpy as np
import pandas
from fitter import Fitter, get_common_distributions
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


class FT2:
    def plot(self):
        fs2 = self.extract_data()
        plt.show()

    def extract_data(self):
        fs1 = '/Users/hungvu/Desktop/E7130/final/out/FS1'
        fs2 = '/Users/hungvu/Desktop/E7130/final/out/FS2'
        col_names = ["src", "sport", "spkt", "sbytes", "dst", "dport", "dpkt", "dbytes",
                     "start", "end", "duration"]
        df_fs1 = pandas.read_csv(fs1, sep=' ', skiprows=1, names=col_names)
        df_fs2 = pandas.read_csv(fs2, sep=' ', names=col_names)
        df_fs2['bytes'] = df_fs2['sbytes'] + df_fs2['dbytes']

        # 2.1 Choosing 1.9
        train, test = train_test_split(df_fs2['bytes'], test_size=0.4)
        fit_train = Fitter(train,
                           distributions=get_common_distributions())
        fit_test = Fitter(test,
                          distributions=get_common_distributions())
        fit_train.fit()
        print("Summary fitting")
        print(fit_train.summary())
        print("Parameters: " + str(fit_train.get_best(method='sumsquare_error')))

        fit_test.fit()
        print("Summary Evaluating")
        print(fit_test.summary())
        print("Parameters: " + str(fit_test.get_best(method='sumsquare_error')))

        return df_fs2
