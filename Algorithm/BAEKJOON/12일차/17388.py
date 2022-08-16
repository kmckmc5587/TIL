import sys

sys.stdin = open("17388.txt")

S, K, H = map(int, input().split())
dic = {S : 'Soongsil', K : 'Korea', H : 'Hanyang'} # 딕셔너리 사용

if S + K + H >= 100: # 참여도의 합이 100 이상이면 OK 출력
    print('OK')
else: # 참여도가 가장 낮은 학교 출력
    print(dic[min(S, K, H)])