
f = []
a = input()

while a != 'OVER':
    f.append(list(map(int, a.split(' '))))
    a = input()

f.sort(key = lambda x: x[0])

for i in range(len(f)):
    if f[i][1] >=60:
        print(f[i][0], f[i][1])