import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(1, T + 1):
    number = list(map(int,input().split())) # 3개의 숫자
    number.sort() # 정렬하기 위해 sort 사용
 
    if number[0] != number[1]: # 0, 1, 2번째 숫자가 주어지기 때문에 생각할 경우는 0번째, 1번째가 다를 때와
        print('#{} {}'.format(i, number[0])) # 무조건 0번째 숫자와 같아야 한다.
    else: # 0번째, 1번째가 같을 때
        print('#{} {}'.format(i, number[2])) # 무조건 2번째 숫자와 같아야 한다.