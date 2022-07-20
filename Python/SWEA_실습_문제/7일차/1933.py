# import sys

# sys.stdin = open("1933_input.txt", "r")

T = int(input())
for i in range(T):
    if T % (i + 1) == 0:
        print(i + 1, end = ' ')