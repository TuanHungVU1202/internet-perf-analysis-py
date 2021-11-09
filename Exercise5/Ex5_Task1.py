import random

import numpy as np
import pandas
from matplotlib import pyplot as plt
from pandas.plotting import parallel_coordinates


class Ex5_Task1:
    def plot(self):
        orig_data, data_str, sport80 = self.extract_data()

        # I. samping 1000 from original data
        plot_1k = plt.figure("I. 1000 samples - Original")
        plt.title("1000 random samples")
        plt.xlabel("Variables")
        plt.ylabel("Value")
        parallel_coordinates(data_str.sample(1000), 'flows', cols=["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                        "start", "end"])
        plt.tight_layout()

        # II. data from source port 80 only
        sport80_plt = plt.figure("II. Source port 80 data")
        plt.title("Source port 80")
        plt.xlabel("Variables")
        plt.ylabel("Value")
        parallel_coordinates(sport80, 'flows', cols=["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                        "start", "end"])
        plt.tight_layout()

        # III. scatter bytes against packets
        plot = plt.figure("III. Bytes vs Packets")
        plt.title("Bytes vs Packets")
        plt.xlabel("Bytes")
        plt.ylabel("Packets")
        plt.scatter(np.log(orig_data['bytes']), np.log(orig_data['pkt']))
        plt.tight_layout()

        plt.show()

    def extract_data(self):
        file_path = '/Users/hungvu/Desktop/E7130/e5/sampling-data/flowdata.txt'
        data = pandas.read_csv(file_path, sep='\t')
        data.columns = ["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                        "start", "end"]
        # II
        sport80 = data[data.sport == 80]

        # III
        data['pkt_size'] = data['bytes']/data['pkt']
        print("Maximum average packet size: ")
        print(data['pkt_size'].max())

        # IV
        data['ave_throughput'] = data['bytes'] / (data['end'] - data['start'])
        filtered_data = data.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
        print(filtered_data)
        print("Mean= " + str(filtered_data['ave_throughput'].mean()) + " - Median= " + str(filtered_data['ave_throughput'].median()))
        return data, data.astype(str), sport80.astype(str)
