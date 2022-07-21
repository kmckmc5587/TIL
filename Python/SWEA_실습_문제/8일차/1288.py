# import sys

# sys.stdin = open("1288_input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    n = input()
    a = [0 for _ in range(10)]
    intn = int(n)
    count = 1

    while 0 in a:
        for i in n:
            if a[int(i)] > 0:
                continue
            else:
                a[int(i)] += 1
        count += 1
        n = str(intn * count)
    count -= 1
    print('# %d %d' % (t, intn * count) )