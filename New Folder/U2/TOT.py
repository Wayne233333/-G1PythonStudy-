
from math import pi

r = float(input())
print(round(4*pi*r**3/3,4))



from math import sin
from math import pi

a, b, c = map(float, input().split())
print(round(a*b*sin(c/180*pi)/2,3))



from calendar import month

a, b = map(int, input().split())
print(month(a, b))