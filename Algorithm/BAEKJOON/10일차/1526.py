import sys

sys.stdin = open("1526.txt")

N = int(input()) # N이 주어진다.
while True: # 반복문 while 사용
    number = True # bool 자료형 -> True 사용

    for i in str(N):
        if i != '4' and i != '7': # 4나 7이 아니라면 count 해준다.
            number = False # bool 자료형 -> False 사용
            N -= 1 # 가장 큰 수를 구해야 하기 때문에
                   # 주어진 수에서 -1씩 하면서 구한다.

    if number: # 4나 7로만 이루어져 있으면 출력
        print(N)
        break