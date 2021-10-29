import glob
import os
import re
import statistics as stat

import numpy as np
from matplotlib import pyplot as plt


class Ex4_Task1:
    def get_answers(self):
        packet_num = []
        byte_num = []
        byte_pairs = []
        flow_num = []
        flow_pairs = []

        raw_data = self.read_file()
        lists = self.sort_by_col(raw_data)

        # 3 lists from list_packets, list_bytes, list_flows
        for idx, list in enumerate(lists):
            # iterate through each list
            for pair, data_count in list:
                # get number of packets/bytes/flows, add to a list to calculate stats
                if idx == 0:
                    packet_num.append(data_count)
                elif idx == 1:
                    byte_num.append(data_count)
                    byte_pairs.append(pair)
                elif idx == 2:
                    flow_num.append(data_count)
                    flow_pairs.append(pair)

        # Packets
        print("Calculating stats based on PACKETS")
        self.cal_stats(packet_num)
        # Bytes
        print("Calculating stats based on BYTES")
        self.cal_stats(byte_num)
        # get top 10
        print("Top 10 pairs sorted by BYTES")
        self.get_top_n_pair(byte_pairs, byte_num, 10)
        # Flow
        print("Calculating stats based on FLOWS")
        self.cal_stats(flow_num)
        print("Top 10 pairs sorted by FLOWS")
        self.get_top_n_pair(flow_pairs, flow_num, 10)

        self.plot(flow_pairs[:100], flow_num[:100])

    def plot(self, pairs, data):
        # Linear scale
        plot = plt.figure("Linear scale - Task 1.III")
        plt.title("Linear scale - Number of flows")
        plt.xlabel("Pairs")
        plt.ylabel("Number of flows")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.bar(pairs, data, linestyle='solid')

        # Logarithm scale
        plot = plt.figure("Logarithmic scale - Task 1.III")
        plt.title("Logarithmic scale - Number of flows")
        plt.xlabel("Pairs")
        plt.ylabel("Number of flows")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.bar(pairs, np.log(data), linestyle='solid')

        plt.show()

    def read_file(self):
        raw_data = []
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/e4/out", "*.t2"))
        for file_path in file_list:
            with open(file_path) as f_input:
                lines = f_input.readlines()
                for line in lines:
                    raw_data.append(line)
        return raw_data

    def sort_by_col(self, raw_data):
        # col number 7, 8, 9 from crl_flow output
        # 7: packets, 8: bytes, 9: flows
        columns = [7, 8, 9]
        lists_sorted_list = []

        for col in columns:
            pairs = {}
            for line in raw_data:
                if line == '\n' or line[0] == '#':
                    continue
                l = re.split('\t', line[:-1])
                src = l[0]
                dst = l[1]
                # sort packets, 7th column => index 6th
                # sort bytes, 8th column => index 7th
                # sort flow, 9th column => index 8th
                val = l[col - 1]
                pair = ''
                if src < dst:
                    pair = src + ',' + dst
                else:
                    pair = dst + ',' + src
                if pair in pairs:
                    pairs[pair] += int(val)
                else:
                    pairs[pair] = int(val)

            sorted_dict = sorted(pairs.items(), key=lambda x: x[1], reverse=True)
            list_sort = list(sorted_dict)
            lists_sorted_list.append(list_sort)

        return lists_sorted_list

    def cal_stats(self, sorted_data):
        # return max, min, med, mean
        sum_element = sum(sorted_data)
        min_element = min(sorted_data)
        max_element = max(sorted_data)
        mean = sum_element/len(sorted_data)
        median = stat.median(sorted_data)
        print("Sum = " + str(sum_element))
        print("Min = " + str(min_element))
        print("Max = " + str(max_element))
        print("Mean = " + str(mean))
        print("Median = " + str(median) + '\n')

    def get_top_n_pair(self, pairs, data_count, number_of_result):
        for idx in range(number_of_result):
            print(str(idx + 1) + '\t' + pairs[idx] + '\t' + str(data_count[idx]))