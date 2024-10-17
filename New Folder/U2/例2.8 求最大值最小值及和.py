
def main():

    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    minn = x[0]
    maxn = x[0]
    Sum = x[0]

    for i in range(1,10):

        if x[i] < minn:   minn = x[i]
        if x[i] > maxn:   maxn = x[i]
        Sum += x[i]

    print(minn, maxn, Sum)

    print(min(x), max(x), sum(x))

if __name__ == "__main__":
    main()