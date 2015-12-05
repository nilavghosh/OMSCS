from matrix import *

measurements = [[1],[2],[3],[4],[5],[6]]
x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1], [0,1.]]) # next state function
B = matrix([[0,0],[0,0]])
H = matrix([[1., 0]]) #measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix
def filter(x, P):
    for n in range(len(measurements)):
        #measurement update
        Z = matrix([measurements[n]])
        y = Z-(H * x)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        x = x + (K * y)
        P = (I-(K * H)) * P
        
        # prediction
        x = (F * x) + (B * u)
        P = F * P * F.transpose()        print 'x= '
        x.show()
        print 'P= '
        P.show()   filter(x, P)