import pandas as pd
import numpy as np
from pandas.io.data import DataReader
import matplotlib



def test():
    #matplotlib.use('Qt4Agg')
    sp500 = DataReader('^GSPC', 'yahoo', start='1/1/2000', end='4/14/2014')
    import matplotlib.pyplot as plt
    plt.plot(sp500['Close'])
    plt.show()
    
if __name__ == "__main__":
    print (test())
