import datetime as dt
from datetime import datetime
from datetime import date
from datetime import timedelta
import os
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import sys

style.use('ggplot')
# get stock data for a given length of time
def get_stock_data(period=10, ticker='AKAM'):
    today = date.today()
    day = timedelta(days=1)
    start = today.replace(year=today.year - period)
    end = datetime.today() - timedelta(days=1)
    df = web.get_data_yahoo(ticker, start, end)
    return df

if len(sys.argv) == 2:
    # get input arguemnts
    input_ticker = sys.argv[0]
    input_time = sys.argv[1]
    retdf = get_stock_data(input_time,input_ticker)
    # create rolling average of data
    retdf['100ma'] = retdf['Adj Close'].rolling(window=100, min_periods=0).mean()
    # add two plot axis to the plot
    ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
    ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1, sharex=ax1)
    # supply two streams of data and bar chart to the plot
    ax1.plot(retdf.index,retdf['Adj Close'])
    ax1.plot(retdf.index,retdf['100ma'])
    ax2.bar(retdf.index,retdf['Volume'])
    # display the plot
    plt.show()
else:
    print('invalid arguments supplied')
