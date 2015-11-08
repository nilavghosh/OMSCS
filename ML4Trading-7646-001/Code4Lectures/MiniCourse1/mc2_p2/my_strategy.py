
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def show_bollinger():
    IBM ='IBM'
    SPY = 'SPY'
    start_date = '2009-12-31'
    end_date = '2011-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = list(set([IBM]))
    adjclose = get_data(symbols, dates)  # automatically adds SPY
    

    #-----------------Bollinger Bands-------------------
    # Get the  day moving avg and moving stddev
    movavg = pd.rolling_mean(adjclose,20,min_periods=20)
    movstddev = pd.rolling_std(adjclose,20 , min_periods=20)
    # Compute the upper and lower bollinger bands
    upperband = movavg + 2 * movstddev
    lowerband = movavg - 2 * movstddev
    
    #-----------------Bollinger Bands-------------------
    # Get the 40 day moving avg and moving stddev
    #movavg40 = pd.rolling_mean(adjclose,40,min_periods=40)
    #movstddev40 = pd.rolling_std(adjclose, 40, min_periods=40)
    ## Compute the upper and lower bollinger bands
    #upperband40 = movavg + 2 * movstddev
    #lowerband40 = movavg - 2 * movstddev
    
      
    # Plot the adjclose, movingavg, upper and lower bollinger bands
    plt.clf()
    
    #plt.plot(adjclose.index,movavg[IBM].values)
    #plt.plot(adjclose.index,movavg40[SPY].values)
    #plt.legend([IBM, SPY])
    

   
    plt.plot(adjclose.index,adjclose[IBM].values)
    plt.plot(adjclose.index,movavg[IBM].values)
    plt.plot(adjclose.index,upperband[IBM].values)
    plt.plot(adjclose.index,lowerband[IBM].values)
    plt.xlim(adjclose.index[0], adjclose.index[len(adjclose.index) - 1])
    plt.legend(['IBM','Moving Avg.','Upper Bollinger Band','Lower Bollinger Band'], loc='lower right')


    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')

    longbuy = False
    shortbuy = False
    longbuySPY = False
    shortbuySPY = False
    isaggressive = False
    datelen = len(movavg);
    count = 0;
    orders = []
    #for i in range(19,datelen-1):
    #    date = adjclose.index[i]
        
    #    if(adjclose.ix[i,IBM] < lowerband.ix[i,IBM] and adjclose.ix[i+1,IBM] > lowerband.ix[i+1,IBM]):
    #        if(longbuy == False and shortbuy == False):
    #            count += 1
    #            plt.axvline(adjclose.index[i+1], color='g')
    #            orders.append([adjclose.index[i+1],stock,"BUY",100])
    #            longbuy = True
    #    if(adjclose.ix[i,IBM] < movavg.ix[i,IBM] and adjclose.ix[i+1,IBM] > movavg.ix[i+1,IBM]):
    #        if(longbuy == True):
    #            count += 1
    #            plt.axvline(adjclose.index[i+1], color='black')
    #            orders.append([adjclose.index[i+1],stock,"SELL",100])
    #            longbuy = False
           
    #    if(adjclose.ix[i,IBM] > upperband.ix[i,IBM] and adjclose.ix[i+1,IBM] < upperband.ix[i+1,IBM]):
    #        if(longbuy == False and shortbuy == False):
    #            count += 1
    #            plt.axvline(adjclose.index[i+1], color='r')
    #            orders.append([adjclose.index[i+1],stock,"SELL",100])
    #            shortbuy = True
    #    if(adjclose.ix[i,IBM] > movavg.ix[i,IBM] and adjclose.ix[i+1,IBM] < movavg.ix[i+1,IBM]):
    #        if(shortbuy == True):
    #            count += 1
    #            plt.axvline(adjclose.index[i+1], color='black')
    #            orders.append([adjclose.index[i+1],stock,"BUY",100])
    #            shortbuy = False
        
    ##now perform analysis on open/close based on date, etc..
    #ordersnp = np.array(orders)
    #ordersDataFrame = pd.DataFrame(ordersnp[0:,1:], index=ordersnp[0:,0])

    #ordersDataFrame.columns = ['Symbol','Order','Shares']
    #ordersDataFrame.index.name = 'Date'
    ##adjclose.index.name = "Date"
    #ordersDataFrame.to_csv("C:\Users\Nilav\Documents\orders_mc2_p2.csv")
    ##adjclose.plot();

    for i in range(19,datelen-1):
        date = adjclose.index[i]

        if(adjclose.ix[i,SPY] < lowerband.ix[i,SPY] and adjclose.ix[i+1,SPY] > lowerband.ix[i+1,SPY]):
            if(longbuySPY == False and shortbuySPY == False):
                #count += 1
                #plt.axvline(adjclose.index[i+1], color='g')
                #orders.append([adjclose.index[i+1],SPY,"BUY",100])
                longbuySPY = True
        if(adjclose.ix[i,SPY] < movavg.ix[i,SPY] and adjclose.ix[i+1,SPY] > movavg.ix[i+1,SPY]):
            if(longbuySPY == True):
                #count += 1
                #plt.axvline(adjclose.index[i+1], color='black')
                #orders.append([adjclose.index[i+1],SPY,"SELL",100])
                longbuySPY = False
           
        if(adjclose.ix[i,SPY] > upperband.ix[i,SPY] and adjclose.ix[i+1,SPY] < upperband.ix[i+1,SPY]):
            if(longbuySPY == False and shortbuySPY == False):
                #count += 1
                #plt.axvline(adjclose.index[i+1], color='r')
                #orders.append([adjclose.index[i+1],SPY,"SELL",100])
                shortbuySPY = True
        if(adjclose.ix[i,SPY] > movavg.ix[i,SPY] and adjclose.ix[i+1,SPY] < movavg.ix[i+1,SPY]):
            if(shortbuySPY == True):
                #count += 1
                #plt.axvline(adjclose.index[i+1], color='black')
                #orders.append([adjclose.index[i+1],SPY,"BUY",100])
                shortbuySPY = False


        if(adjclose.ix[i,IBM] < lowerband.ix[i,IBM] and adjclose.ix[i+1,IBM] > lowerband.ix[i+1,IBM]):
            if(longbuy == False and shortbuy == False):
                count += 1
                if(longbuySPY == True):
                    isaggressive = True
                    orders.append([adjclose.index[i+1],IBM,"BUY",150])
                    plt.axvline(adjclose.index[i+1], color='brown')
                else:
                    orders.append([adjclose.index[i+1],IBM,"BUY",100])
                    plt.axvline(adjclose.index[i+1], color='g')
                longbuy = True
        if(adjclose.ix[i,IBM] < movavg.ix[i,IBM] and adjclose.ix[i+1,IBM] > movavg.ix[i+1,IBM]):
            if(longbuy == True):
                count += 1
                plt.axvline(adjclose.index[i+1], color='black')
                if(isaggressive == True):
                    orders.append([adjclose.index[i+1],IBM,"SELL",150])
                    isaggressive = False
                else:
                    orders.append([adjclose.index[i+1],IBM,"SELL",100])
                longbuy = False
           
        if(adjclose.ix[i,IBM] > upperband.ix[i,IBM] and adjclose.ix[i+1,IBM] < upperband.ix[i+1,IBM]):
            if(longbuy == False and shortbuy == False):
                count += 1
                if(shortbuySPY == True):
                    isaggressive = True
                    orders.append([adjclose.index[i+1],IBM,"SELL",150])
                    plt.axvline(adjclose.index[i+1], color='orange')
                else:
                    orders.append([adjclose.index[i+1],IBM,"SELL",100])
                    plt.axvline(adjclose.index[i+1], color='r')
                shortbuy = True
        if(adjclose.ix[i,IBM] > movavg.ix[i,IBM] and adjclose.ix[i+1,IBM] < movavg.ix[i+1,IBM]):
            if(shortbuy == True):
                count += 1
                plt.axvline(adjclose.index[i+1], color='black')
                if(isaggressive == True):
                    isaggressive = False
                    orders.append([adjclose.index[i+1],IBM,"BUY",150])
                else:
                    orders.append([adjclose.index[i+1],IBM,"BUY",100])
                shortbuy = False


    #now perform analysis on open/close based on date, etc..
    ordersnp = np.array(orders)
    ordersDataFrame = pd.DataFrame(ordersnp[0:,1:], index=ordersnp[0:,0])

    ordersDataFrame.columns = ['Symbol','Order','Shares']
    ordersDataFrame.index.name = 'Date'
    #adjclose.index.name = "Date"
    ordersDataFrame.to_csv("C:\Users\Nilav\Documents\orders_mc2_p2_newstrategy_10_11.csv")
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
        #df= df.dropna(subset=[IBM])
        #df= df.fillna()
        #df= df.fillna(method='backfill')
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
    return df


if __name__ == "__main__":
    show_bollinger()