M = int(input())
# cup = [1, 2, 3] # IndexError: list index out of range
cup = [0, 1, 2, 3]

for i in range(M):
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]

print(cup.index(1)) # 첫째 줄 공이 들어있는 컵 번호 출력