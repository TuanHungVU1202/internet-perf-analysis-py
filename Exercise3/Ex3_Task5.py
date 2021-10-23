import numpy as np
import pandas as pd


class Ex3_Task5:
    def plot(self):
        print("E3_Task4")
        self.extract_data()

    def extract_data(self):
        # read data file to pandas series, separate by the \t
        # remove NaN using dropna()
        df = pd.read_csv("Exercise3/r-data/flowdata_unclean.txt", sep='\\t', engine='python').dropna()
        # adding new column "Y", checking condition if bytes <50
        # return 0 if condition is true, 1 if false
        df["Y"] = np.where(df["bytes"] < 50, 0, 1)
        print(df)
