import glob
import os

import pandas as pd


class Ex4_Task4:
    def get_answers(self):
        self.read_file()

    def read_file(self):
        file_list = glob.glob(os.path.join(os.getcwd(), "/Users/hungvu/Desktop/E7130/e4/out", "*.csv"))
        for file_path in file_list:
            print(file_path)
            data = pd.read_csv(file_path)
            sum_rtt = data['ICMP Response Time'].sum()
            print(sum_rtt)
