
stu = []

a = input()

while a:
    try:
        _id, name = a.split()
        stu.append((int(_id), name))
    except ValueError:
        print("Value error!")
    
    a = input()

stu.sort(key = lambda x : x[0], reverse = True)

top_stu = stu[:3]

with open('result.txt', 'w') as file:
    for _, name in top_stu:
        file.write(f'{name}\n')

print("处理完毕，前 3 个学生的姓名已写入 result.txt。")
