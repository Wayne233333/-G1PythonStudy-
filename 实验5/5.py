def demo():
    lst = eval(input())
    op = input('还需要输入新的学生成绩吗：是请输入“1”，否请输入“0”：')
    while op == '1':
        name = input('请输入学生姓名：')
        a, b = map(int, input('请输入学生两门课成绩，用逗号分隔：').split(','))
        for i in range(len(lst)):
            if lst[i][0] == name:
                lst[i] = (name, [a, b]) #无反馈需求，则直接覆盖
                break
        else:
            lst.append((name,[a, b]))
        op = input('还需要输入新的学生成绩吗：是请输入“1”，否请输入“0”：')
    print(lst)
demo()
