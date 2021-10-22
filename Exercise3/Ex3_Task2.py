import csv

import matplotlib.pyplot as plt
import pandas as pd


class Ex3_Task2:
    log_scale = "log"

    def plot(self, linear_or_log):
        print("Ex3_T2")
        raw_data, number_of_data_points = self.extract_data(linear_or_log)
        scatter_plot = plt.figure("I. Scatterplot")
        plt.scatter(number_of_data_points, raw_data)
        plt.title("Flow lengths in bytes and number of data points")
        plt.xlabel("Number of Data Points")
        plt.ylabel("Flow length (bytes)")

        hist = plt.figure("II. Histogram")
        # numbers = [0.1, 0.5, 1, 1.5, 2, 4, 5.5, 6, 8, 9]
        plt.hist(raw_data, bins=5)
        plt.title("Flow lengths in bytes and its frequency")
        plt.xlabel("Frequency")
        plt.ylabel("Flow length (bytes)")

        boxplot = plt.figure("III. Boxplot")
        # values = [1, 2, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10, 21]
        plt.boxplot(raw_data)
        # plt.yticks(range(1, 22))
        plt.ylabel("Value")

        plt.show()

    def extract_data(self, linear_or_log):
        value = []
        freq = []
        file = open("Exercise3/r-data/flows.txt", "r")
        raw_data = file.read()
        str_data = raw_data.split("\n")
        file.close()
        # remove last blank element
        str_data.pop()
        int_data = list(map(int, str_data))
        # traverse for all elements
        for x in int_data:
            # check if exists in unique_list or not
            if x not in value:
                value.append(x)

        # sort value list
        value.sort()
        # traverse new value list
        for idx, val in enumerate(value):
            freq.insert(idx, int_data.count(val))

        # print(value)
        # print(freq)
        if linear_or_log == self.log_scale:
            print("Getting Logarithmic scale")
            # scale to log
            # data =
        return int_data, range(len(int_data))

    # TODO: method to scale to log scale
