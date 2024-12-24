
Prime = [2]

def prime(x):
    for i in range(1,len(Prime)):
        if not x%Prime[i]:
            break
    else:
        return True
    return False


def demo():
    for i in range(3,1001,2):
        if(prime(i)):
            Prime.append(i)
    for i in range(len(Prime)):
        print(f'{Prime[i]}\t',end = '')
        if not (i+1)%8:
            print()

demo()
