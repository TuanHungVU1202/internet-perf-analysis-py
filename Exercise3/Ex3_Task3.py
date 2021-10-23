import matplotlib
import pandas as pd
from matplotlib import pyplot as plt


class Ex3_Task3:
    def plot(self, number_of_dataset):
        print("Ex3_T3")
        timestamp_data, linkload_data = self.extract_data(number_of_dataset)
        for idx in range(number_of_dataset):
            # for now even with linkload-2 still can use "fake" datetime with interval = 1s
            if idx >= 0:
                dates = matplotlib.dates.date2num(timestamp_data[idx])
                # Timeplot
                plot = plt.figure("Linkload-" + str(idx + 1) + " Timeplot")
                plt.title("Linkload along time")
                plt.xlabel("Time (interval = 1s)")
                plt.ylabel("Linkload (bps)")
                plt.tight_layout()
                plt.plot_date(dates, linkload_data[idx], linestyle='solid', marker='None')

                # Lagplot
                series = pd.Series(linkload_data[idx])
                lagplot = plt.figure("Linkload-" + str(idx + 1) + " Lag plot")
                plt.title("Lag plot with Lag-1")
                plt.xlabel("Linkload (bps) at (T-1)")
                plt.ylabel("Linkload (bps) at T")
                pd.plotting.lag_plot(series, lag=1)

                # Autocorrelation plot
                correlation_plot = plt.figure("Linkload-" + str(idx + 1) + " Autocorrelation plot")
                plt.title("Autocorrelation plot")
                plt.xlabel("Lag")
                plt.ylabel("Autocorrelation")
                pd.plotting.autocorrelation_plot(series)
            else:
                pass

        plt.show()

    def extract_data(self, number_of_dataset):
        timestamp_list = [None] * 4
        linkload_list = [None] * 4

        for idx in range(number_of_dataset):
            # if NOT linkload-2 dataset
            if idx != 1:
                header_list = ["timestamp", "linkload"]
                df = pd.read_csv("Exercise3/r-data/linkload-" + str(idx + 1) + ".txt", sep=' ', index_col=False,
                                 names=header_list)
                timestamp = df.loc[:, "timestamp"].to_list()
                linkload = df.loc[:, "linkload"].to_list()
                timestamp_list.insert(idx, timestamp)
                linkload_list.insert(idx, linkload)
            else:
                print("Processing linkload 2")
                header_list = ["linkload"]
                df = pd.read_csv("Exercise3/r-data/linkload-" + str(idx + 1) + ".txt", names=header_list)
                timestamp = list(range(len(df.index)))
                linkload = df.loc[:, "linkload"].to_list()
                timestamp_list.insert(idx, timestamp)
                linkload_list.insert(idx, linkload)

        # print(timestamp_list[1])
        # print(linkload_list[1])
        return timestamp_list, linkload_list
