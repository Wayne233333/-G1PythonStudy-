from random import randint

def demo():
    for i in range(5):
        print(chr(randint(0,25)+97)*3, end = ' ')
    print('\n')

    for i in range(5):
        for j in range(randint(3, 5)):
            print(chr(randint(0, 25) +97), end = '')
        print(' ', end = '')

demo()

