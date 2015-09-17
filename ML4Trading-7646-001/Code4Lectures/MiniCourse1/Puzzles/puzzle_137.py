import numpy as np

def f1(x):
    y = x
    print(id(x))
    print(id(y))
    y[0] = 2
    y[1] = 2
    return 0

def f2(x):
    y = x + 0 
    print(id(x))
    print(id(y))
    y[0] = 4
    y[1] = 4
    return 0

print("f1")
x = np.array([0, 0])
print(x)
y = f1(x)
print(x)

print("f2")
x = np.array([0, 0])
print(x)
y = f2(x)
print(x)