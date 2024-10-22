
lst = map(str, input().split())
d = {}
for i in lst:
    if not i in d:
        d[i] = 1
    else:
        d[i] += 1

d = sorted(d.items(), key = lambda d:d[1], reverse = True)

for i in range(10)
    print(f'单词{d[i][0]}出现{d[i][1]}次')
