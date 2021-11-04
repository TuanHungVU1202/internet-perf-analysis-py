import random

import pandas
from matplotlib import pyplot as plt
from pandas.plotting import parallel_coordinates


class Ex5_Task1:
    def plot(self):
        data = self.extract_data()
        samples = data.sample(1000)
        parallel_coordinates(samples, 'flows', cols=["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                        "start", "end"])
        plt.tight_layout()
        plt.show()

    def extract_data(self):
        file_path = '/Users/hungvu/Desktop/E7130/e5/sampling-data/flowdata.txt'
        data = pandas.read_csv(file_path, sep='\t')
        data.columns = ["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                        "start", "end"]
        return data.astype(str)
