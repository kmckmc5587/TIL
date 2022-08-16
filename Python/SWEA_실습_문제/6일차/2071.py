# import sys

# sys.stdin = open("2071_input.txt", "r")

T = int(input())
for t in range(0, T):
    numbers = list(map(int, input().split()))
    print("#%d %d" % (t + 1, round(sum(numbers)/10)))