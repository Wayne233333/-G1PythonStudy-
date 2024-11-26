def demo():
    a = int(input())
    if a == 1:
        print('1没有质因子')
        return
    a_ = a
    op = True
    lst = []
    ans = []
    for i in range(2, int(a**0.5)+1):
        for j in lst:
            if not i%j:
                break
        else:
            lst.append(i)
            while not a_%i:
                ans.append(str(i))
                a_ /= i
            if a_ == 1:
                break
    if a == a_:
        print(f'{a} = 1*{a}')
    else:
        print(f'{a} = {"*".join(ans)}')
demo()
        
    
