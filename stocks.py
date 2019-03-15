import numpy as np
import pandas as pd
import pandas_datareader as pdr
import fix_yahoo_finance as fyf

import matplotlib.pyplot as plt
%matplotlib inline
#data = fyf.download

'''
Two different ways to get data on Amazon stock price

fyf.pdr_override()
amzn = pdr.get_data_yahoo('AMZN', start = '2018-01-01')
amzn.head()

amzn = fyf.download('AMZN', start = '2018-01-01')
amzn.head()


stocks = ['AMZN', 'FB', 'GOOG', 'MSFT']

Two different ways to get data on stock prices for different companies (Amazon, Facebook, Google, Microsoft)

data = pdr.get_data_yahoo(stocks, start = '2018-01-01')
data.head()

data = fyf.download(stocks, start = '2018-01-01')
data.head()


#find first five data values specific to the closing price of the day. 'Close' can be replaced w/  open, high, low, etc.
data['Close'].head()

#find closing prices for a specific company. Close can be replaced w/ open, high, low, etc.
data['Close']['AMZN']
'''