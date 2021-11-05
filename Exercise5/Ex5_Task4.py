import numpy as np
import pandas
from matplotlib import pyplot as plt


class Ex5_Task4:
    def plot(self):
        data, moving_ave, x_value = self.extract_data()

        # I
        plot = plt.figure("I. Bytes vs Packets - Log scale")
        plt.title("Bytes vs Packets In Logarithmic scale")
        plt.xlabel("Packets")
        plt.ylabel("Bytes")
        plt.scatter(np.log(data['pkt']), np.log(data['bytes']))
        plt.tight_layout()

        # III
        plot_moving_ave = plt.figure("II. Moving average")
        plt.title("Moving average")
        plt.xlabel("Number of flows")
        plt.ylabel("Mean values")
        plt.plot(x_value, moving_ave, '-')
        plt.tight_layout()

        plt.show()

    def extract_data(self):
        file = '/Users/hungvu/Desktop/E7130/e5/sampling-data/flows.txt'
        col_name = ['pkt', 'bytes']
        data = pandas.read_csv(file, sep='\t', names=col_name)
        # I, Mean and Median for Packets and Bytes, respectively
        print("Packets - Mean= " + str(data['pkt'].mean()) + ", " + "Median= " + str(data['pkt'].median()))
        print("Bytes - Mean= " + str(data['bytes'].mean()) + ", " + "Median= " + str(data['bytes'].median()))

        # III.
        moving_ave = data['bytes'].rolling(100).mean()
        x_axis = list(range(0, len(moving_ave)))
        return data, moving_ave, x_axis