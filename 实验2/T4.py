from random import randint

def demo():
    op = False
    a = chr(randint(0,25) + 65)
    while not op:
        b = ''
        for i in range(7):
            c = randint(0,61)
            if c <= 25:
                b += chr(c + 65)
            elif c <= 51:
                b += chr(c + 71)
            else:
                b += chr(c - 4)
                op = True
    print(a+b)
demo()
                
