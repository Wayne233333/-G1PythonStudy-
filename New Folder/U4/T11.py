
def Sort(f1, f2):   #二分，查找olog2n，排序on2
    for i in range(len(f1)):
        t1 = f1[i]
        t2 = f2[i]
        l = 0
        r = i - 1
        while l <= r:
            m = (l + r) // 2
            if t1 < f1[m]:
                r = m - 1
            else:
                l = m + 1
        for j in range(i-1, l-1, -1):
            f1[j + 1] = f1[j]
            f2[j + 1] = f2[j]
        if l != i:
            f1[l] = t1
            f2[l] = t2
    return f1, f2

num = []
sco = []

a = input()

while a != 'OVER':

    b,c = map(int, a.split(' '))
    num.append(b)
    sco.append(c)
    a = input()

num, sco = Sort(num, sco)

for i in range(len(num)):
    if sco[i] >= 60:
        print(num[i], sco[i])
