import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
card_number = ['3', '4', '5', '6', '9'] # 카드 번호는 3, 4, 5, 6, 9로 시작해야 한다.

for i in range(1, T + 1):
    data = list(input())

    if data[0] not in card_number: # 카드 번호의 시작이 3, 4, 5, 6 ,9이 아니면 0으로 출력
        print('#{} {}'.format(i, 0))
    elif len(data) - data.count('-') != 16: # '-'를 제외하고 숫자가 16개가 아니면 0으로 출력
        print('#{} {}'.format(i, 0))
    else:
        print('#{} {}'.format(i, 1)) # 이게 모두 성립하면 1로 출력

# if data[0] in card_number: # 카드 번호의 시작이 3, 4, 5, 6 ,9이면 1로 출력
#     print('#{} {}'.format(i, 1))
# elif len(data) - data.count('-') == 16: # '-'를 제외하고 숫자가 16개가 되면 1로 출력
#     print('#{} {}'.format(i, 1))
# else:
#     print('#{} {}'.format(i, 0)) # 이 둘 다 아니면 0으로 출력
# -> 실패(다시 생각했습니다.)