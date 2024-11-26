def demo():
    ans = 0
    for i in range(1, 1001):
        if not i % 10:
            continue
        ans += i
    print(ans)

demo()
