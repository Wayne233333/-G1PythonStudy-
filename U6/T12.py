
a = input()
stu = []

while a:
    stu.append(list(map(str, a.split(','))))
    a = input()

print(stu)

for i in range(len(stu)):   stu[i][1] = int(stu[i][1])
stu.sort(key = lambda x : x[1], reverse=True)

print(stu)
