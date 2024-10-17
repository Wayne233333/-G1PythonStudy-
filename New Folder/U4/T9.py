
print('输入坐标，完成请输入done')
s = 0
xpre = ypre = x = y = 0
a = input()
while a != 'done':
    x, y = map(str, a.split(','))
    x = int(x[1:])
    y = int(y[:-1])
    s += ((x-xpre)**2 + (y-ypre)**2)**0.5
    xpre = x
    ypre = y
    a = input()

print(s)