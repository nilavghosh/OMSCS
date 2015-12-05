import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import Tkinter
import turtle
from Tkinter import *
import os
from matrix import *
import tkMessageBox

def contains_point(xpred,ypred):
    global x1,x2,y1,y2
    poly = [x1, y1, x2, y2]
    bbPath = mplPath.Path(np.array([[poly[0], poly[1]],
                         [poly[1], poly[2]],
                         [poly[2], poly[3]],
                         [poly[3], poly[0]],
                         [poly[0], poly[1]]]))
    #x, y = zip(*bbPath.vertices)
    #line, = plt.plot(x, y, 'go-')
    #plt.grid()
    #plt.title('spline paths')
    #plt.show()
    return bbPath.contains_point((xpred, ypred))




    
ix = matrix([[0.],[0.],[0.], [0.]]) # initial state (location and velocity)
orinP = matrix([[1000., 0.,0,0], [0., 1000.,0,0],[0, 0,1000,0],[0., 0.,0,1000]]) # initial uncertainty
P = matrix([[1000., 0.,0,0], [0., 1000.,0,0],[0, 0,1000,0],[0., 0.,0,1000]]) # initial uncertainty
u = matrix([[0.], [0.], [0], [0]]) # external motion
F = matrix([[1., 1, 0, 0], [0,1.,0,0], [0,0,1,1], [0,0,0,1]]) # next state function
B = matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
H = matrix([[1., 0,0,0],[0,0,1,0]]) #measurement function
R = matrix([[0.00001,0],[0.0,0.00001]]) # measurement uncertainty
I = matrix([[1., 0.,0,0], [0., 1,0,0],[0., 0,1,0],[0, 0,0,1]]) # identity matrix



def run_turtles(*args):
    for t, d in args:
        t.circle(250, d)
    root.after_idle(run_turtles, *args)

def run_robot(bot):   
    bot.goto(10,20)
    


filename = os.getcwd() + "\\" + "Final Project\\test01.txt"
lines = open(filename, 'r').readlines()
count=1
scale = 3
stopb = False

root = Tkinter.Tk()
root.withdraw()

def locAfter10Moves(ixa,P):
    ix = ixa # initial state (location and velocity)
    u = matrix([[0.], [0.], [0], [0]]) # external motion
    F = matrix([[1., 1, 0, 0], [0,1.,0,0], [0,0,1,1], [0,0,0,1]]) # next state function
    B = matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    H = matrix([[1., 0,0,0],[0,0,1,0]]) #measurement function
    R = matrix([[0.00001,0],[0.0,0.00001]]) # measurement uncertainty
    I = matrix([[1., 0.,0,0], [0., 1,0,0],[0., 0,1,0],[0, 0,0,1]]) # identity matrix
    x = ix.value[0][0]
    y = ix.value[2][0]
    for i in range(10):
        Z = matrix([[x],[y]])
        y = Z - (H * ix)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        ix = ix + (K * y)
        P = (I - (K * H)) * P 
        
        # prediction
        ix = (F * ix) + (B * u)
        P = F * P * F.transpose()
        x = ix.value[0][0]
        y = ix.value[2][0]
        #if(contains_point(x,y) == 0):
        #    tkMessageBox.showinfo("Outside Grid")
    return x,y

def show_movement():
    
    turtle3.ht(); turtle3.pu()
    global count,scale, ix,P, u, F, B, H, R, I
    x, y = lines[count].split(',')
    x = int(x)/scale-400
    y = int(y)/scale-400
    turtle1.goto(x,y)

    #measurement update
    Z = matrix([[x],[y]])
    y = Z - (H * ix)
    S = H * P * H.transpose() + R
    K = P * H.transpose() * S.inverse()
    ix = ix + (K * y)
    P = (I - (K * H)) * P 
    
    # prediction
    ix = (F * ix) + (B * u)
    P = F * P * F.transpose()
    turtle2.goto(ix.value[0][0],ix.value[2][0])
    turtle3.setx(ix.value[0][0])
    turtle3.sety(ix.value[2][0])
    posX,posY = locAfter10Moves(ix,P)
    
    turtle3.st(); turtle3.pd()
    turtle3.clear()
    turtle3.goto(posX,posY)
    
    #print 'x= '
    #ix.show()

    #print 'P= '
    #P.show()

    count = count + 1
    if(count%10 ==0):
        P = orinP
    if(count < len(lines) and stopb == False):
        root.after_idle(show_movement)


def callback():
    global stopb
    stopb= False
    show_movement()
    print "click!"

def stopbot():
    global stopb
    stopb = True

b = Button(root, text="OK", command=callback)
c = Button(root, text="Stop", command=stopbot)

b.pack()
c.pack()

frame = Tkinter.Frame(bg='black')
Tkinter.Label(frame, text=u'Hello', bg='grey', fg='white').pack(fill='x')
canvas = Tkinter.Canvas(frame, width=1200, height=1200)
canvas.pack()
frame.pack(fill='both', expand=True)

box_A = turtle.RawTurtle(canvas)
translate = 400
x1, y1 = 1688/scale-translate, 121/scale-translate
x2, y2 = 244/scale-translate, 979/scale-translate

box_A.setposition(x1,y1)
box_A.setposition(x1,y2)
box_A.setposition(x2,y2)
box_A.setposition(x2,y1)
box_A.setposition(x1,y1)

turtle1 = turtle.RawTurtle(canvas)
turtle1.color('blue')
turtle2 = turtle.RawTurtle(canvas)
turtle2.color('red')
turtle3 = turtle.RawTurtle(canvas)
turtle3.color('black')
turtle3.ht(); turtle3.pu()

turtle1.ht(); turtle1.pu()
x, y = lines[0].split(',')
x = int(x)/scale-400
y = int(y)/scale-400
turtle1.setx(x)
turtle1.sety(y)
turtle1.st(); turtle1.pd()

turtle2.ht(); turtle2.pu()
turtle2.setx(0-400)
turtle2.sety(0-400)
turtle2.st(); turtle2.pd()



root.deiconify()

#run_turtles((turtle1, 3), (turtle2, 4))
#run_robot(turtle1)

root.mainloop()