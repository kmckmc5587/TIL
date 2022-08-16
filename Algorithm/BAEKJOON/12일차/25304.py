import sys

sys.stdin = open("25304.txt")

X = int(input()) # 총 금액 = X
N = int(input()) # 종류의 수 = N
x = 0

for i in range(N):
    a, b = map(int, input().split()) # 물건의 가격 = a, 물건의 개수 = b
    c = a * b
    x = x + c

if X == x:
    print('Yes')
else:
    print('No')