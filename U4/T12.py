
f = []
a = input()

while a != 'OVER':
    f.append(list(map(int, a.split(' '))))
    a = input()

f.sort(key = lambda x: x[1], reverse = True)

for i in range(len(f)):
    print(f[i][0], f[i][1])