import sys

sys.stdin = open("문제21_input.txt", "r")

a = int(input())
b = (a // 1000) + (((a % 1000) // 100) * 10) + (((a % 100) // 10) * 100) + ((a % 10) * 1000)
print(b)

# 정수 number가 주어질 때, 뒤집어서 출력하기
number = 123

# print(int(str(number)[::-1]))
result = 0
while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number %10
    # number를 깎는다.
    number //= 10
    
print(result)