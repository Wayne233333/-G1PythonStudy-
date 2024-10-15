def demo():

    x1, x2, y1, y2 = map(float, input().split())

    print(round(((x1-x2)**2+(y1-y2)**2)**0.5,2))

demo()