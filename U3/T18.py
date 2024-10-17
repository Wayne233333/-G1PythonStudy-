
for i in range(1,10):
    print(' '*(7*(9-i)), end = '')
    for j in range(1,i+1):
        print(f'{i}*{j}={" "*(2-len(str(i*j)))}{i*j} ', end = '')
    print()