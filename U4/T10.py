
n = int(input())
x = list(map(float,input().split(',')))

xn = sum(x)/n
s = 0
for i in x:
    s += (xn - i)**2

s = (s/(n-1))**0.5
print(f'xn={xn}, s={s}')