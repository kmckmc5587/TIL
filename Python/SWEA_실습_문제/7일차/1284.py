# import sys

# sys.stdin = open("1284_input.txt", "r")

T = int(input())
for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    B = 0
    if W < R:
        B = Q
    else:
        B = Q + (W - R) * S
    
    if A < B:
        print('#%d %d' % (i, A))
    else:
        print('#%d %d' % (i, B))