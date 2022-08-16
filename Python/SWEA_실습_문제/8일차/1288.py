import sys

sys.stdin = open("1288_input.txt", "r")

# T = int(input())
# for t in range(1, T + 1):
#     n = input()
#     a = [0 for _ in range(10)]
#     intn = int(n)
#     count = 1

#     while 0 in a:
#         for i in n:
#             if a[int(i)] > 0:
#                 continue
#             else:
#                 a[int(i)] += 1
#         count += 1
#         n = str(intn * count)
#     count -= 1
#     print('# %d %d' % (t, intn * count) )

T = int(input())
for test_case in range(1, T +1):
    # Input 가져오기
    N = int(input())
    N1 = N
    # Set에 계속 추가 예정
    numbers = set()
    # while 반복 => set 길이가 10이 될 때 까지
    while True:
        # for 반복 : 숫자를 문자로
        for n in str(N): 
        # numbers set에 계속 추가
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    print(f'#{test_case} {N}')

# N * cnt OK!