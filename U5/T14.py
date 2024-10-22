
def f(a, s):
    if len(a) == len(s):
        print(s, end = ' ')
        return
    
    for i in a:
        if not i in s:
            f(a, s+i)

n = int(input())

a = [str(i+1) for i in range(n)]
s = ''

f(a, s)
