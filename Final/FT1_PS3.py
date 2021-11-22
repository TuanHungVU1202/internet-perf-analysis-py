import numpy as np
import pandas
from matplotlib import pyplot as plt

class FT1_PS3:
    def plot(self):
        orig_data = self.extract_data()

        # 1.1
        rtt = plt.figure("1.11. Round-trip times")
        plt.plot(orig_data['RTT_SUM'])
        plt.title("Round-trip time")
        plt.xlabel("Connection Number")
        plt.ylabel("RTT (ms)")

        rtt_log = plt.figure("1.11. Round-trip times - Log Scale")
        plt.plot(np.log(orig_data['RTT_SUM']))
        plt.title("Round-trip time - Log Scale")
        plt.xlabel("Connection Number")
        plt.ylabel("RTT (ms) - Log")

        plt.show()


    def extract_data(self):
        ps3 = '/Users/hungvu/Desktop/E7130/final/out/ps3.csv'
        data = pandas.read_csv(ps3, sep=',', skiprows=10)
        # filtered = data.loc[:, data.columns.str.startswith('RTT')]

        # 1.11
        data['RTT_SUM'] = data['RTT_samples_a2b'] + data['RTT_samples_b2a']
        print("Round-trip times variance= " + str(data['RTT_SUM'].var()))
        return data
