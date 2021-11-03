import glob
import os

import pandas as pd


class Ex4_Task4:
    def get_answers(self):
        self.read_file()

    def read_file(self):
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/e4/out", "*csv"))
        for file_path in file_list:
            print(file_path)
            data = pd.read_csv(file_path)
            self.cal_stats(data)

    def cal_stats(self, raw_data):
        request_str = "Echo (ping) request"
        reply_str = "Echo (ping) reply"
        req = 0
        rep = 0

        for value in raw_data['Info'].values:
            if request_str in value:
                req += 1
            elif reply_str in value:
                rep += 1

        sum_rtt = raw_data['ICMP Response Time'].sum()

        print("Sum of Response time= " + str(sum_rtt))
        print("Average response time= " + str(sum_rtt/rep))
        print("Request packets= " + str(req))
        print("Reply packets= " + str(rep))
        print("Lost ratio= " + str(1 - rep/req) + "\n")

