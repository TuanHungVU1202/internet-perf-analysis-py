import pandas
from matplotlib import pyplot as plt

class FT1_PS3:
    def plot(self):
        orig_data = self.extract_data()

        # 1.1
        hist = plt.figure("1.1. Port distribution")
        # plt.hist(ports, bins='auto', log=True)
        plt.title("Port distribution")
        plt.xlabel("Port number")
        plt.ylabel("Freq")

        # plt.show()


    def extract_data(self):
        ps3 = '/Users/hungvu/Desktop/E7130/final/out/ps3.csv'
        # col_name = ['tcp.sp', 'tcp.dp', 'udp.sp', 'udp.dp', 'len', 'time']
        data = pandas.read_csv(ps3, sep=',', skiprows=10)
        filtered = data.loc[:, data.columns.str.startswith('RTT')]
        print(filtered)
        return data
