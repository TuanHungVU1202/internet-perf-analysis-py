import glob
import os

import pandas
from matplotlib import pyplot as plt


class FT1_PS2:
    def plot(self):
        ports = self.extract_data()

        # 1.1
        hist = plt.figure("1.1. Port distribution")
        # plt.hist(ports, bins='auto')
        plt.title("Port distribution")
        plt.xlabel("Port number")
        plt.ylabel("Freq")

        plt.show()

    def extract_data(self):
        ps1 = '/Users/hungvu/Desktop/E7130/final/out/ps1'
        col_name = ['tcp.sp', 'tcp.dp', 'udp.sp', 'udp.dp', 'len', 'time']
        data = pandas.read_csv(ps1, sep=',', names=col_name)
        return data

    def read_file(self):
        raw_data = []
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/final/out", "*.t2"))
        for file_path in file_list:
            with open(file_path) as f_input:
                lines = f_input.readlines()
                for line in lines:
                    raw_data.append(line)
        return raw_data
