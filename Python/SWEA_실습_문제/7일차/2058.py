# import sys

# sys.stdin = open("2058_input.txt", "r")

T = input()

result = 0
for i in range(len(T)) :
    result += int(T[i])

print(result)