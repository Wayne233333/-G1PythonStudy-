import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font",family='FangSong')

# 输入两组相同长度的数组
x = list(map(float, input("请输入第一组数据（以空格分隔）: ").split()))
y = list(map(float, input("请输入第二组数据（以空格分隔）: ").split()))

# 检查数组长度是否相同
if len(x) != len(y):
    print("数组长度不相同，请重新输入。")
else:
    # 绘制折线图
    plt.plot(x, y, marker='o')
    plt.title('折线统计图')
    plt.xlabel('第一组数据')
    plt.ylabel('第二组数据')
    plt.grid()
    plt.show()
