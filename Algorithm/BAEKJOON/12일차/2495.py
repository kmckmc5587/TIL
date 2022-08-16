import sys

sys.stdin = open("2495.txt")

for _ in range(3):
    s = str(input())
    word = 1
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            word = max(count, word)
            count = 1
    word = max(count, word)
    print(word)