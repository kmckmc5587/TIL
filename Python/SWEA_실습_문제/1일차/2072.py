# import sys

# sys.stdin = open("2072_input.txt", "r")

T = int(input())
 
for t in range(1, T + 1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        if i % 2 != 0:
            answer += i
    print("#"+ str(t), str(answer))