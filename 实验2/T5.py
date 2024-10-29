
def demo():
    a, b = map(str, input().split())
    la = len(a)
    lb = len(b)
    if la == 1 or lb == 1:
        print('error!')
        return
    la //= 2
    lb //= 2
    print(str(int(a[:la])%int(a[-la:])) + str(int(b[:lb])//int(b[-lb:])))
        

demo()
