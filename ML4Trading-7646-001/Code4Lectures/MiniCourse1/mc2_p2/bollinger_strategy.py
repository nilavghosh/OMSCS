
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def show_bollinger():
    start_date = '2007-12-31'
    end_date = '2009-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = list(set(["IBM"]))
    adjclose = get_data(symbols, dates)  # automatically adds SPY
    stock='IBM'

    # Get the 20 day moving avg and moving stddev
    movavg = pd.rolling_mean(adjclose,20,min_periods=20)
    movstddev = pd.rolling_std(adjclose, 20, min_periods=20)
    
    # Compute the upper and lower bollinger bands
    upperband = movavg + 2 * movstddev
    lowerband = movavg - 2 * movstddev
    
    # Plot the adjclose, movingavg, upper and lower bollinger bands
    plt.clf()
    
    plt.plot(adjclose.index,adjclose[stock].values)
    plt.plot(adjclose.index,movavg[stock].values)
    plt.plot(adjclose.index,upperband[stock].values)
    plt.plot(adjclose.index,lowerband[stock].values)
    plt.xlim(adjclose.index[0], adjclose.index[len(adjclose.index) - 1])
    plt.legend(['IBM','Moving Avg.','Upper Bollinger Band','Lower Bollinger Band'], loc='lower right')
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')

    longbuy = False
    shortbuy = False
    datelen = len(movavg);
    count = 0;
    orders = []
    for i in range(19,datelen-1):
        date = adjclose.index[i]
        
        if(adjclose.ix[i,"IBM"] < lowerband.ix[i,"IBM"] and adjclose.ix[i+1,"IBM"] > lowerband.ix[i+1,"IBM"]):
            if(longbuy == False and shortbuy == False):
                count += 1
                plt.axvline(adjclose.index[i+1], color='g')
                orders.append([adjclose.index[i+1],stock,"BUY",100])
                longbuy = True
        if(adjclose.ix[i,"IBM"] < movavg.ix[i,"IBM"] and adjclose.ix[i+1,"IBM"] > movavg.ix[i+1,"IBM"]):
            if(longbuy == True):
                count += 1
                plt.axvline(adjclose.index[i+1], color='black')
                orders.append([adjclose.index[i+1],stock,"SELL",100])
                longbuy = False
           
        if(adjclose.ix[i,"IBM"] > upperband.ix[i,"IBM"] and adjclose.ix[i+1,"IBM"] < upperband.ix[i+1,"IBM"]):
            if(longbuy == False and shortbuy == False):
                count += 1
                plt.axvline(adjclose.index[i+1], color='r')
                orders.append([adjclose.index[i+1],stock,"SELL",100])
                shortbuy = True
        if(adjclose.ix[i,"IBM"] > movavg.ix[i,"IBM"] and adjclose.ix[i+1,"IBM"] < movavg.ix[i+1,"IBM"]):
            if(shortbuy == True):
                count += 1
                plt.axvline(adjclose.index[i+1], color='black')
                orders.append([adjclose.index[i+1],stock,"BUY",100])
                shortbuy = False
        
    #now perform analysis on open/close based on date, etc..
    ordersnp = np.array(orders)
    ordersDataFrame = pd.DataFrame(ordersnp[0:,1:], index=ordersnp[0:,0])

    ordersDataFrame.columns = ['Symbol','Order','Shares']
    ordersDataFrame.index.name = 'Date'
    #adjclose.index.name = "Date"
    ordersDataFrame.to_csv("C:\Users\Nilav\Documents\orders_mc2_p2.csv")
    #adjclose.plot();
    plt.show()


def get_data(symbols, dates, addSPY=True):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if addSPY and 'SPY' not in symbols: # add SPY for reference, if absent
        symbols = ['SPY'] + symbols

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        #df= df.dropna(subset=["IBM"])
        #df= df.fillna()
        #df= df.fillna(method='backfill')
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
    return df


if __name__ == "__main__":
    show_bollinger()