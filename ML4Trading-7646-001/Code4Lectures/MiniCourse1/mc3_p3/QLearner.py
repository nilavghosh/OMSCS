"""
Template for implementing QLearner  (c) 2015 Tucker Balch
"""

import numpy as np
import random as rand

class QLearner(object):

    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):

        self.num_states=100
        self.alpha = 0.2 
        self.gamma = 0.9
        self.rar = 0.5
        self.radr = 0.99
        self.dyna = dyna
        self.satuples = {}
        self.verbose = verbose
        self.num_actions = num_actions
        self.s = 0
        self.a = 0
        self.Q = np.array([[0.0 for k in range(num_actions)] for i in range(num_states)])

    def querysetstate(self, s):
        """
        @summary: Update the state without updating the Q-table
        @param s: The new state
        @returns: The selected action
        """
        self.s = s
        action = rand.randint(0, self.num_actions-1)
        if self.verbose: print "s =", s,"a =",action
        self.a = action
        return action

    def query(self,s_prime,r):
        """
        @summary: Update the Q table and return an action
        @param s_prime: The new state
        @param r: The next state
        @returns: The selected action
        """
        self.satuples[(self.s,self.a)] = (s_prime,r)
        self.Q[self.s,self.a] = self.alpha*self.Q[self.s,self.a] + (1-self.alpha)*(r + self.gamma*self.Q[s_prime].max())
        if(self.dyna > 0):
            for i in range(self.dyna):
                upd_sa_ind = rand.randint(0,len(self.satuples)-1)
                temp_s = self.satuples.keys()[upd_sa_ind][0]
                temp_a = self.satuples.keys()[upd_sa_ind][1]
                temp_s_prime = self.satuples.values()[upd_sa_ind][0]
                temp_r = self.satuples.values()[upd_sa_ind][1]
                self.Q[temp_s,temp_a] = self.alpha*self.Q[temp_s,temp_a] + (1-self.alpha)*(temp_r + self.gamma*self.Q[temp_s_prime].max())
        self.alpha = self.alpha * self.radr #decaying alpha over time
        self.s = s_prime
        rnd_num = rand.random()
        p = 1. - self.rar
        if rnd_num < p:
            action = self.Q[s_prime].argmax()
            self.a = action
            if self.verbose: print "s =", s_prime,"a =",action,"r =",r
            self.rar = self.rar * self.radr
            return action      
        action = rand.randint(0, self.num_actions-1)
        self.a = action
        if self.verbose: print "s =", s_prime,"a =",action,"r =",r
        self.rar = self.rar * self.radr
        return action

if __name__=="__main__":
    print "Remember Q from Star Trek? Well, this isn't him"
