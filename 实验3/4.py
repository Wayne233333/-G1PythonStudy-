def demo():
    a = input('请输入一个字符串:')
    if a == a[::-1]:
        print(f'{a}是一个回文字符串')
    else:
        print(f'{a}不是一个回文字符串')
    b = input('请输入一个整数:')
    ans = 0
    for i in b:
        ans += int(i)**len(b)
    if int(b) == ans:
        print(f'{b}是水仙花数')
    else:
        print(f'{b}不是水仙花数')

demo()
