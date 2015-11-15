"""
A simple wrapper for KNN Learner.  (c) 2015 Tucker Balch
"""

import numpy as np

class BagLearner(object):

    def __init__(self):
        pass # move along, these aren't the drones you're looking for

    def __init__(self,learner, kwargs, bags, boost):
        self.bags = []
        self.nbags = bags
        self.learners = []
        for i in range(0,bags):
            self.learners.append(learner(**kwargs))
        self.boost = boost
        
    def addEvidence(self,Xtrain,Ytrain):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        self.Xtrain = Xtrain
        self.Ytrain = Ytrain
        self.XBags = []
        self.YBags = []

        for i in range(0,self.nbags):
            randomIndices = np.random.randint(0,len(self.Xtrain),int(.6*len(self.Xtrain)))
            self.XBags.append(self.Xtrain[randomIndices])
            self.YBags.append(self.Ytrain[randomIndices])
            self.learners[i].addEvidence(self.XBags[i], self.YBags[i])
        
        
    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        YPredict = []
        for i in range(0,self.nbags):
            YPredict.append(self.learners[i].query(points))
        return np.mean(YPredict,axis=0)      

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
