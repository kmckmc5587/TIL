import sys

sys.stdin = open("문제21_input.txt", "r")

a = int(input())
b = (a // 1000) + (((a % 1000) // 100) * 10) + (((a % 100) // 10) * 100) + ((a % 10) * 1000)
print(b)