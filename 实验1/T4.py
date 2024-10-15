
def demo():

    a = input("请输入一个三位整数")

    while(True):

        try:
            int(a)
        except:
            a = input("请输入数字，而不是字符串！")
            continue

        if len(a) != 3:
            a = input("请输入一个正确的三位整数！")
            continue

        if a == a[::-1]:
            print(f'{a}是一个对称的三位数')
        else:
            print(f'{a}不是一个对称的三位数')

        break
    
def main():
    demo()

if __name__ == '__main__':
    main()