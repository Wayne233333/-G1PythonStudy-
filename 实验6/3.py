
yuanyin = 'aeiou'

def jdg(x):
    for i in yuanyin:
        if i not in x:
            return False
    return True

def demo():
    x = input("请输入一个单词：")
    if jdg(x):
        print(f'{x}包含每个元音字母')
    else:
        print(f'{x}不是元音单词')


demo()
