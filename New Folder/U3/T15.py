
n = int(input())
tot = 0
f = []

for i in range(2, n+1):
    for j in f:
        if i%j==0:  break
    else:
        tot+=1
        f.append(i)

print(f'{f} {tot}')