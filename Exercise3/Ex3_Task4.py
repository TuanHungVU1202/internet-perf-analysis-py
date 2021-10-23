import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Ex3_Task4:
    def plot(self):
        print("E3_Task4")
        data = self.extract_data()
        sns.set(style="ticks", color_codes=True)
        # sns.pairplot(data, hue="Time")
        sns.pairplot(data)
        # pd.plotting.scatter_matrix(data, alpha=0.2)
        # sns.pairplot(data, vars=["Time", "RXbytes", "RXpackets"], hue="RXbytes")
        plt.show()

    def extract_data(self):
        df = pd.read_csv("Exercise3/r-data/bytes.csv")
        df['Time'] = pd.to_datetime(df['Time'])
        # print(type(df["Time"].values[0]))
        return df

