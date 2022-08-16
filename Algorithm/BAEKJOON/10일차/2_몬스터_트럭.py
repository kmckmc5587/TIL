import sys

sys.stdin = open("2_몬스터_트럭.txt")

R, C = map(int, input().split()) # R = 행, C = 열
park = [input() for _ in range(R)] # park 리스트 생성
park_0, park_1, park_2, park_3, park_4 = 0, 0 ,0 ,0 ,0

for i in range(R - 1):
    for j in range(C - 1):
        w = park[i][j]
        x = park[i][j + 1]
        y = park[i + 1][j]
        z = park[i + 1][j + 1]
        sum_ = w + x + y + z

        if '#' in sum_: # 빌딩 -> '#' 부술 수 X
            continue
        else:
            cnt = sum_.count('X')
            if cnt == 0:
                park_0 += 1
            elif cnt == 1:
                park_1 += 1
            elif cnt == 2:
                park_2 += 1
            elif cnt == 3:
                park_3 += 1 
            elif cnt == 4:
                park_4 += 1

print(park_0)
print(park_1)
print(park_2)
print(park_3)
print(park_4)