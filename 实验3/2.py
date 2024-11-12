def demo():
    x1, x2, x3 = map(float, input('输入三个数x1,x2,x3').split(','))
    print(f'方法一:{max(x1, x2, x3)}')
    if x1 > x2:
        a = x1
    else:
        a = x2
    if a < x3:
        a = x3
    print(f'方法二:{a}')
    if x1 > x2:
        if x1 > x3:
            b = x1
        else:
            b = x3
    else:
        if x2 > x3:
            b = x2
        else:
            b = x3
    print(f'方法三:{b}')

demo()
