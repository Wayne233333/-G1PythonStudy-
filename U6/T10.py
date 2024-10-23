
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)
        
num = int(input())
ans = f(num)
print(ans)
