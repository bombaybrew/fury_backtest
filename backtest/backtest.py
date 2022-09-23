import numpy as np
import pandas as pd

class Backtest:

    def __init__(self):
        self.stock_df = pd.DataFrame()

    def init_data(self, stock_name):
        # read from csv file
        self.stock_df = pd.read_csv('./data/sandbox/' + stock_name +'.csv')
        self.stock_df.dropna(inplace=True)
        print(self.stock_df)
        return 0

    def run(self):
        self.stock_df['Signal'] = self.stock_df['Adj Close'].rolling(20).mean() - self.stock_df['Adj Close'].rolling(100).mean()
        self.stock_df['Position'] = (self.stock_df['Signal'].apply(np.sign) + 1)/2

        print(self.stock_df)