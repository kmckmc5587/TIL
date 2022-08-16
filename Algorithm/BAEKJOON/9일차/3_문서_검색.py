import sys

sys.stdin = open("3_문서_검색.txt")

word = input() # 전체 단어
W = input() # 해당 단어
print(word.count(W)) # 중복되지 않게 최대 몇 번 등장하는지(count 함수 사용)