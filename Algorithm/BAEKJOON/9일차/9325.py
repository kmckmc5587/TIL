import sys

sys.stdin = open("9325.txt")

for i in range(int(input())):
    s = int(input()) # 자동차 가격 = s

    for i in range(int(input())):
        q, p = map(int, input().split()) # 특정 옵션 = q, 해당 옵션 = p
        s += q * p
    print(s)