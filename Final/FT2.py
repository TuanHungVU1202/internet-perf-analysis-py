import numpy as np
import pandas
from fitter import Fitter, get_common_distributions
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


class FT2:
    def plot(self):
        fs2, combine_bytes = self.extract_data()

        # hist_data = [i for i in list(combine_bytes.values()) if i != 0]

        plot2_bytes2 = plt.figure("2.2. Aggregate Data Volume")
        plt.bar(range(len(combine_bytes)), list(combine_bytes.values()))
        plt.title("Aggregate Data Volume")
        plt.xlabel("User (IP address)")
        plt.ylabel("Bytes")

        plt.show()

    def extract_data(self):
        fs1 = '/Users/hungvu/Desktop/E7130/final/out/FS1'
        fs2 = '/Users/hungvu/Desktop/E7130/final/out/FS2'
        col_names = ["src", "sport", "spkt", "sbytes", "dst", "dport", "dpkt", "dbytes",
                     "start", "end", "duration"]
        df_fs1 = pandas.read_csv(fs1, sep=' ', skiprows=1, names=col_names)
        df_fs2 = pandas.read_csv(fs2, sep=' ', names=col_names)
        df_fs2['bytes'] = df_fs2['sbytes'] + df_fs2['dbytes']

        # 2.1 Choosing 1.9 - Consider each flow only
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

        # 2.2 Consider bytes each USER (not each flow)
        columns = ["pkt", "bytes", "flows"]
        combine_bytes = self.combine_flow(df_fs2, columns[1])
        # sorted_bytes = sorted(combine_bytes.items(), key=lambda x: x[1], reverse=True)

        return df_fs2, combine_bytes

    def combine_flow(self, data, col_name):
        pairs = {}
        for row in data.itertuples():
            src = row.src
            dst = row.dst
            if col_name == "pkt":
                val = row.pkt
            elif col_name == "bytes":
                val = row.bytes
            elif col_name == "flows":
                val = row.flows
            pair = ''
            if src < dst:
                pair = src + ',' + dst
            else:
                pair = dst + ',' + src
            if pair in pairs:
                pairs[pair] += int(val)
            else:
                pairs[pair] = int(val)

        return pairs
