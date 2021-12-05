import pandas
import pandas as pd
from matplotlib import pyplot as plt
from IPython.display import display
from scipy import stats
from scipy.stats.mstats import gmean


class FT3_AS1:
    def plot(self):
        as1, as1_lost, combine, as2 = self.extract_data()
        nameserver = ["d1", "d2", "d3", "n1", "n2", "n3"]
        re_iperf = ["r1", "r2", "r3", "i1", "i2"]

        # 3.1.1
        # boxplot_no_lost = plt.figure("3.1 Successful latency measurements")
        for column in as1:
            plt.figure('3.1 Successful latency - Dataset ' + column)
            col_plot = as1.boxplot([column])
            col_plot.set_ylabel("ms")

        # 3.1.2
        # Lost packets
        for column in as1_lost:
            plt.figure('3.1 Lost packet - Dataset ' + column)
            col_plot = as1_lost.boxplot([column])
            col_plot.set_ylabel("ms")

        plt.figure('3.1 Successful latency measurements - All Datasets')
        ax = as1.boxplot()
        ax.set_xlabel("Dataset")
        ax.set_ylabel("ms")

        # 3.1.3
        # PDF and CDF
        for column in combine:
            plt.figure('3.1.3 PDF and CDF - Dataset ' + column)
            plt.title('PDF and CDF - Dataset ' + column)
            plt.hist(combine[column], density=True, cumulative=False, label='pdf')
            plt.hist(combine[column], density=True, cumulative=True, label='cdf')
            plt.legend()

        # 3.2
        # times = [(datetime.datetime(2017, 7, 17, 11, 00, 0) + datetime.timedelta(minutes=60 * x)).time() for x in
        #          range(len(as1[col]))]
        for col in nameserver:
            plt.figure('3.2 Latency Time Series - Dataset ' + col)
            plt.plot(as1[col], linestyle='solid', marker='.')
            plt.title('Latency Time Series - Dataset ' + col)
            plt.xlabel('Time interval - 1 hour')
            plt.ylabel('Latency (ms)')

        for col in re_iperf:
            plt.figure('3.2 Latency Time Series - Dataset ' + col)
            plt.plot(as1[col], linestyle='solid', marker='.')
            plt.title('Latency Time Series - Dataset ' + col)
            plt.xlabel('Time interval - 10 minutes')
            plt.ylabel('Latency (ms)')

        # 3.2.2 Autocorrelation plot
        autocor_as1 = ["r3", "i1", "i2"]
        for col in autocor_as1:
            as1i2 = plt.figure("3.2 Autocorrelation plot - " + col)
            plt.title("3.2 Autocorrelation plot")
            plt.xlabel("Lag")
            plt.ylabel("Autocorrelation")
            pd.plotting.autocorrelation_plot(as1[col])

        # 3.3
        plt.figure('3.3 Throughput - All Datasets')
        ax = as2.boxplot()
        ax.set_xlabel("Dataset")
        ax.set_ylabel("bps")

        for column in as2:
            plt.figure('3.3 Throughput - Dataset ' + column)
            col_plot = as2.boxplot([column])
            col_plot.set_ylabel("bps")

        # 3.4.1
        for col in re_iperf[3::]:
            plt.figure('3.4 Throughput Time Series - Dataset ' + col)
            plt.plot(as2[col], linestyle='solid', marker='.')
            plt.title('Throughput Time Series - Dataset ' + col)
            plt.xlabel('Time interval - 1 hour')
            plt.ylabel('Throughput - bps')

        # 3.4.2 Autocorrelation plot
        for col in autocor_as1[1::]:
            as2ix = plt.figure("3.4. Autocorrelation plot - " + col)
            plt.title("3.4. Autocorrelation plot")
            plt.xlabel("Lag")
            plt.ylabel("Autocorrelation")
            pd.plotting.autocorrelation_plot(as2[col])

        plt.show()

    def extract_data(self):
        col_names = ["d1", "d2", "d3", "n1", "n2", "n3", "r1", "r2", "r3", "i1", "i2"]
        as1 = pd.DataFrame(columns=col_names)
        as2 = pd.DataFrame(columns=col_names[9:11])

        # 3.1.1
        sub_col_name = ["delay"]
        for col in col_names:
            path = '/Users/hungvu/Desktop/E7130/final/out/AS1.' + col
            df = pandas.read_csv(path, header=None, names=sub_col_name)
            as1[col] = pd.Series(df[sub_col_name[0]])

        # 3.1.2
        col_names_lost = ["n1.lost", "n2.lost", "n3.lost", "r1.lost", "r2.lost", "r3.lost", "i1.lost", "i2.lost"]
        as1_lost = pd.DataFrame(columns=col_names_lost)
        for col in col_names_lost:
            path = '/Users/hungvu/Desktop/E7130/final/out/AS1.' + col
            df = pandas.read_csv(path, header=None, names=sub_col_name)
            as1_lost[col] = pd.Series(df[sub_col_name[0]])

        as1_lost = as1_lost.fillna(0)
        as1_lost = as1_lost.replace(5, 400)

        combine = as1.append(as1_lost, ignore_index=True)

        # 3.1.4
        stat = as1.describe()
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.precision', 3)
        display(stat)

        # 3.2
        sub_col_name = ["bps"]
        for col in col_names[9:11]:
            path = '/Users/hungvu/Desktop/E7130/final/out/AS2.' + col
            df = pandas.read_csv(path, header=None, names=sub_col_name)
            as2[col] = pd.Series(df[sub_col_name[0]])

            # statistics
            bps_mean = as2[col].mean()
            bps_hmean = stats.hmean(as2[col])
            bps_geomean = gmean(as2[col])
            bps_median = as2[col].median()
            print(col + ": Mean= " + str(bps_mean))
            print(col + ": Harmonic Mean= " + str(bps_hmean))
            print(col + ": Geometric Mean= " + str(bps_geomean))
            print(col + ": Median= " + str(bps_median))


        return as1, as1_lost, combine, as2
