def demo():
    a, b, c = map(str, input("请输入三个字符用逗号分隔:").split(','))
    print(f'{a},{b},{c}中最大的字符是{max(a, max(b, c))}')

demo()

