
a = list(map(int,input().split()))
e = sum(a)/len(a)
for i in a:
    if i > e:   print(i,end = ' ')