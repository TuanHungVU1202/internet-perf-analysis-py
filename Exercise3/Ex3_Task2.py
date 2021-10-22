import csv

import matplotlib.pyplot as plt
import pandas as pd


class Ex3_Task2:
    log_scale = "log"
    def plot(self, linear_or_log):
        print("Ex3_T2")
        value, freq = self.extract_data(linear_or_log)
        plt.scatter(value, freq)
        plt.title("Flow lengths in bytes and its frequency")
        plt.xlabel("Flow length (bytes)")
        plt.ylabel("Frequency")
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
        # data_dict = self.to_frequency_table(data)
        # traverse for all elements
        for x in int_data:
            # check if exists in unique_list or not
            if x not in value:
                value.append(x)
        # traverse new value list
        value.sort()
        for idx, val in enumerate(value):
            freq.insert(idx, int_data.count(val))

        # print(value)
        # print(freq)
        if linear_or_log == self.log_scale:
            print("Getting Logarithmic scale")
            # scale to log
            # data =
        return value, freq

    # TODO: method to scale to log scale