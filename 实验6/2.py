
from random import randint

def jdg(lst):
    lst1 = []
    lst2 = []
    lst3 = []
    for i in lst:
        if not i%2:
            lst1.append(i)
        if not i%3:
            lst2.append(i)
        if i not in lst1 and i not in lst2:
            lst3.append(i)
    return (lst1,lst2,lst3)

def demo():
    n = int(input("请输入随机整数数量："))
    lst = [randint(10,99) for i in range(n)]
    print(f'原始数据：{lst}\n{jdg(lst)}')



demo()
