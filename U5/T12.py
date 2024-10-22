
lst = map(int, input().split(' '))
d = {}

for i in lst:
    if not i in d:
        d[i] = 1
    else:
        d[i] += 1

a = sorted(d.keys(), reverse = True)
print(a)