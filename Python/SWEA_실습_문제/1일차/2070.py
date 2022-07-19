# import sys

# sys.stdin = open("2070_input.txt", "r")

T = int(input())
for t in range(0, T):
    a, b = map(int, input().split())
    print( f"#{t + 1} ", end = '' )
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")