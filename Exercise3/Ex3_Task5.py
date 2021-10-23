import numpy as np
import pandas as pd


class Ex3_Task5:
    def plot(self):
        print("E3_Task4")
        self.extract_data()

    def extract_data(self):
        df = pd.read_csv("Exercise3/r-data/flowdata_unclean.txt", sep='\\t', engine='python').dropna()
        df["Y"] = np.where(df["bytes"] < 50, 0, 1)
        print(df)
        # return df
