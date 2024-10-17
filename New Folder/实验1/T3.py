
from random import randint

def demo():

    l = [randint(1,999) for i in range(10)]

    print(f'一组数：{l}\n{round(sum(l)/len(l),3)}')

def main():
    demo()

if __name__ == "__main__":
    main()