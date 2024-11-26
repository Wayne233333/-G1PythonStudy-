def demo():
    a, b = map(int, input('请输入两个数:').split(','))
    if a < b:
        a, b = b, a
    m, n = a, b
    while m % n:
        m, n = n, m%n
    print(f'{a}和{b}的最小公倍数是{int(a*b/n)}\n{a}和{b}的最大公约数是{n}')
demo()
