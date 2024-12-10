
def demo():
    #part 1
    a = input('请输入第一串字符内容：')
    b = input('请输入第二串字符内容：')
    a1 = list(a)
    b1 = list(b)
    ans1 = []
    for i in b1:
        if i in a1 and not i in ans1:
            ans1.append(i)
    ans1.sort()
    print(ans1)
    #part 2
    a2 = list(a)
    b2 = list(b)
    ans2 = []
    for i in b2:
        if i in a2:
            ans2.append(i)
    ans2 = list(set(ans2))
    ans2.sort()
    print(ans2)
    #part 3
    a3 = set(a)
    b3 = set(b)
    ans3 = []
    for i in b3:
        if i in a3:
            ans3.append(i)
    ans3.sort()
    print(ans3)
demo()
