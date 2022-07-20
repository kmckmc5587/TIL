# import sys

# sys.stdin = open("2043_input.txt", "r")

P, K = map(int, input().split())
count = 0
while P >= K:
    K += 1
    count += 1
print(count)