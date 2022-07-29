import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    score = [0] * 101 # 101까지 한 이유는 점수는 0 ~ 100까지기 때문에

    for i in range(len(num)): # 학생 수 만큼 반복
        score[100 - num[i]] += 1 # 점수를 인덱스로 받는다. 1씩 올려준다.
                               # 100이 score[0]에 들어가도록, 순서를 거꾸로 받아서 최대값의 인덱스를 구해준다.
    max_score = score[0]

    for j in range(1, 101):
        if max_score < score[j]:
            max_score = score[j]

    result = 100 - score.index(max_score) # 100에서 뺀 이유는 인덱스를 구하면
                                          # 앞에 있는 값의 인덱스를 추출해주기 때문에 거꾸로했다.
    print("#{} {}".format(t, result))