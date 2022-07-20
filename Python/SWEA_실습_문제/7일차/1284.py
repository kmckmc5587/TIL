# import sys

# sys.stdin = open("1284_input.txt", "r")

T = int(input())
for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A_result = 0
    B_result = 0
    A_result += W * P
    B_result += Q
    if W > R:
        B_result += (W - R) * S

    print('#%d %d' % (i, min(A_result, B_result)))