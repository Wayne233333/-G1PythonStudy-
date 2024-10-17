
tot = 0

for i in range(1, 101):
    if not i % 7 or '7' in str(i):

        tot += 1
        print(i, end = ' ')

        if tot % 10 == 0:
            print()