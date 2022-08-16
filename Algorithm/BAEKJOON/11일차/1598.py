import sys

sys.stdin = open("1598.txt")

N, M = map(int, input().split())
N1 = (N - 1) // 4 + 1
M1 = (N - 1) % 4
N2 = (M - 1) // 4 + 1
M2 = (M - 1) % 4

print(abs(N2 - N1) + abs(M2 - M1))