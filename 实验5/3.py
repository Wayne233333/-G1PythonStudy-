from random import randint

def demo():
    #part 1
    lst = list(map(str,input('please input a string list:').split(',')))
    a = input('please input a repeated letter:')
    for i in range(len(lst)-1,-1,-1):
        if lst[i].count(a) >= 3:
            lst.remove(lst[i])
    print(f'new list: {lst}')
    #part 2
    lst = eval(input('please input a string list:'))
    a = input('please input a repeated letter:')
    for i in range(len(lst)-1,-1,-1):
        if lst[i].count(a) >= 3:
            lst.remove(lst[i])
    print(f'changed list: {lst}')
demo()
