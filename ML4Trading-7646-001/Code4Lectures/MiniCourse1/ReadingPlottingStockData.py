import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    dataframe = pd.read_csv("data/AAPL.csv")
    print (dataframe['Adj Close'])
    dataframe['Adj Close'].plot()
    plt.show()
    
if __name__ == "__main__":
    test_run()
