# import sys

# sys.stdin = open("2068_input.txt", "r")

T = int(input())
for i in range(1, T + 1):
    t = map(int, input().split())
    print(f"#{i} {max(t)}")