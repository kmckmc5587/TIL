# import sys

# sys.stdin = open("2063_input.txt", "r")

T = int(input())
score = list(map(int, input().split()))
score.sort()

for i in range(T):
    if i == T // 2:
        print(score[i])
        break