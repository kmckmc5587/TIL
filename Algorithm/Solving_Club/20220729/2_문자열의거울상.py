import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for test_case in range(1, T + 1):

    case = input() # 각 테스트 케이스마다 입력받은 문자열(case)을 거꾸로 확인
    text = '' # 거울에 비추어 표헌되는 문자를 text 문자열에 추가

    for i in case[::-1]: # 문자를 뒤집어 주는 과정 # [::-1]을 빼먹어서 2번이나 틀렸습니다.
        if i == 'b':
            text += 'd' ## 처음에 texxt = 'd' 이렇게만 했는데 답이 아니여서 +=로 수정
        elif i == 'd':
            text += 'b'
        elif i == 'p':
            text += 'q'
        else:
            text += 'p'

    print("#{} {}".format(test_case, text)) # text 문자열 출력

# T = int(input())
# for test_case in range(1, T + 1):
#     text = list(input()) # text라는 리스트 생성
#     text.reverse() # reverse 사용해서 뒤집는다.

#     for i in range(len(text)): # b는 d로 d는 b로, p는 q로 q는 p로 변환한다.
#         if text[i] == 'b':
#             text[i] = 'd'
#         elif text[i] == 'd':
#             text[i] = 'b'
#         elif text[i] == 'p':
#             text[i] = 'q'
#         else:
#             text[i] ='p'

#     print("#{} {}".format(test_case, text)) # text 문자열 출력

#  이렇게도 풀어봤는데 결과가
# #1 ['p', 'q', 'q', 'b', 'd']
# #2 ['b', 'd', 'd', 'q', 'q', 'q', 'p', 'p', 'p', 'p']