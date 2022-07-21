# import sys

# sys.stdin = open("1976_input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2
    if h > 12:
        h = h - 12
    if m >= 60:
        h = h + 1
        m = m - 60
    print('#%d %d %d' % (t, h, m))