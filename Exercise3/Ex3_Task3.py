import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Ex3_Task3:
    def plot(self, number_of_dataset):
        print("Ex3_T3")
        for idx in range(number_of_dataset):
            timestamp_data, linkload_data = self.extract_data(number_of_dataset)


        # time_plot = plt.figure("Timeplot")
        # plt.scatter(number_of_data_points, raw_data)
        # plt.title("Flow lengths in bytes and number of data points")
        # plt.xlabel("Number of Data Points")
        # plt.ylabel("Flow length (bytes)")
        #
        # lag_plot = plt.figure("Lag Plot")
        # # numbers = [0.1, 0.5, 1, 1.5, 2, 4, 5.5, 6, 8, 9]
        # plt.hist(raw_data, bins=5)
        # plt.title("Flow lengths in bytes and its frequency")
        # plt.xlabel("Flow length (bytes)")
        # plt.ylabel("Frequency")
        #
        # correlogram = plt.figure("Correlogram")
        # # values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]
        # plt.boxplot(raw_data)
        # # plt.yticks(range(1, 22))
        # plt.ylabel("Flow length (bytes)")

        # plt.show()

    def extract_data(self, number_of_dataset):
        timestamp_list = [None] * 4
        linkload_list = [None] * 4

        for idx in range(number_of_dataset):
            # if NOT linkload-2 dataset
            if idx != 1:
                # file = open("Exercise3/r-data/linkload-" + str(idx+1) + ".txt", "r")
                # raw_data = file.read()
                # str_data = raw_data.split("\n")
                # file.close()
                # str_data.pop()
                # int_data = list(map(int, str_data))
                #
                # sorted_data = np.sort(int_data)
                # log_data = list(np.log(int_data))
                # sorted_log_data = np.sort(log_data)
                # number_of_data_points = range(len(int_data))
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
