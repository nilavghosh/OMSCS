import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
matplotlib.style.use('ggplot')
#http://stackoverflow.com/questions/16522380/python-pandas-plot-is-a-no-show/16522626#16522626


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()

plt.show()