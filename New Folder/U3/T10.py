
a, b, c = map(float, input().split())
Max = max(max(a, b), c)

while Max >= a + b + c - Max:
    a, b, c = map(float, input("non-existent triangle,pls type in again!\n").split())

s = a + b + c
s /= 2
S = (s * (s-a) * (s-b) * (s-c))**0.5

print(round(S, 4))