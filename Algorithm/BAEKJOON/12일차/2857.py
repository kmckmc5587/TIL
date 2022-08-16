import sys

sys.stdin = open("2857.txt")

list = []
for i in range(5):
    list.append(input())
resut = 0

for i in range(5):
    if 'FBI' in list[i]:
        print(i + 1, end = '')
        result = 1

if result == 0:
    print('HE GOT AWAY!')