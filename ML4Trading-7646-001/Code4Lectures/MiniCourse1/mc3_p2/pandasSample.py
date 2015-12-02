import pandas as pd
import numpy as np
import pandas.io.data as web
import datetime

msft = web.DataReader('^GSPC', 'yahoo', start='1/1/2000', end='4/14/2014')
i =1