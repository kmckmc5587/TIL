N = int(input())
A = N

for i in range(N):
    if i % 2 == 0:
        print('* ' * A)
    elif i % 2 == 1:
        print(' *' * A)