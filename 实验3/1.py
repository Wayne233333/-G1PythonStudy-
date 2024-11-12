from math import e
from math import cos
from math import pi
from math import log

def demo():
    x = float(input())

    if x < 0:
        y = -x
    elif x < 5:
        y = e**x * cos(x/180*pi)
    elif x < 10:
        y = x**3
    else:
        y = (7 + 8*x) * log(x)
    if y == int(y):
        print(int(y))
    else:
        print(round(y, 2))

demo()
