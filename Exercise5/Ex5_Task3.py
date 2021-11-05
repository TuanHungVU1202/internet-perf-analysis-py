import pandas
from matplotlib import pyplot as plt
from fitter import Fitter, get_common_distributions, get_distributions


class Ex5_Task3:
    def plot(self):
        data_a, data_b, data_c = self.extract_data()

        # 1. distr A
        dist_a = plt.figure("A - Histogram")
        plt.title("A data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(data_a, bins=100)
        plt.tight_layout()

        # 2. distr b
        dist_b = plt.figure("B - Histogram")
        plt.title("B data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(data_b, bins=50)
        plt.tight_layout()

        # 3. distr c
        dist_c = plt.figure("C - Histogram")
        plt.title("C data")
        plt.xlabel("Bins")
        plt.ylabel("Frequency")
        plt.hist(data_c, bins=50)
        plt.tight_layout()

        plt.show()

    def extract_data(self):
        file_a = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_a.txt'
        file_b = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_b.txt'
        file_c = '/Users/hungvu/Desktop/E7130/e5/sampling-data/distr_c.txt'
        data_a = pandas.read_csv(file_a, header=None)
        data_b = pandas.read_csv(file_b, header=None)
        data_c = pandas.read_csv(file_c, header=None)

        # A - perato
        # B - lognorm
        # C - expon

        # Taking samples
        sample_a = data_a.sample(int(len(data_a) / 2))
        sample_b = data_b.sample(int(len(data_b) / 2))
        sample_c = data_c.sample(int(len(data_c) / 2))

        # fit_a = Fitter(data_a,
        #                distributions=get_common_distributions())
        fit_a = Fitter(data_a,
                       distributions=[
                           "cauchy",
                           "chi2",
                           "expon",
                           "exponpow",
                           "gamma",
                           "lognorm",
                           "norm",
                           "powerlaw",
                           "rayleigh",
                           "uniform",
                           "pareto", "weibull_max", "weibull_min"
                       ])
        fit_a.fit()
        print("Summary fitting A distribution")
        print(fit_a.summary())
        print("Parameters: " + str(fit_a.get_best(method='sumsquare_error')))

        fit_b = Fitter(data_b,
                       distributions=get_common_distributions())
        fit_b.fit()
        print("Summary fitting B distribution")
        print(fit_b.summary())
        print("Parameters: " + str(fit_b.get_best(method='sumsquare_error')))

        fit_c = Fitter(data_c,
                       distributions=get_common_distributions())
        fit_c.fit()
        print("Summary fitting C distribution")
        print(fit_c.summary())
        print("Parameters: " + str(fit_c.get_best(method='sumsquare_error')))
        return data_a, data_b, data_c
