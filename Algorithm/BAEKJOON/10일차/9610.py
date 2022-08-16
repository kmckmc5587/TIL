import sys

sys.stdin = open("9610.txt")

n = int(input())
Q1, Q2, Q3, Q4, axis = 0, 0, 0, 0, 0 # 1사분면, 2사분면, 3사분면, 4사분면, 축
                                     # 축은 x의 값이나 y의 값 중 하나면 0이면 성립

for i in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0: # 1사분면
        Q1 += 1
    elif y > 0 and x < 0: # 2사분면
        Q2 += 1
    elif x < 0 and y < 0: # 3사분면
        Q3 += 1
    elif x > 0 and y < 0: # 4사분면
        Q4 += 1
    elif x == 0 or y == 0: # 축 -> x의 값이 0이거나 y의 값이 0
        axis += 1

print('Q1: ' + str(Q1)) # Q1: ... -> 이 형태이기 때문에 print('Q1: ' + str(Q1)) 이렇게 표현
print('Q2: ' + str(Q2))
print('Q3: ' + str(Q3))
print('Q4: ' + str(Q4))
print('AXIS: ' + str(axis))