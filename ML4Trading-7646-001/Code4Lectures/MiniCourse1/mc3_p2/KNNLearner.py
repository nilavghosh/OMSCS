"""
A simple wrapper for KNN Learner.  (c) 2015 Tucker Balch
"""

import numpy as np

class KNNLearner(object):

    def __init__(self):
        pass # move along, these aren't the drones you're looking for

    def __init__(self, k):
        self.k = k
        
    def addEvidence(self,Xtrain,Ytrain):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        self.Xtrain = Xtrain
       
        self.Ytrain = Ytrain
        
    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        YPredict = []
        arindex = np.arange(len(points)).reshape(len(points),1)
        for obs in points:
            pointsModel = np.array([obs]*len(self.Xtrain))
            YPredict.append(np.mean(self.Ytrain[np.argsort((((self.Xtrain - pointsModel)**2).sum(axis=1))**.5)[0:self.k]]))
        return YPredict      

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
