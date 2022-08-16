import sys

sys.stdin = open("1264.txt")

vowel = ['a', 'e', 'i', 'o', 'u'] # 모음 = vowel -> 리스트로 만든다.

while True:
    count = 0
    w = list(input().lower()) # 문자열을 리스트로 받고 -> lower 함수 사용해서 소문자로 변경
    if w[0] == '#': # 만약에 첫 글자에 '#'이면 종료
        break
    for i in w:
        if i in vowel: # 모음이 있다면 1씩 count
            count += 1
    print(count)