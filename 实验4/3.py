def demo():
    x = float(input())
    s = 1
    fenmu = 1
    fenzi = 1
    i = 1
    while fenzi / fenmu >= 1e-5:
        fenmu *= i
        fenzi *= x
        i += 1
        s += fenzi / fenmu
    print(s)
demo()
