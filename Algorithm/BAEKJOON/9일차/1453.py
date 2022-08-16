import sys

sys.stdin = open("1453.txt")

N = int(input()) # 손님의 수 = N
seat = map(int, input().split()) # 손님 자기가 앉고 싶은 자리
computer = [0] *  101 # 1 ~ 100번 컴퓨터
reject = 0 # 거절당하는 손님

for i in seat:
    if(computer[i] == 0): # 원하는 지리가 비어있다면
        computer[i] += 1
    else: # 그렇지 않다면
        reject += 1

print(reject) # 거절당하는 손님의 수 출력