import pandas
from matplotlib import pyplot as plt


class Ex5_Task2:
    def plot(self):
        orig_data = self.extract_data()

        # I. original data
        orig_plot = plt.figure("I. Original")
        plt.title("Original data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(orig_data, bins=7)
        plt.axvline(int(orig_data.mean()), color='k', linestyle='dashed', linewidth=1)
        plt.tight_layout()

        plt.show()

    def extract_data(self):
        file_path = '/Users/hungvu/Desktop/E7130/e5/sampling-data/sampling.txt'
        data = pandas.read_csv(file_path, header=None)

        return data