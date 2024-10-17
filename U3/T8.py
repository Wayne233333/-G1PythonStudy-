
from random import randint

a = randint(10,99)  #不能直接在20～198范围里取Sum，题目中取到每个Sum的概率不同
b = randint(10,99)
Sum = a + b
print(Sum)

while True:

    ans = int(input("guess ans pls: "))
    if ans == Sum:
        print("正确")
        break
    
    if ans > Sum:
        op = "big"
    else:
        op = "small"

    print(f"错误\nthe num you guess is too {op}")
