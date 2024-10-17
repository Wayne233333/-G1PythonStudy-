
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']

def demo():

    a = int(input('请输入月份：'))

    for i in range(3):
        print(f'{a}月的月份简写是{month[a-1]}')

def main():
    demo()

if __name__ == "__main__":
    main()