def demo():
    a = input("请输入一个三位整数:")
    if not len(a) == 3:
        print('警告！不是三位数')
        return
    print(f'方法一:{a[::-1]}')
    b = int(a)
    print(f'方法二:{b%10*100 + b//10%10*10 + b//100}')
    print('方法三:'+''.join(reversed(a)))

demo()
    
