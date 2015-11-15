"""
Test a learner.  (c) 2015 Tucker Balch
"""

import numpy as np
import math
import LinRegLearner as lrl
import KNNLearner as knn
import BagLearner as bgl

if __name__=="__main__":
    inf = open('C:/Learning/OMSCS/OMSCS-Code/ML4Trading-7646-001/Code4Lectures/MiniCourse1/mc3_p1/Data/ripple.csv')
    data = np.array([map(float,s.strip().split(',')) for s in inf.readlines()])

    # compute how much of the data is training and testing
    train_rows = math.floor(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data[:train_rows,0:-1]
    trainY = data[:train_rows,-1]
    testX = data[train_rows:,0:-1]
    testY = data[train_rows:,-1]

    for b in range(1,21):
        # create a learner and train it
        #learner = knn.KNNLearner(1) # create a LinRegLearner
        #learner = lrl.LinRegLearner() # create a LinRegLearner
        learner = bgl.BagLearner(learner = knn.KNNLearner, kwargs = {"k":1}, bags = b, boost = False)
        learner.addEvidence(trainX, trainY) # train it

        # evaluate in sample
        predY = learner.query(trainX) # get the predictions
        #np.savetxt("knnlearner.txt")
        print "No of bags: ", b
        rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
        print "In sample results"
        print "RMSE: ", rmse
        c = np.corrcoef(predY, y=trainY)
        print "corr: ", c[0,1]

        # evaluate out of sample
        predY = learner.query(testX) # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
        #np.savetxt("linreglearner_test.csv",np.append(testX,np.array(predY).reshape(400,1),axis=1),delimiter=",")
        print
        print "Out of sample results"
        print "RMSE: ", rmse
        c = np.corrcoef(predY, y=testY)
        print "corr: ", c[0,1]
