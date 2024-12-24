
def MaxScore(lst):
    index = 0
    for i in range(1, len(lst)):
        if sum(lst[i][1]) > sum(lst[index][1]):
            index = i
    return (lst[index][0], sum(lst[index][1]))

def SortScore(lst):
    lst.sort(key = lambda x: sum(x[1]), reverse = True)
    print(f'按总分降序排序结果：{lst}')
    


def demo():
    lst = []
    for i in range(4):
        name = input(f'请输入第{i}个学生姓名：')
        score1, score2 = map(int, input(f'请输入第{i}个学生两门课成绩：').split(','))
        lst.append([name, (score1, score2)])
    print(f'总分最高的学生姓名和成绩是：{MaxScore(lst)}')
    SortScore(lst)

demo()
