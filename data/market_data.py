import pandas as pd

class MarketData:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath, parse_dates=['Date'])
        self.df.set_index('Date', inplace=True)

    def get_spot(self, date):
        return self.df.loc[date, 'Spot']

    def get_vol(self, date):
        return self.df.loc[date, 'Vol']
