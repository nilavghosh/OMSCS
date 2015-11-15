import sympy as spy
from sympy import symbols
from sympy.mpmath import *
from sympy.plotting import plot3d
from sympy.utilities.lambdify import lambdify
from sympy import sin,cos
r, R = 1, 2.5
f = lambda u, v: [r*spy.cos(u), (R+r*spy.sin(u))*spy.cos(v), (R+r*spy.sin(u))*spy.sin(v)]
splot(f, [0, 2*pi], [0, 2*pi]) 