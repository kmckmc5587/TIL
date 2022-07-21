# import sys

# sys.stdin = open("1926_input.txt", "r")

T = int(input())
clap = ['3', '6', '9']

for t in range(1, T + 1):
    count = 0
    for i in str(t):
        if i in clap:
            count += 1
    if count > 0:
        t = '-' * count
    print(t, end = ' ')