numbers = [0, 20, 100]

max = 0
for num in numbers:
    if(num > max):
        max = num
print(max)

#최댓값 구하기
numbers = [0, 20, 100, 40]
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if max_num < n:
        max_num = n
    print(max_num)