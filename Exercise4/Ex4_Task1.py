import glob
import os
import re


class Ex4_Task1:
    def get_answers(self):
        raw_data = self.read_file()
        lists = self.sort_by_col(raw_data)

        # 3 lists from list_packets, list_bytes, list_flows
        for list in lists:
            # iterate through each list
            for element in list:
                # get number of packets/bytes/flows, add to a list to calculate stats
                print(element[1])


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
        pass
