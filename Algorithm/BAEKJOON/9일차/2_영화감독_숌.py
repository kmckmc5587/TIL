import sys

sys.stdin = open("2_영화감독_숌.txt")

N = int(input())
end = 666 # 종말 제목 = 666
count = 0

while True:
    if '666' in str(end): # '666'이 포함되어 있다면
        count += 1 # 카운트
    if count == N: # N과 같다면
        print(end) # end 출력
        break # while문 종료
    end += 1 # '666' 나올 때 까지 end를 1씩 증가