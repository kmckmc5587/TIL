import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for i in range(1, T + 1): # T로 했다가 틀렸습니다. T + 1로 수정
    data = list(map(int, input().split()))
    sum = 0 # 합
    result = 0

    for j in range(len(data)): # 홀수인 경우에는 * 2
        if (j + 1) % 2 == 1:
            sum += data[j] * 2
        else: # 짝수인 경우에는 그대로 나와서 더해준다.
            sum += data[j]

    if sum % 10 == 0: # 합이 10의 배수 일 때는 더할 필요가 없으므로 0으로 출력
        result = 0
    else: # 합이 10으 배수가 아닐 경우에는 10에서 합의 나머지를 빼준 값을 출력
        result = 10 - (sum % 10)

    print('#{} {}'.format(i, result))