import glob
import os
import re


class Ex4_Task1:
    def calculate_stat(self):
        raw_data = self.read_file()
        sorted_data_list = self.sort_by_col(raw_data)
        print(sorted_data_list[0])

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
