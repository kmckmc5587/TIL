N = list(map(int, input().split()))
result = [1, 2, 3, 4, 5, 6, 7, 8]

if N == result:
    print('ascending')
elif N == result[::-1]:
    print('dsecending')
else:
    print('mixed')