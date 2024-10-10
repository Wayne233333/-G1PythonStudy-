
from random import randint
a = [randint(10,99) for i in range(10)]
print(a)

n = int(input())%10
print(a[-n:]+a[:-n])