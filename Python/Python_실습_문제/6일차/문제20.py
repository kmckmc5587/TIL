# import sys

# sys.stdin = open("문제20_input.txt", "r")

N = 123
answer = 0
for n in str(N):
	answer += int(n)
print(answer)

# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.
number = 123
# number가 0일 때 Stop!
# => int는 0일 때 False
result = 0
while number:
	# 몫은 다음 number가 됨
	# 나머지는 더해나가면 된다!

	# 1.
	# result += number % 10
	# number //= 10
	
	# 2.
	# divmod(x, y)는 x를 y로 나누고,
	# 결과를 tuple로 반환
	# (몫, 나머지)
	number, remainder = divmod(number, 10)
	result += remainder

print(result)