import sys

sys.stdin = open("1371.txt")

word = [0] * 26
w = sys.stdin.read()
for i in w:
    if i.islower(): # 소문자
        word[ord(i) - 97] += 1

for i in range(len(word)):
    if word[i] == max(word): # 리스트의 인덱스가 최대값이라면
        print(chr(97 + i), end = '') # 문자를 알파벳 순서로 출력