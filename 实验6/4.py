
def demo():
    n = int(input("请输入一半菱形的行数："))

    for i in range(1,n*2):
        num = (n-abs(n-i))*2-1
        print(' '*abs(n-i), end = '')
        if i%2:
            a = 'A'*int(num/2+1)
            print('B'.join(a))
        else:
            b = 'B'*int(num/2+1)
            print('A'.join(b))


demo()
