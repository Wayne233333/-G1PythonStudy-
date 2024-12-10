from random import randint

def demo():
    lst = [randint(10,99) for i in range(10)]
    print(f'十个随机数：{lst}')
    lst.sort(reverse = True)
    print(f'排序后数据：{lst}')
    a = int(input('please input a number:'))
    for i in range(10):
        if a > lst[i]:
            lst = lst[:i] + [a] + lst[i:]
            break
    else:
        lst = lst + [a]
    print(f'插入新的数据后：{lst}')
demo()
