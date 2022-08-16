import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(T):
    N = int(input())
    score = list(map(int, input().split())) # 리스트 값들을 모두 더해준다(sum 활용)
    sum = 0

    for j in score:
        sum += int(j)
    average = sum / N # 평균을 구한다. average = 합 / 갯수
    count = 0
    
    for j in score:
        if int(j) <= average: # 구한 값들 중 평균이하 값들을 카운트
            count += 1

    print("#{} {}".format(i + 1, count)) # 카운트 출력