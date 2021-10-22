import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Ex3_Task2:
    log_scale = "log"

    def plot(self, linear_or_log):
        print("Ex3_T2")
        raw_data, sorted_data, log_data, sorted_log_data, number_of_data_points = self.extract_data(linear_or_log)

        scatter_plot = plt.figure("I. Scatterplot")
        plt.scatter(number_of_data_points, raw_data)
        plt.title("Flow lengths in bytes and number of data points")
        plt.xlabel("Number of Data Points")
        plt.ylabel("Flow length (bytes)")

        hist = plt.figure("II. Histogram")
        # numbers = [0.1, 0.5, 1, 1.5, 2, 4, 5.5, 6, 8, 9]
        plt.hist(raw_data, bins=5)
        plt.title("Flow lengths in bytes and its frequency")
        plt.xlabel("Flow length (bytes)")
        plt.ylabel("Frequency")

        boxplot = plt.figure("III. Boxplot")
        # values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]
        plt.boxplot(raw_data)
        # plt.yticks(range(1, 22))
        plt.ylabel("Flow length (bytes)")

        # enpirical cdf
        emp_cdf = plt.figure("IV. Empirical CDF")
        x = sorted_data
        y = np.arange(len(x)) / float(len(x))
        plt.xlabel("Flow length (bytes)")
        plt.ylabel("%")
        plt.plot(x, y)

        # Plot with LOG scale data
        scatter_plot_log = plt.figure("I. LOG Scatterplot")
        plt.scatter(number_of_data_points, log_data)
        plt.title("Flow lengths in bytes and number of data points")
        plt.xlabel("Number of Data Points")
        plt.ylabel("Flow length (bytes)")

        hist_log = plt.figure("II. LOG Histogram")
        plt.hist(log_data, bins=10)
        plt.title("Flow lengths in bytes and its frequency")
        plt.xlabel("Flow length (bytes)")
        plt.ylabel("Frequency")

        boxplot_log = plt.figure("III. LOG Boxplot")
        plt.boxplot(log_data)
        plt.ylabel("Flow length (bytes)")

        # enpirical cdf
        emp_cdf_log = plt.figure("IV. LOG Empirical CDF")
        x = sorted_log_data
        y = np.arange(len(x)) / float(len(x))
        plt.xlabel("Flow length (bytes)")
        plt.ylabel("%")
        plt.plot(x, y)

        plt.show()

    def extract_data(self, linear_or_log):
        file = open("Exercise3/r-data/flows.txt", "r")
        raw_data = file.read()
        str_data = raw_data.split("\n")
        file.close()
        # remove last blank element
        str_data.pop()
        int_data = list(map(int, str_data))

        # This was intentionally to get the freq for histogram but no use
        # value = []
        # freq = []
        # for x in int_data:
        #     # check if exists in unique_list or not
        #     if x not in value:
        #         value.append(x)
        #
        # # sort value list
        # value.sort()
        # # traverse new value list
        # for idx, val in enumerate(value):
        #     freq.insert(idx, int_data.count(val))

        # return data
        sorted_data = np.sort(int_data)
        log_data = list(np.log(int_data))
        sorted_log_data = np.sort(log_data)
        number_of_data_points = range(len(int_data))

        # return raw_data, sorted_data, log_data, sorted_log_data, number_of_data_points (i.e index or number of
        # lines in data set)
        return int_data, sorted_data, log_data, sorted_log_data, number_of_data_points

    # TODO: method to scale to log scale
