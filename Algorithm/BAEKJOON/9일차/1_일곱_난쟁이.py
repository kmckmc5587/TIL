import sys

sys.stdin = open("1_일곱_난쟁이.txt")

# 이중 for문 사용
N = []
for i in range(9):
    N.append(int(input()))
sum = sum(N) # 키의 합
N.sort() # 오름차순 정렬

# 원래는 일곱 난쟁이 / 현재는 아홉 난쟁이 -> 백설공주의 일곱 난쟁이가 아닌 두 명 속출 -> 출력하지 않는다.
# 일곱 난쟁이의 키의 합 = 100 -> 전체 합 - (백설공주 난쟁이 X) = 100
for i in range(9):
    for j in range(9):
        if sum - (N[i] + N[j]) == 100: # 두 난쟁이 제외하고 합이 100
            for k in range(9):
                if k == i or k == j: # 두 난쟁이를 제외한다.
                    continue
                else:
                    print(N[k]) # 일곱 난쟁이 출력
                    
            exit() # exit()를 사용해서 함수 종료 # 사용 안 하면 틀린 답