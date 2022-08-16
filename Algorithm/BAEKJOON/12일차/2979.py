import sys

sys.stdin = open("2979.txt")

A, B, C = map(int, input().split()) # 주차요금 A, B, C
arr = [0] * 100
result = 0

for _ in range(3):
    arrive, depart = map(int, input().split()) # 도착 = arrive, 출발 = depart
    for i in range(arrive, depart): arr[i] += 1

for j in arr:
    result += {0 : 0, 1 : A, 2 : B * 2, 3 : C * 3}[j]
print(result)