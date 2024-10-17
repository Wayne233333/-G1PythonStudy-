
from math import sin
from math import pi

a, b, c = map(float, input().split())
print(round(a*b*sin(c/180*pi)/2,3))