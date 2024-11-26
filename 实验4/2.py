from random import randint
def demo():
    a = randint(1, 10)
    b = randint(1, 10)
    if a < b:
        a, b = b, a
    ans = a - b
    while True:
        i = int(input(f'What is {a}-{b} = '))
        if i == ans:
            print('You got it')
            break
        print('Wrong! ', end = '')
demo()
