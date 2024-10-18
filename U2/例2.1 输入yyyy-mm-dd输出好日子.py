def demo():
    data = input('请以yyyy-mm-dd的格式输入年月日：')
    y = data[:4]
    m = data[5:7]
    d = data[-2:]      # 这样把日切出来更简单，最后两个字符

    if m[0] == '0':     # 注意索引访问到的是字符，右边的0必须加引号
        m = m[-1]

    if d[0] == '0':     # 注意索引访问到的是字符，右边的0必须加引号
        d = d[-1]

    print(str(y) + '年' + str(m) + '月' + str(d) + '日是个好日子')

demo()

def demo1():
    data = input('请以yyyy-mm-dd的格式输入年月日：').split('-')
    y = int(data[0])
    m = int(data[1])
    d = int(data[2])      

    print(str(y) + '年' + str(m) + '月' + str(d) + '日是个好日子')

demo1()
