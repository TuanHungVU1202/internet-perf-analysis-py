import pandas
import pandas as pd
from matplotlib import pyplot as plt


class FT3_AS1:
    def plot(self):
        as1, as1_lost = self.extract_data()

        # 3.1
        # boxplot_no_lost = plt.figure("3.1 Successful latency measurements")
        for column in as1:
            plt.figure('3.1 Successful latency - Dataset ' + column)
            col_plot = as1.boxplot([column])
            col_plot.set_ylabel("ms")

        plt.figure('3.1 Successful latency measurements - All Datasets')
        ax = as1.boxplot()
        ax.set_xlabel("Dataset")
        ax.set_ylabel("ms")

        plt.show()

    def extract_data(self):
        col_names = ["d1", "d2", "d3", "n1", "n2", "n3", "r1", "r2", "r3", "i1", "i2"]
        as1 = pd.DataFrame(columns=col_names)

        sub_col_name = ["delay"]
        for col in col_names:
            path = '/Users/hungvu/Desktop/E7130/final/out/AS1.' + col
            df = pandas.read_csv(path, header=None, names=sub_col_name)
            as1[col] = pd.Series(df[sub_col_name[0]])

        col_names_lost = ["n1", "n2", "n3", "r1", "r2", "r3", "i1", "i2"]
        as1_lost = pd.DataFrame(columns=col_names_lost)
        for col in col_names_lost:
            path = '/Users/hungvu/Desktop/E7130/final/out/AS1.' + col + '.lost'
            df = pandas.read_csv(path, header=None, names=sub_col_name)
            as1_lost[col] = pd.Series(df[sub_col_name[0]])

        return as1, as1_lost