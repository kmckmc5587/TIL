number = int(input())
count = 0
while number >= 1:
    number = number // 10
    count += 1
print(count)