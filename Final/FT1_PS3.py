import numpy as np
import pandas
from matplotlib import pyplot as plt

class FT1_PS3:
    def plot(self):
        orig_data = self.extract_data()

        # 1.11
        rtt = plt.figure("1.11. Round-trip times")
        plt.scatter(orig_data['RETRANS_SUM'], orig_data['RTT_SUM'])
        plt.title("Round-trip time")
        plt.xlabel("Retransmission")
        plt.ylabel("RTT (ms)")

        rtt_log = plt.figure("1.11. Round-trip times - Log Scale")
        plt.scatter(orig_data['RETRANS_SUM'], np.log(orig_data['RTT_SUM']))
        plt.title("Round-trip time - Log Scale")
        plt.xlabel("Retransmission")
        plt.ylabel("RTT (ms) - Log")

        # 1.12
        traffic_vol = plt.figure("1.12. Traffic volume")
        plt.scatter(orig_data['RETRANS_SUM'], orig_data['total_bytes'])
        plt.title("Traffic volume")
        plt.xlabel("Retransmission")
        plt.ylabel("Traffic volume (bytes)")

        traffic_vol_log = plt.figure("1.12. Traffic volume - Log Scale")
        plt.scatter(orig_data['RETRANS_SUM'], np.log(orig_data['total_bytes']))
        plt.title("Traffic volume - Log Scale")
        plt.xlabel("Retransmission")
        plt.ylabel("Traffic volume (bytes) - Log")

        plt.show()


    def extract_data(self):
        ps3 = '/Users/hungvu/Desktop/E7130/final/out/ps3.csv'
        data = pandas.read_csv(ps3, sep=',', skiprows=10)
        # filtered = data.loc[:, data.columns.str.startswith('RTT')]
        # filtered = data.loc[:, data.columns.str.contains('retrans_a2b')]

        # 1.11
        data['RTT_SUM'] = data['RTT_samples_a2b'] + data['RTT_samples_b2a']
        data['RETRANS_SUM'] = data['max_#_retrans_a2b'] + data['max_#_retrans_b2a']
        print("Round-trip times variance= " + str(data['RTT_SUM'].var()))

        # 1.12
        data['total_bytes'] = data['actual_data_bytes_a2b'] + data['actual_data_bytes_b2a']
        print("Total traffic volumes= " + str(data['total_bytes'].sum()))
        return data
