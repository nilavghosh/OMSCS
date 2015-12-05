import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import KNNLearner as knn
matplotlib.style.use('ggplot')

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_Features(s_date, e_date, stock_name):
    start_date = s_date
    end_date = e_date
    stock = stock_name
    dates = pd.date_range(start_date, end_date)
    symbols = list(set([stock]))
    adjclose = get_data(symbols, dates)  # automatically adds SPY
    adjclose = adjclose[stock].to_frame()
    
    # Get the 20 day moving avg and moving stddev
    movavg = pd.rolling_mean(adjclose,20,min_periods=20)
    movstddev = pd.rolling_std(adjclose, 20, min_periods=20)
    
    # Compute the upper and lower bollinger bands
    upperband = movavg + 2 * movstddev
    lowerband = movavg - 2 * movstddev

    normalized_bbValue = (adjclose - movavg) / (2 * movstddev)
    normalized_momentum = (adjclose / adjclose.shift(5)) - 1
    daily_returns = (adjclose[1:] / adjclose[:-1].values) - 1.0
    daily_returns.ix[0] = 0.0

    normalized_vol = pd.rolling_std(daily_returns,5, min_periods=5)

    normalized_features = adjclose
    normalized_features[stock+"-N"] = adjclose[stock] - np.mean(adjclose[stock])
    #pd.DataFrame(index = adjclose.index.get_values())
    
    normalized_features["BB"] = normalized_bbValue
    normalized_features["Momentum"] = normalized_momentum
    range = normalized_vol[stock].max() - normalized_vol[stock].min()
    normalized_features["Volatility"] = ((normalized_vol-normalized_vol[stock].min())/range)*2 - 1
    RET5D = ((adjclose.shift(-5)/adjclose)-1)*100
    normalized_features["Training Y"] = RET5D[stock]
    return normalized_features



def applyStrategy():
    stock = "IBM"
    train_features = get_Features('2008-1-1','2009-12-31', stock)
    learner = knn.KNNLearner(3)
    learner.addEvidence(train_features[["BB","Momentum","Volatility"]].values,  train_features["Training Y"]) 

    test_features = get_Features('2010-1-1','2010-12-31', stock)
    test_features["Predicted Y"] = learner.query(test_features[["BB","Momentum","Volatility"]].values)

    test_features[["Volatility"]].plot()
    plt.show()

    longbuy = False
    shortbuy = False
    count = 0;
    orders = []
    datelen = len(test_features)
    for i in range(19,datelen-1):
        date = test_features.index[i]
        if(test_features.ix[i,"Predicted Y"] > 0):
            if(longbuy == False and shortbuy == False):
                count += 1
                plt.axvline(test_features.index[i+1], color='g')
                orders.append([test_features.index[i+1],stock,"BUY",100])
                longbuy = True

        if(test_features.ix[i,"Predicted Y"] < 0):
            if(longbuy == True):
                count += 1
                plt.axvline(test_features.index[i+1], color='black')
                orders.append([test_features.index[i+1],stock,"SELL",100])
                longbuy = False
                continue

        if(test_features.ix[i,"Predicted Y"] < 0):
            if(longbuy == False and shortbuy == False):
                count += 1
                plt.axvline(test_features.index[i+1], color='r')
                orders.append([test_features.index[i+1],stock,"SELL",100])
                shortbuy = True

        if(test_features.ix[i,"Predicted Y"] > 0):
            if(shortbuy == True):
                count += 1
                plt.axvline(test_features.index[i+1], color='black')
                orders.append([test_features.index[i+1],stock,"BUY",100])
                shortbuy = False

    #now perform analysis on open/close based on date, etc..
    ordersnp = np.array(orders)
    ordersDataFrame = pd.DataFrame(ordersnp[0:,1:], index=ordersnp[0:,0])

    ordersDataFrame.columns = ['Symbol','Order','Shares']
    ordersDataFrame.index.name = 'Date'
    ordersDataFrame.to_csv("C:\Users\Nilav\Documents\ml_mc3_p2_IBM_test.csv")
    test_features[stock].plot(color='c')
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
    applyStrategy()