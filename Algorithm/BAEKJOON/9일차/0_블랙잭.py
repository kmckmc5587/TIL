import sys

sys.stdin = open("0_블랙잭.txt")

N, M = map(int, input().split()) # 카드의 개수 = N, 3장의 카드의 합에 가까운 수 = M
card = list(map(int, input().split())) # 카드의 쓰여져 있는 수들을 리스트 저장
result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):

            if card[i] + card[j] + card[k] > M: # 세 카드 숫자의 합이 M보다 크면
                continue # continue
            else:
                result = max(result, card[i] + card[j] + card[k]) # 크지 않을 경우 정답에 근접
                                                                  # 100보다 크면 X
print(result)


# def blackjack(N, M, card):
#     max_total = 0 # 현재 가장 큰 합
#     for i in range(N - 2):
#         for j in range(i + 1, N - 1):
#             for k in range(j + 1, N):
#                 total = card[i] + card[j] + card[k]

#                 if max_total < total <= M: # 현재 가장 큰 합보다는 크고, M을 넘으면 X
#                     max_total = total

#                 if total == M: # 합과 M이 같으면 X
#                     return total

#     return max_total