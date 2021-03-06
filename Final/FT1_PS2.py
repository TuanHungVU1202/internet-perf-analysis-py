import glob
import os

import numpy as np
from fitter import Fitter, get_common_distributions
from geolite2 import geolite2
import pandas
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


class FT1_PS2:
    def plot(self):
        orig_data, ports, vol_1, vol_2, countries, stats, sorted_bytes, sorted_flows, flow_count = self.extract_data()

        # 1.4
        hist = plt.figure("1.4. Port distribution")
        port = list(ports.keys())
        pkt = list(ports.values())
        plt.scatter(port, pkt)
        plt.title("Port distribution")
        plt.xlabel("Port number")
        plt.ylabel("Number of packets")

        # 1.4
        hist_log = plt.figure("1.4. Port distribution - Log Scale")
        plt.scatter(port, np.log(pkt))
        plt.title("Port distribution - Log Scale")
        plt.xlabel("Port number")
        plt.ylabel("Number of packets - Log")

        # 1.5 - 1s
        plot15_1 = plt.figure("1.5. Traffic Volume - 1s")
        plt.plot(vol_1,  marker='.')
        plt.title("Traffic Volume - 1s")
        plt.xlabel("Time")
        plt.ylabel("Traffic bytes/s")

        # 1.5 - 60s
        plot15_2 = plt.figure("1.5. Traffic Volume - 60s")
        plt.plot(vol_2,  marker='.')
        plt.title("Traffic Volume - 60s")
        plt.xlabel("Time")
        plt.ylabel("Traffic bytes/60s")

        # 1.6
        hist_countries = plt.figure("1.6. Flow distribution - Countries")
        plt.hist(countries, bins='auto', log=True)
        plt.title("Flow distribution - Countries")
        plt.xlabel("Countries")
        plt.xticks(rotation=45)
        plt.ylabel("Freq")

        # 1.7
        plot17_flow = plt.figure("1.7. Pairs Distribution by Flows - Zipf")
        plt.plot(range(len(sorted_flows)), sorted_flows,  marker='.')
        plt.title("Pairs Distribution by Flows - Zipf")
        plt.xlabel("Rank")
        plt.ylabel("Flows - Log")

        plot17_bytes = plt.figure("1.7. Pairs Distribution by Bytes - Zipf")
        plt.plot(range(len(sorted_bytes)), sorted_bytes, marker='.')
        plt.title("Pairs Distribution by Bytes - Zipf")
        plt.xlabel("Rank")
        plt.ylabel("Bytes - Log")

        # 1.8
        # flow length = total number of bytes in a flow
        hist_flowlen = plt.figure("1.8. Flow length distribution")
        plt.hist(np.log(orig_data['bytes']), bins='auto')
        plt.title("Flow length distribution - Log scale")
        plt.xlabel("Flow length")
        plt.ylabel("Freq")

        # 1.8 ecdf
        plot_ecdf = plt.figure("1.8. Empirical Cumulative Distribution")
        X, y = self.ecdf(np.log(orig_data['bytes']))
        plt.plot(X, y, marker='.', linestyle='none')
        plt.title("ECDF")
        plt.xlabel("Flow length")
        plt.ylabel("Proportion")

        # 1.8 key stats
        stat_plot = plt.figure("1.8. Statistics Summary")
        stats.reset_index(inplace=True)
        plt.plot(stats.iloc[:, 0].values, stats['bytes_log'].values,  marker='.')
        plt.title("Statistics Summary")

        # 1.10
        plot110_count = plt.figure("1.10. Number of Flows each timeout")
        timeouts = [1, 10, 60, 120, 1800]
        plt.plot(np.log(timeouts), np.log(flow_count),  marker='.')
        plt.title("Number of Flows each timeout")
        plt.xlabel("Timeout Period - Log")
        plt.ylabel("Number of Flows - Log")

        plt.show()

    def extract_data(self):
        # raw_data appended from file
        raw_data = self.read_file()
        # write file if needed
        # self.write_file()

        # 1.4
        file_path = '/Users/hungvu/Desktop/E7130/final/out/ps2_raw'
        col_names = ["src", "dst", "proto", "valid", "sport", "dport", "pkt", "bytes", "flows",
                     "start", "end"]
        # 21962 rows x 11 cols
        data = pandas.read_csv(file_path, sep='\t', names=col_names)

        ports_pkt = {}
        for col in data.columns[4:6]:
            for port in data[col].values:
                pkt = data.loc[data[col] == port, 'pkt'].values[0]
                if port in ports_pkt:
                    ports_pkt[port] = ports_pkt.get(port) + pkt
                else:
                    ports_pkt[port] = pkt

        # 1.5
        start_1 = data['end'].values[0]
        start_2 = data['end'].values[0]
        # traffic vol for time scale 1 and 2
        bytes_1 = []
        bytes_2 = []
        byte_1_interval = 0
        bytes_2_interval = 0

        # time scale 1 - interval = 1s
        for idx, time in enumerate(data['end']):
            if time <= start_1 + 1:
                byte_1_interval = byte_1_interval + data['bytes'].values[idx]
            else:
                bytes_1.append(byte_1_interval)
                start_1 = data['end'].values[idx]
                byte_1_interval = 0

        # time scale 2 - interval = 60s
        for idx, time in enumerate(data['end']):
            if time <= start_2 + 60:
                bytes_2_interval = bytes_2_interval + data['bytes'].values[idx]
            else:
                bytes_2.append(bytes_2_interval)
                start_2 = data['end'].values[idx]
                bytes_2_interval = 0

        # combine flows
        columns = ["pkt", "bytes", "flows"]
        combine_flows = self.combine_flow(data, columns[2])
        combine_bytes = self.combine_flow(data, columns[1])
        combine_pkt = self.combine_flow(data, columns[0])

        # 1.6
        # sc = src country, dc = dst country
        sc = []
        dc = []
        for ip in data['src']:
            country = self.find_country_from_ip(ip)
            sc.append(country)

        for ip in data['dst']:
            country = self.find_country_from_ip(ip)
            dc.append(country)

        data['sc'] = sc
        data['dc'] = dc
        countries = data['sc'].append(data['dc']).dropna()

        # 1.7 Sort and get log scale of values
        log_bytes = np.log(list(combine_bytes.values()))
        log_flows = np.log(list(combine_flows.values()))
        sorted_bytes = np.sort(log_bytes)[::-1]
        sorted_flows = np.sort(log_flows)[::-1]
        # sorted_flows = sorted(combine_flows.items(), key=lambda x: x[1], reverse=True)
        # sorted_bytes = sorted(combine_bytes.items(), key=lambda x: x[1], reverse=True)

        # 1.8
        # key statistics
        stat = data.describe()
        stat['bytes_log'] = np.log(stat['bytes'])

        # 1.9
        train, test = train_test_split(data['bytes'], test_size=0.4)
        fit_train = Fitter(train,
                           distributions=get_common_distributions())
        fit_test = Fitter(test,
                          distributions=get_common_distributions())
        fit_train.fit()
        print("Summary fitting")
        print(fit_train.summary())
        print("Parameters: " + str(fit_train.get_best(method='sumsquare_error')))

        fit_test.fit()
        print("Summary Evaluating")
        print(fit_test.summary())
        print("Parameters: " + str(fit_test.get_best(method='sumsquare_error')))

        # 1.10
        timeouts = [1, 10, 60, 120, 1800]
        flow_count = []
        for val in timeouts:
            no_flows = self.count_flow(val)
            flow_count.append(no_flows)

        return data, ports_pkt, bytes_1, bytes_2, countries, stat, sorted_bytes, sorted_flows, flow_count

    def read_file(self):
        raw_data = []
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/final/out", "*.t2"))
        for file_path in file_list:
            with open(file_path) as f_input:
                lines = f_input.readlines()
                for line in lines:
                    raw_data.append(line)
        return raw_data

    def write_file(self):
        raw_data = self.read_file()
        f = open("/Users/hungvu/Desktop/E7130/final/out/ps2_raw", "a")
        for line in raw_data:
            if line == '\n' or line[0] == '#':
                continue
            # write file
            f.write(line)
        f.close()

    def combine_flow(self, data, col_name):
        pairs = {}
        for row in data.itertuples():
            src = row.src
            dst = row.dst
            if col_name == "pkt":
                val = row.pkt
            elif col_name == "bytes":
                val = row.bytes
            elif col_name == "flows":
                val = row.flows
            pair = ''
            if src < dst:
                pair = src + ',' + dst
            else:
                pair = dst + ',' + src
            if pair in pairs:
                pairs[pair] += int(val)
            else:
                pairs[pair] = int(val)

        return pairs

    def find_country_from_ip(self, ip):
        geo = geolite2.reader()
        try:
            country = geo.get(ip)
        except ValueError:  # Faulty IP value
            return np.nan
        try:
            return country['country']['names']['en'] if country is not None else np.nan
        except KeyError:  # Faulty Key value
            return np.nan

        return country

    # ECDF function to generate x and y axis data
    def ecdf(self, xdata):
        xdataecdf = np.sort(xdata)
        ydataecdf = np.arange(1, len(xdata) + 1) / len(xdata)
        return xdataecdf, ydataecdf

    # 1.10
    def count_flow(self, timeout):
        raw_data = []
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/final/out", "tf" + str(timeout) + "*.t2"))
        for file_path in file_list:
            with open(file_path) as f_input:
                lines = f_input.readlines()
                for line in lines:
                    raw_data.append(line)
        return len(raw_data)
