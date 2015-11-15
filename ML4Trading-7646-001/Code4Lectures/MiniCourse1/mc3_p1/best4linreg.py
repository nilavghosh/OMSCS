# function z = x+2y
import numpy as np


x = np.array([np.random.uniform(-5.0,5.0) for i in range(1000)]).reshape(1000,1)
y = np.array([np.random.uniform(-5.0,5.0) for i in range(1000)]).reshape(1000,1)
z = x + 2*y

dataset = x
dataset=np.append(dataset,y,axis = 1)
dataset=np.append(dataset,z,axis = 1)
dataset = dataset[dataset[:,2].argsort()]
np.savetxt("best4linreg.csv", dataset, delimiter=",")


