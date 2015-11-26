import Tkinter
import turtle
from Tkinter import *
import os
from matrix import *

ix = matrix([[0.],[0.],[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.,0,0], [0., 1000.,0,0],[0, 0,1000,0],[0., 0.,0,1000]]) # initial uncertainty
u = matrix([[0.], [0.], [0], [0]]) # external motion
F = matrix([[1., 1, 0, 0], [0,1.,0,0], [0,0,1,1], [0,0,0,1]]) # next state function
B = matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
H = matrix([[1., 0,0,0],[0,0,1,0]]) #measurement function
R = matrix([[0.001,0],[0.0,0.001]]) # measurement uncertainty
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

def show_movement():
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
    #print 'x= '
    #ix.show()

    #print 'P= '
    #P.show()

    count = count + 1
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

turtle1 = turtle.RawTurtle(canvas)
turtle1.color('blue')
turtle2 = turtle.RawTurtle(canvas)
turtle2.color('red')

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