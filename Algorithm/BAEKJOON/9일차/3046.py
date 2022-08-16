import sys

sys.stdin = open("3046.txt")

R1, S = input().split()
# S = (R1 + R2) / 2 -> R2 = (S * 2) - R1 
print(int(S) * 2 - int(R1))

R1, S = map(int, input().split())
print(S * 2 - R1)