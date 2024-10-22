
lst = map(str, input().split())
d = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for i in lst:
    if i[0] in d:
        d[i[0]] += 1
    elif i[0].lower() in d:
        d[i[0].lower()] += 1
    
for i in d.keys():
    print(f'首字母{i}出现{d[i]}次')
        