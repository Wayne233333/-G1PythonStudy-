
from random import randint
a = []

while len(a) != 5:
    n = randint(5, 49)*2 + 1
    if not n in a:  a.append(n)

while len(a) != 10:
    n = randint(5, 49)*2
    if not n in a: a.append(n)

print(a)