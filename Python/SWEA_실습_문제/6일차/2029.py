# import sys

# sys.stdin = open("2029_input.txt", "r")

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print("#%d %d %d" % (t + 1, a // b, a % b))