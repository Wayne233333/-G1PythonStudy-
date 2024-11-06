import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rc("font",family='SimHei')

# 输入两组相同长度的数组
x = list(map(float, input("请输入第一组数据T（以空格分隔）: ").split()))
y = list(map(float, input("请输入第二组数据lgk（以空格分隔）: ").split()))
for i in range(len(x)):
    x[i] = 1/x[i]

# 检查数组长度是否相同
if len(x) != len(y):
    print("数组长度不相同，请重新输入。")
else:
    # 绘制折线图
    plt.scatter(x, y, marker='o')
    para = np.polyfit(x, y, 1)
    y_fit = np.polyval(para, x)
    plt.plot(x, y_fit, 'g')
    correlation = np.corrcoef(x, y)[0][1]
    plt.text(0.8, 0.9, '拟合函数：'+str(round(para[0], 3))+'x+'+str(round(para[1], 3)), ha='center', va='center', transform=plt.gca().transAxes)
    plt.text(0.88, 0.8, '斜率：'+str(round(float(para[0]), 3)), ha='center', va='center', transform=plt.gca().transAxes)
    plt.text(0.9, 0.7, 'R^2：'+str(round(correlation**2, 3)), ha='center', va='center', transform=plt.gca().transAxes)


    plt.title('拟合函数_Create by 吴浩铭302024569154')
    plt.xlabel('1/T')
    plt.ylabel('lgk')
    plt.grid(alpha=0.5)
    plt.show()
