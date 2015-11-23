import Tkinter
import turtle
from Tkinter import *

def run_turtles(*args):
    for t, d in args:
        t.circle(250, d)
    root.after_idle(run_turtles, *args)

def run_robot(bot):   
    bot.goto(10,20)
    


filename = "C:\\test01.txt"
lines = open(filename, 'r').readlines()
count=1
scale = 3

root = Tkinter.Tk()
root.withdraw()

def show_movement():
    global count,scale
    x, y = lines[count].split(',')
    x = int(x)
    y = int(y)
    turtle1.goto(x/scale,y/scale)
    count = count + 1
    if(count < len(lines)):
        root.after_idle(show_movement)


def callback():
    show_movement()
    print "click!"

b = Button(root, text="OK", command=callback)
b.pack()


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
x = int(x)
y = int(y)
turtle1.setx(x/scale)
turtle1.sety(y/scale)
#Kturtle1.left(90); turtle1.fd(250); turtle1.lt(90)
turtle1.st(); turtle1.pd()

turtle2.ht(); turtle2.pu()
turtle2.fd(250); turtle2.lt(90)
turtle2.st(); turtle2.pd()



root.deiconify()

#run_turtles((turtle1, 3), (turtle2, 4))
#run_robot(turtle1)

root.mainloop()