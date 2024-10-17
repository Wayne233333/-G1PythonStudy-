
x = float(input())
op = -1
s = x
i = 1
xn = x

while abs(xn) >= 1e-5:   #题目题意不清

    xn = xn * x**2 / (i+1)/(i+2) * op
    s += xn
    op *= -1
    i += 2

print(round(s, 6))