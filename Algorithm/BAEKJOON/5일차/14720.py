N = int(input())
data = list(map(int, input().split()))
number = 0
result = 0

for i in range(len(data)):
    if data[i] == number:
        result += 1
        number += 1

    if number > 2:
        number = 0

print(result)