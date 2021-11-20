import numpy as np
import pandas
from matplotlib import pyplot as plt
import seaborn as sns


class FT1_PS1:
    def plot(self):
        orig_data, ports, vol_1, vol_2, max_bins, stats = self.extract_data()

        # 1.1
        hist = plt.figure("1.1. Port distribution")
        plt.hist(ports, bins='auto', log=True)
        plt.title("Port distribution")
        plt.xlabel("Port number")
        plt.ylabel("Freq")

        # 1.2 - 60s
        plot12_1 = plt.figure("1.2. Traffic Volume - 60s")
        plt.plot(vol_1)
        plt.title("Traffic Volume - 60s")
        plt.xlabel("Time")
        plt.ylabel("Traffic bytes/60s")

        # 1.2 - 1800s
        plot12_2 = plt.figure("1.2. Traffic Volume - 1800s")
        plt.plot(vol_2)
        plt.title("Traffic Volume - 1800s")
        plt.xlabel("Time")
        plt.ylabel("Traffic bytes/1800s")

        # 1.3
        hist13 = plt.figure("1.3. Packet length distribution")
        plt.hist(orig_data['len'], bins=max_bins, log=True)
        plt.title("Packet length distribution")
        plt.xlabel("Packet length")
        plt.ylabel("Freq")

        # ecdf
        plot_ecdf = plt.figure("1.3. Empirical Cumulative Distribution")
        X, y = self.ecdf(orig_data['len'])
        plt.plot(X, y, marker='.', linestyle='none')
        plt.title("Empirical Cumulative Distribution")
        plt.xlabel("Packet length")
        plt.ylabel("Proportion")

        # 1.3 key stats
        stat_plot = plt.figure("1.3. Statistics Summary")
        stats.reset_index(inplace=True)
        plt.plot(stats.iloc[:, 0].values, stats['len_log'].values)
        plt.title("Statistics Summary")
        # other ways to plot
        # stats.plot(kind='line', x='index', y='len_log')
        # sns.catplot(x='index', y='len_log', data=stats)

        # plt.tight_layout()
        plt.show()

    def extract_data(self):
        ps1 = '/Users/hungvu/Desktop/E7130/final/out/ps1'
        col_name = ['tcp.sp', 'tcp.dp', 'udp.sp', 'udp.dp', 'len', 'time']
        data = pandas.read_csv(ps1, sep=',', names=col_name)

        # 1.1
        ports = []

        for col in data.columns[:4]:
            for port in data[col].dropna().values:
                ports.append(int(port))

        # 1.2
        start_1 = data['time'].values[0]
        start_2 = data['time'].values[0]
        # traffic vol for time scale 1 and 2
        bytes_1 = []
        bytes_2 = []
        byte_1_interval = 0
        bytes_2_interval = 0

        # time scale 1 - interval = 1m = 60s
        for idx, time in enumerate(data['time']):
            if time <= start_1 + 60:
                byte_1_interval = byte_1_interval + data['len'].values[idx]
            else:
                bytes_1.append(byte_1_interval)
                start_1 = data['time'].values[idx]
                byte_1_interval = 0

        # time scale 2 - interval = 30m = 1800s
        for idx, time in enumerate(data['time']):
            if time <= start_2 + 1800:
                bytes_2_interval = bytes_2_interval + data['len'].values[idx]
            else:
                bytes_2.append(bytes_2_interval)
                start_2 = data['time'].values[idx]
                bytes_2_interval = 0

        # 1.3
        # key statistics
        stat = data.describe()
        stat['len_log'] = np.log(stat['len'])
        # for performance check
        # start_time = timeit.default_timer()
        # elapsed = timeit.default_timer() - start_time
        # print(elapsed)
        return data, ports, bytes_1, bytes_2, data['len'].max(), stat

    # ECDF function to generate x and y axis data
    def ecdf(self, xdata):
        xdataecdf = np.sort(xdata)
        ydataecdf = np.arange(1, len(xdata) + 1) / len(xdata)
        return xdataecdf, ydataecdf
