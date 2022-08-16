# 1) while
n = 5
mul = 1
i = 1

while i <= 5:
    mul *= i
    i += 1

print(mul)

# 2) for
mul = 1
for num in range(1, 6):
    mul *= num

print(mul)