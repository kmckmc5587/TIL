import sys

sys.stdin = open("5800.txt")

K = int(input())
for i in range(1, K + 1):
    print('Class %d' %(i)) # 'Class X' 출력
    score = list(map(int, input().split()))
    max_gap = 0
    count = score[0] # 개수 저장
    score = score[1:] # 개수빼고 값들로만
    score.sort(reverse = True) # 값들 -> 내림차순

    for i in range(count - 1):
        gap = abs(score[i] - score[i + 1]) # 값들 차이 구하기
        if gap > max_gap: # 가장 큰 차이나는 값 저장
            max_gap = gap

    print('Max %d, Min %d, Largest gap %d' %(max(score), min(score), max_gap))