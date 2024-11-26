def demo():
    a = input('输入一个数字字符a：')
    ans1 = eval('+'.join([a*i for i in range(1, int(a)+1)]))
    a2 = int(a)
    a2_ = a2
    l2 = []
    for i in range(1, a2+1):
        l2.append(a2_)
        a2_ = a2_*10 + a2
    ans2 = sum(l2)
    ans3 = sum([int(a*i) for i in range(1, int(a)+1)])
    print(f'方法一，用eval直接计算字符串表达式：{ans1}')
    print(f'方法二，先把数值添加到列表后再求和：{ans2}')
    print(f'方法三，采用列表推导式一句话求和：{ans3}')
demo()
