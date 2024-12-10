from random import randint

def demo():
    lst = [randint(10,99) for i in range(10)]
    lst1 = sorted(lst[:5], reverse = True)
    lst2 = sorted(lst[5:])
    print(f'{lst}\n{lst[:5]} 中最大的数是：{lst1[0]}\n{lst[5:]} 中最小的数是{lst2[0]}')
demo()
