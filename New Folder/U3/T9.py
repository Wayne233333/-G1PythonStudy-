
from math import sin
from math import exp
from math import log
from math import pi

x = float(input())

if x < 0:
    y = x**2 + 5
elif x < 10:
    y = (sin(x / 180 * pi)**2)
else:
    y = exp(x) - log(x)

print(round(y, 4))