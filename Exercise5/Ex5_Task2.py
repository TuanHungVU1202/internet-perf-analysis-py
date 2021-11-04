import statistics
from statistics import mean

import pandas
import pylab
from matplotlib import pyplot as plt
from scipy import stats


class Ex5_Task2:
    def plot(self):
        orig_data, list_10k_nsize = self.extract_data()

        # 1. original data
        orig_plot = plt.figure("1. Original")
        plt.title("Original data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(orig_data, bins='auto')
        plt.axvline(int(orig_data.mean()), color='k', linestyle='dashed', linewidth=1)
        plt.text(int(orig_data.mean()) + 5000, 800, "Mean= " + str(orig_data.mean().item()))

        # 2. 5000 samples
        plot_5k = plt.figure("2. 5000 Samples")
        samples_5k = orig_data.sample(5000)
        plt.title("5000 samples data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(samples_5k, bins='auto')
        plt.axvline(int(samples_5k.mean()), color='k', linestyle='dashed', linewidth=1)
        plt.text(int(samples_5k.mean()) + 5000, 400, "Mean= " + str(samples_5k.mean().item()))

        # 3. 10000 samples - Size 5
        plot_10k_5 = plt.figure("3. 10000 Samples - Size 5")
        sampl_10k_5 = list_10k_nsize[0]
        mean_size_5 = mean(sampl_10k_5)
        plt.title("10000 Samples - Size 5")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(sampl_10k_5, bins='auto')
        plt.axvline(mean_size_5, color='k', linestyle='dashed', linewidth=1)
        plt.text(mean_size_5 + 5000, 400, "Mean= " + str(mean_size_5))
        plt.text(mean_size_5 + 5000, 380, "Standard Deviations= " + str(statistics.stdev(sampl_10k_5)))
        # Q-Q plot against normal dist - 10k-5
        plot_10k_5_qq = plt.figure("3. QQ plot 10000 Samples - Size 5")
        stats.probplot(sampl_10k_5, dist="norm", plot=pylab)

        # 4. 10000 samples - Size 10
        plot_10k_10 = plt.figure("4. 10000 Samples - Size 10")
        sampl_10k_10 = list_10k_nsize[1]
        mean_size_10 = mean(sampl_10k_10)
        plt.title("10000 Samples - Size 10")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(sampl_10k_10, bins='auto')
        plt.axvline(mean_size_10, color='k', linestyle='dashed', linewidth=1)
        plt.text(mean_size_10 + 5000, 400, "Mean= " + str(mean_size_10))
        plt.text(mean_size_10 + 5000, 380, "Standard Deviations= " + str(statistics.stdev(sampl_10k_10)))
        plot_10k_10_qq = plt.figure("4. QQ plot 10000 Samples - Size 10")
        stats.probplot(sampl_10k_10, dist="norm", plot=pylab)

        # 5. 10000 samples - Size 100
        plot_10k_100 = plt.figure("5. 10000 Samples - Size 100")
        sampl_10k_100 = list_10k_nsize[2]
        mean_size_100 = mean(sampl_10k_100)
        plt.title("10000 Samples - Size 100")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(sampl_10k_100, bins='auto')
        plt.axvline(mean_size_100, color='k', linestyle='dashed', linewidth=1)
        plt.text(mean_size_100 + 5000, 400, "Mean= " + str(mean_size_100))
        plt.text(mean_size_100 + 5000, 380, "Standard Deviations= " + str(statistics.stdev(sampl_10k_100)))
        plot_10k_100_qq = plt.figure("5. QQ plot 10000 Samples - Size 100")
        stats.probplot(sampl_10k_100, dist="norm", plot=pylab)

        pylab.show()
        plt.show()

    def extract_data(self):
        file_path = '/Users/hungvu/Desktop/E7130/e5/sampling-data/sampling.txt'
        data = pandas.read_csv(file_path, header=None)

        # loop 10k times for each size below
        # get mean of each run (in each size)
        # => get 10k means value from above, these are 10k needed samples
        total_list = []
        sizes = [5, 10, 100]
        number_samples = 10000

        for size in sizes:
            tmp_lst = []
            for idx in range(number_samples):
                tmp_lst.append(int(data.sample(5).mean()))

            total_list.append(tmp_lst)

        return data, total_list
