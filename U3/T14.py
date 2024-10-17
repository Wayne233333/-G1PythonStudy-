
n = int(input())
f = input().split()
f = [float(x) for x in f]

print(round(sum(f)/n, 4), end = " ")
print(round(((sum([x**2 for x in f]) - sum(f)**2/n)/(n-1))**0.5, 4))