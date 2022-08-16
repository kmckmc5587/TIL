import sys

sys.stdin = open("11170.txt")

T = int(input())
for i in range(T):
    count = 0
    N, M = map(int, input().split()) # N, M(N 부터 M 까지의 수들)

    for i in range(N, M + 1):
        zero = str(i) # 문자열로 받는다.
        count += zero.count('0') # '0'이 나올 시에 카운트
    
    print(count) # count를 출력