
from math import sin
from math import cos
from math import pi

deg = [0,30,60,90,120,150,180]
sp1 = [2,1,1,1,0,0,0]
sp2 = [5,5,0,5,0,5,5]
sp3 = [5,0,5,5,5,0,5]

print('deg|sin(deg)|cos(deg)\n'+'-'*18)
for i in range(len(deg)):
    a = sin(deg[i]*pi/180)
    b = cos(deg[i]*pi/180)
    c = ''
    if b >= 0:  c = ' '
    print(f'{" "*sp1[i]}{deg[i]}|{round(a,6)}{"0"*sp2[i]}|{c}{round(b,6)}{"0"*sp3[i]}')