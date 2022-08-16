import sys

sys.stdin = open("2587.txt")

number = []
for i in range(5):
    number.append(int(input()))
avg = sum(number) // 5
number.sort() # 크기 순서대로

print(avg) # 평균 출력
print(number[2]) # 중앙값을 출력(0, 1, 2, 3, 4) 중앙에 있는 [2] 출력