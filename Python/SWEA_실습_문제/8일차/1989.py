# import sys

# sys.stdin = open("1989_input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    word = input()
    for i in range(len(word) // 2):
        if word[i] == word[-1 -i]:
            correct = 1
        else:
            correct = 0
    print('#%d %d' % (t, correct))