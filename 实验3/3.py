from string import digits
def demo():
    eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    a = input('请输入一个整数:')
    for i in a:
        if not i in digits:
            print('请输入一个正确的整数')
            return
    print(f'{a}的英文输出为:', end = '')
    for i in a:
        print(eng[int(i)], end = ' ')
    
demo()
